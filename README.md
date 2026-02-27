# TechStack Scanner

**Instantly detect every technology behind any website** — frameworks, CMS platforms, analytics tools, CDNs, JavaScript libraries, and more.

TechStack Scanner is a command-line tool that reveals the full technology stack of any website. Point it at a URL (or a list of URLs) and get a clean, detailed breakdown of what powers that site.

Perfect for competitive analysis, security audits, lead generation, and tech due diligence.

---

## Example Output

```
╔══════════════════════════════════════════════════════════╗
║                   TechStack Scanner                      ║
║           Powered by Technology Detection API             ║
╚══════════════════════════════════════════════════════════╝

  ✓ https://github.com  —  14 technologies detected

   Technology             Category              Version     Confidence
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Ruby on Rails          Web frameworks        7.1              100%
   React                  JavaScript frameworks 18.2.0            99%
   Nginx                  Web servers           -                 95%
   webpack                Build tools           5.x               98%
   GitHub Pages           Hosting               -                 90%
   Cloudflare             CDN                   -                 95%
   Google Analytics       Analytics             GA4               92%
   Turbo                  JavaScript frameworks 7.3               88%
   Redis                  Databases             -                 85%
   Elasticsearch          Search engines        -                 80%
   Primer CSS             UI frameworks         21.0              95%
   D3.js                  JavaScript libraries  7.8               78%
   Node.js                Programming languages 18.x              90%
   Polaris                Security              -                 70%

  ✓ https://shopify.com  —  11 technologies detected

   Technology             Category              Version     Confidence
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Ruby on Rails          Web frameworks        7.0              100%
   React                  JavaScript frameworks 18.2.0            99%
   Next.js                Web frameworks        14.1              97%
   Cloudflare             CDN                   -                 95%
   Contentful             CMS                   -                 88%
   TypeScript             Programming languages 5.x               92%
   Google Tag Manager     Tag managers          -                 90%
   Tailwind CSS           UI frameworks         3.4               85%
   Fastly                 CDN                   -                 80%
   Snowplow               Analytics             -                 75%
   Liquid                 Template engines      -                 95%
```

## Get Started

### 1. Get your API key

This tool uses the [Technology Detection API](https://rapidapi.com/dapdev-dapdev-default/api/technology-detection-api) — a fast, accurate technology profiling service.

Sign up on RapidAPI and subscribe to get your API key (free tier available).

### 2. Install

```bash
git clone https://github.com/deividi86/techstack-scanner.git
cd techstack-scanner
pip install -r requirements.txt
```

### 3. Set your API key

```bash
export RAPIDAPI_KEY="your-key-here"
```

Or create a `.env` file in the project directory:

```
RAPIDAPI_KEY=your-key-here
```

### 4. Scan

**Single URL:**

```bash
python scanner.py github.com
```

**Multiple URLs:**

```bash
python scanner.py github.com shopify.com stripe.com
```

**From a file:**

```bash
python scanner.py -f urls.txt
```

**JSON output (for piping to other tools):**

```bash
python scanner.py -o json github.com | jq .
```

## Use Cases

- **Competitive Analysis** — See what tech your competitors use and find their weak spots.
- **Sales Prospecting** — Find companies using specific technologies and target your outreach.
- **Security Audits** — Identify outdated frameworks and known-vulnerable components.
- **Tech Due Diligence** — Evaluate a company's tech stack before acquisition or investment.
- **Market Research** — Map technology adoption trends across industries.

## How It Works

The scanner sends each URL to the [Technology Detection API](https://rapidapi.com/dapdev-dapdev-default/api/technology-detection-api), which analyzes HTTP headers, HTML content, JavaScript variables, cookies, and DNS records to identify technologies with high accuracy.

## License

MIT License — see [LICENSE](LICENSE) for details.
