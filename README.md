# TechStack Scanner — Detect Any Website's Technology Stack

![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

Instantly discover what technologies power any website — frameworks, CDNs, analytics, CMS, and more — using the [Technology Detection API](https://rapidapi.com/dapdev-dapdev-default/api/technology-detection-api) on RapidAPI.

## Quick Demo

```
$ python scanner.py https://stripe.com

Technology Stack for stripe.com
──────────────────────────────────────────────────

  CDN:
    Cloudflare                ██████████ 100%

  JavaScript frameworks:
    React v18.2               █████████░ 90%

  Web servers:
    Nginx                     ████████░░ 80%

  Analytics:
    Segment                   ██████████ 100%
```

## Installation

```bash
git clone https://github.com/deividi86/techstack-scanner.git
cd techstack-scanner
pip install -r requirements.txt
```

## Usage

1. Get your free API key from [RapidAPI — Technology Detection API](https://rapidapi.com/dapdev-dapdev-default/api/technology-detection-api)
2. Set your key:

```bash
export RAPIDAPI_KEY="your-key-here"
```

3. Scan any website:

```bash
python scanner.py https://example.com

# Raw JSON output
python scanner.py https://stripe.com --json
```

## Use Cases

- **Competitive Intelligence** — See what tech your competitors are running
- **Lead Qualification** — Identify prospects using specific technologies
- **Security Audits** — Discover exposed technologies and versions
- **Market Research** — Analyze technology adoption trends at scale

## API

This tool is powered by the [Technology Detection API on RapidAPI](https://rapidapi.com/dapdev-dapdev-default/api/technology-detection-api).

## License

MIT — see [LICENSE](LICENSE)
