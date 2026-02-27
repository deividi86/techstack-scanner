#!/usr/bin/env python3
"""
TechStack Scanner — Detect technologies used by any website.

Uses the Technology Detection API via RapidAPI.
Get your API key at: https://rapidapi.com/dapdev-dapdev-default/api/technology-detection-api
"""

import argparse
import json
import os
import sys

import requests

API_URL = "https://technology-detection-api.p.rapidapi.com/api/v1/technology-detection/detect"

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.text import Text
    from rich import box
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False


def get_api_key():
    """Retrieve the RapidAPI key from environment or .env file."""
    key = os.environ.get("RAPIDAPI_KEY")
    if key:
        return key
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line.startswith("RAPIDAPI_KEY="):
                    return line.split("=", 1)[1].strip().strip("\"'\"")
    return None


def detect_technologies(url: str, api_key: str) -> dict:
    """Call the Technology Detection API for a single URL."""
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "technology-detection-api.p.rapidapi.com",
        "Content-Type": "application/json",
    }
    payload = {"url": url}
    resp = requests.post(API_URL, json=payload, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json()


def normalize_url(url: str) -> str:
    """Ensure the URL has a scheme."""
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    return url


# ---------------------------------------------------------------------------
# Rich (pretty) output
# ---------------------------------------------------------------------------

def print_results_rich(results: list[dict]):
    console = Console()
    console.print()
    console.print(
        Panel(
            Text("TechStack Scanner", style="bold cyan", justify="center"),
            subtitle="Powered by Technology Detection API",
            box=box.DOUBLE,
        )
    )
    console.print()

    for entry in results:
        url = entry["url"]
        techs = entry.get("technologies", [])
        error = entry.get("error")

        if error:
            console.print(f"  [bold red]✗[/] {url} — {error}")
            console.print()
            continue

        console.print(f"  [bold green]✓[/] [bold]{url}[/]  —  [dim]{len(techs)} technologies detected[/dim]")
        console.print()

        if not techs:
            console.print("    [dim]No technologies detected.[/dim]\n")
            continue

        table = Table(box=box.SIMPLE_HEAVY, show_header=True, header_style="bold magenta", pad_edge=False)
        table.add_column("Technology", style="cyan", min_width=20)
        table.add_column("Category", style="yellow", min_width=18)
        table.add_column("Version", style="green", min_width=8)
        table.add_column("Confidence", justify="right", style="white", min_width=10)

        for tech in sorted(techs, key=lambda t: t.get("category", "")):
            name = tech.get("name", "Unknown")
            category = tech.get("category", "-")
            version = tech.get("version") or "-"
            confidence = tech.get("confidence")
            conf_str = f"{confidence}%" if confidence is not None else "-"
            table.add_row(name, category, version, conf_str)

        console.print(table)
        console.print()


# ---------------------------------------------------------------------------
# Plain-text fallback output
# ---------------------------------------------------------------------------

def print_results_plain(results: list[dict]):
    print()
    print("=" * 60)
    print("  TechStack Scanner")
    print("  Powered by Technology Detection API")
    print("=" * 60)
    print()

    for entry in results:
        url = entry["url"]
        techs = entry.get("technologies", [])
        error = entry.get("error")

        if error:
            print(f"  [ERROR] {url} — {error}")
            print()
            continue

        print(f"  {url}  —  {len(techs)} technologies detected")
        print("-" * 60)

        if not techs:
            print("    No technologies detected.\n")
            continue

        header = f"  {Technology:<22} {Category:<20} {Version:<10} {Confidence:>10}"
        print(header)
        print("  " + "-" * 56)

        for tech in sorted(techs, key=lambda t: t.get("category", "")):
            name = tech.get("name", "Unknown")
            category = tech.get("category", "-")
            version = tech.get("version") or "-"
            confidence = tech.get("confidence")
            conf_str = f"{confidence}%" if confidence is not None else "-"
            print(f"  {name:<22} {category:<20} {version:<10} {conf_str:>10}")

        print()


# ---------------------------------------------------------------------------
# JSON output
# ---------------------------------------------------------------------------

def print_results_json(results: list[dict]):
    print(json.dumps(results, indent=2))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Detect technologies used by websites.",
        epilog="Get your API key at https://rapidapi.com/dapdev-dapdev-default/api/technology-detection-api",
    )
    parser.add_argument("urls", nargs="*", help="One or more URLs to scan")
    parser.add_argument("-f", "--file", help="File containing URLs (one per line)")
    parser.add_argument("-o", "--output", choices=["table", "json"], default="table", help="Output format (default: table)")
    parser.add_argument("-k", "--key", help="RapidAPI key (or set RAPIDAPI_KEY env var)")
    args = parser.parse_args()

    urls = list(args.urls or [])
    if args.file:
        with open(args.file) as fh:
            urls.extend(line.strip() for line in fh if line.strip() and not line.startswith("#"))

    if not urls:
        parser.print_help()
        sys.exit(1)

    api_key = args.key or get_api_key()
    if not api_key:
        print("Error: No API key provided.", file=sys.stderr)
        print("Set RAPIDAPI_KEY env var, create a .env file, or use --key.", file=sys.stderr)
        print("Get your key at https://rapidapi.com/dapdev-dapdev-default/api/technology-detection-api", file=sys.stderr)
        sys.exit(1)

    results = []
    for raw_url in urls:
        url = normalize_url(raw_url)
        try:
            data = detect_technologies(url, api_key)
            techs = data if isinstance(data, list) else data.get("technologies", data.get("results", []))
            if isinstance(techs, dict):
                techs = techs.get("technologies", [])
            results.append({"url": url, "technologies": techs if isinstance(techs, list) else []})
        except requests.exceptions.HTTPError as exc:
            results.append({"url": url, "error": f"HTTP {exc.response.status_code}: {exc.response.text[:200]}", "technologies": []})
        except Exception as exc:
            results.append({"url": url, "error": str(exc), "technologies": []})

    if args.output == "json":
        print_results_json(results)
    elif RICH_AVAILABLE:
        print_results_rich(results)
    else:
        print_results_plain(results)


if __name__ == "__main__":
    main()
