#!/usr/bin/env python3
"""One-shot static site generator for aipulse.lk"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
SITE = "https://aipulse.lk"

PRODUCTS = [
    {
        "slug": "pulsemind",
        "name": "PulseMind",
        "tag": "Enterprise AI Copilot",
        "kicker": "Copilot",
        "lead": "A thinking partner for every team. Draft, decide, and deliver with an assistant that already knows your business.",
        "summary": "PulseMind is AI Pulse's enterprise copilot. It connects to your knowledge, tools, and policies so every answer is grounded, permission-aware, and on-brand.",
        "image": "product-mind.png",
        "color": "#64d2ff",
        "features": [
            ("Grounded answers", "Retrieval from your approved sources, with citations you can audit."),
            ("Private by design", "Regional residency in Sri Lanka or your own VPC. Your data is not used to train public models."),
            ("Works where you work", "Microsoft 365, Slack, browser, and a native API for your own apps."),
            ("Policy aware", "Role-based access, redaction, and human-in-the-loop for sensitive actions."),
            ("Multilingual", "Sinhala, Tamil, and English — with the same quality bar."),
            ("Admin console", "Usage, quality, and cost in one glass cockpit."),
        ],
        "specs": [
            ("Deployment", "SaaS, private cloud, or on-premises"),
            ("Models", "Pulse Foundation + bring-your-own model"),
            ("Integrations", "120+ connectors via PulseConnect"),
            ("Security", "SOC 2 Type II, ISO 27001, GDPR"),
            ("SLA", "99.9% uptime, 24/7 regional support"),
        ],
    },
    {
        "slug": "pulseflow",
        "name": "PulseFlow",
        "tag": "Intelligent Automation",
        "kicker": "Automation",
        "lead": "Turn tribal process into living systems. PulseFlow watches, learns, and runs the work that used to wait on inboxes.",
        "summary": "PulseFlow is the automation fabric for modern operations. Document intelligence, human checkpoints, and event-driven workflows in one canvas.",
        "image": "product-flow.png",
        "color": "#5e5ce6",
        "features": [
            ("Visual canvas", "Design journeys as clearly as a keynote slide."),
            ("Document AI", "Extract, classify, and route any PDF, scan, or email."),
            ("Human in the loop", "Approvals with context, not another form."),
            ("Event native", "React to webhooks, queues, and schedules."),
            ("Observability", "Every step is timed, logged, and replayable."),
            ("No lock-in", "Export definitions as open YAML."),
        ],
        "specs": [
            ("Runtime", "Cloud, hybrid, or air-gapped"),
            ("Triggers", "API, email, file, queue, schedule"),
            ("Builders", "Studio, code SDK, and templates"),
            ("Scale", "Millions of runs per day"),
            ("Compliance", "Full audit trail and versioning"),
        ],
    },
    {
        "slug": "pulsecloud",
        "name": "PulseCloud",
        "tag": "AI Cloud Platform",
        "kicker": "Platform",
        "lead": "The quiet infrastructure behind extraordinary products. Train, serve, and govern models without the noise.",
        "summary": "PulseCloud is a managed AI platform: GPU fleets, feature stores, evaluation, and governed endpoints — tuned for South Asia and global enterprises.",
        "image": "product-cloud.png",
        "color": "#2997ff",
        "features": [
            ("Elastic inference", "Autoscaling endpoints with predictable cost."),
            ("Eval studio", "Offline and online evaluation before you ship."),
            ("Feature store", "Shared, versioned signals across teams."),
            ("Cost guardrails", "Budgets, quotas, and model routing."),
            ("Colombo region", "Low-latency serving for Sri Lanka and the Indian Ocean."),
            ("Open stack", "Kubernetes, OpenTelemetry, and your IAM."),
        ],
        "specs": [
            ("Compute", "NVIDIA GPU pools + CPU burst"),
            ("Regions", "Colombo, Singapore, Mumbai, Frankfurt"),
            ("MLOps", "CI for models, canaries, rollback"),
            ("Networking", "PrivateLink and VPC peering"),
            ("Support", "Named TAM on Scale plans"),
        ],
    },
    {
        "slug": "pulsesecure",
        "name": "PulseSecure",
        "tag": "Adaptive Security",
        "kicker": "Security",
        "lead": "Security that learns as fast as the threat. Identity, data, and AI risk — in one pulse.",
        "summary": "PulseSecure protects people, models, and data. Adaptive access, prompt-injection defense, and a single timeline of risk.",
        "image": "product-secure.png",
        "color": "#30d158",
        "features": [
            ("AI firewall", "Inspect prompts, tools, and outputs in real time."),
            ("Identity pulse", "Risk-based MFA that stays out of the way."),
            ("Data maps", "Know where sensitive knowledge lives."),
            ("SOC copilot", "Triage with PulseMind, act with PulseFlow."),
            ("Zero trust", "Device, location, and behavior — continuously."),
            ("Red team kits", "Built-in evaluations for LLM applications."),
        ],
        "specs": [
            ("Coverage", "Apps, APIs, models, endpoints"),
            ("Response", "SOAR playbooks in PulseFlow"),
            ("Standards", "ISO 27001, NIST CSF, CIS"),
            ("Residency", "LK, EU, or customer-held keys"),
            ("MDR", "Optional 24/7 Pulse SOC"),
        ],
    },
    {
        "slug": "pulseinsight",
        "name": "PulseInsight",
        "tag": "Predictive Analytics",
        "kicker": "Analytics",
        "lead": "See around corners. PulseInsight turns noise into a single, calm narrative for the business.",
        "summary": "PulseInsight is the analytics layer for leaders: governed metrics, forecasts, and natural-language briefings that land before the meeting starts.",
        "image": "product-insight.png",
        "color": "#ff9f0a",
        "features": [
            ("Metric tree", "One definition of revenue, risk, and service."),
            ("Forecasts", "Probabilistic outlooks, not a single heroic number."),
            ("Ask in language", "Sinhala, Tamil, or English — charts included."),
            ("Board mode", "Print-ready stories, not screenshots."),
            ("Alerts that matter", "Fewer pings. Higher signal."),
            ("Embedded", "Drop live insight into any product."),
        ],
        "specs": [
            ("Sources", "Warehouses, lakes, SaaS, files"),
            ("Latency", "Interactive to real-time"),
            ("Modeling", "Pulse + your data science notebooks"),
            ("Governance", "Lineage and certified metrics"),
            ("Export", "PDF, Sheets, API, PulseMind"),
        ],
    },
    {
        "slug": "pulseconnect",
        "name": "PulseConnect",
        "tag": "Enterprise Integrations",
        "kicker": "Integration",
        "lead": "Everything talks. Nothing breaks. PulseConnect is the quiet fabric between your systems.",
        "summary": "PulseConnect is an integration platform with AI mapping, retries that respect the business, and a catalog your architects will actually use.",
        "image": "product-connect.png",
        "color": "#bf5af2",
        "features": [
            ("Connector catalog", "ERP, banks, telco, HR, and custom APIs."),
            ("AI mapping", "Suggests transforms. You approve."),
            ("Exactly once", "Idempotency as a default, not a hope."),
            ("Contract tests", "Breakages caught in staging."),
            ("Edge agents", "Reach systems that cannot come to the cloud."),
            ("Partner exchange", "Publish and consume with governance."),
        ],
        "specs": [
            ("Protocols", "REST, GraphQL, SFTP, ISO 20022, HL7"),
            ("Throughput", "Enterprise message volumes"),
            ("Mapping", "SQL, Python, and AI assist"),
            ("Ops", "Dead-letter, replay, tracing"),
            ("Marketplace", "Certified partner connectors"),
        ],
    },
]

SOLUTIONS = [
    {
        "slug": "enterprise",
        "name": "Enterprise AI",
        "tag": "For the whole company",
        "lead": "A governed AI layer for every function — without a thousand shadow tools.",
        "summary": "We help large organisations adopt AI with a platform, a playbook, and a partner that stays for the operating model — not just the pilot.",
        "challenges": ["Tool sprawl and unsanctioned models", "Unclear ROI beyond demos", "Data that cannot leave the building", "Skills concentrated in one team"],
        "approach": ["Platform first: PulseCloud + PulseMind", "Use-case factory with PulseFlow", "Security and risk with PulseSecure", "Leadership cadence with PulseInsight"],
        "outcomes": ["One approved copilot for all staff", "Measurable cycle-time reductions", "Board-ready risk reporting", "Reusable patterns across subsidiaries"],
        "products": ["pulsemind", "pulsecloud", "pulsesecure", "pulseinsight"],
        "story": {
            "org": "Meridian Holdings",
            "quote": "We stopped collecting AI experiments and started running an AI company.",
            "person": "Anjali Fernando, Group CIO",
        },
    },
    {
        "slug": "healthcare",
        "name": "Healthcare",
        "tag": "Clinical and operational intelligence",
        "lead": "Give clinicians time. Give operations a pulse. Keep patients at the centre.",
        "summary": "AI Pulse for healthcare supports hospitals, insurers, and life sciences with private, auditable AI — from documentation to claims to research ops.",
        "challenges": ["Documentation burden", "Fragmented records", "Claims leakage", "Strict privacy regimes"],
        "approach": ["Ambient notes with PulseMind", "Referral and bed-flow in PulseFlow", "Interoperability via PulseConnect", "Quality dashboards in PulseInsight"],
        "outcomes": ["Shorter documentation time", "Fewer handoff errors", "Cleaner claims", "Audit-ready trails"],
        "products": ["pulsemind", "pulseflow", "pulseconnect", "pulsesecure"],
        "story": {
            "org": "Helix Health Group",
            "quote": "The copilot feels like a careful colleague — never a loud one.",
            "person": "Dr. Nirmala Jayasuriya, Chief Medical Officer",
        },
    },
    {
        "slug": "finance",
        "name": "Financial Services",
        "tag": "Banking, insurance, capital markets",
        "lead": "Move at the speed of the market. Stay inside the lines.",
        "summary": "From KYC to treasury to service, AI Pulse brings intelligence to regulated institutions with explainability and control.",
        "challenges": ["Legacy cores", "Fraud that mutates weekly", "Customer wait times", "Model risk management"],
        "approach": ["Copilot for relationship managers", "Case automation in PulseFlow", "Fraud signals in PulseInsight", "Model firewall in PulseSecure"],
        "outcomes": ["Faster onboarding", "Lower false positives", "Consistent advice", "Examinable AI"],
        "products": ["pulsemind", "pulseinsight", "pulsesecure", "pulseconnect"],
        "story": {
            "org": "Northshore Bank",
            "quote": "Our examiners asked for the lineage. We opened PulseInsight and walked the room through it.",
            "person": "Rohan de Silva, Head of Digital Risk",
        },
    },
    {
        "slug": "retail",
        "name": "Retail & Commerce",
        "tag": "Stores, marketplaces, supply",
        "lead": "A calmer kind of commerce. Demand, service, and stock — in one breath.",
        "summary": "Retailers use AI Pulse to personalise without being invasive, forecast without drama, and serve across store and screen.",
        "challenges": ["Thin margins", "Disconnected channels", "Seasonal shocks", "Service after the sale"],
        "approach": ["Demand sensing in PulseInsight", "Promotions in PulseFlow", "Service copilot in PulseMind", "Partner data via PulseConnect"],
        "outcomes": ["Fewer stockouts", "Higher attachment", "Shorter support time", "Clearer weekly rhythms"],
        "products": ["pulseinsight", "pulseflow", "pulsemind", "pulseconnect"],
        "story": {
            "org": "Apex Retail",
            "quote": "We finally plan the week with one number everyone trusts.",
            "person": "Meera Shah, Chief Commercial Officer",
        },
    },
    {
        "slug": "government",
        "name": "Public Sector",
        "tag": "Citizen services, at national scale",
        "lead": "Public service, privately held. Intelligence that respects the mandate.",
        "summary": "Ministries and agencies use AI Pulse for service design, document-heavy processes, and insight — with residency and accountability built in.",
        "challenges": ["Paper-heavy journeys", "Language inclusion", "Vendor lock-in", "Public trust"],
        "approach": ["Sinhala/Tamil copilots", "Casework in PulseFlow", "Sovereign options on PulseCloud", "Transparency reports via PulseInsight"],
        "outcomes": ["Shorter queues", "Inclusive language", "Local control of data", "Measurable service levels"],
        "products": ["pulsemind", "pulsecloud", "pulseflow", "pulsesecure"],
        "story": {
            "org": "CivicCloud Programme",
            "quote": "Residency was non-negotiable. PulseCloud made it feel ordinary.",
            "person": "Ishara Perera, Programme Director",
        },
    },
    {
        "slug": "education",
        "name": "Education",
        "tag": "Universities, schools, skills",
        "lead": "More teaching. Less administration. Learning with a human pulse.",
        "summary": "Education institutions use AI Pulse to support faculty, personalise practice, and run campuses without adding another silo.",
        "challenges": ["Faculty load", "Uneven access", "Admin sprawl", "Academic integrity"],
        "approach": ["Teaching assistant in PulseMind", "Enrolment flows in PulseFlow", "Learning signals in PulseInsight", "Integrity tools in PulseSecure"],
        "outcomes": ["Time back to teaching", "Earlier student support", "Cleaner operations", "Clear integrity policy"],
        "products": ["pulsemind", "pulseinsight", "pulseflow", "pulsesecure"],
        "story": {
            "org": "Lumen University",
            "quote": "Students get a tutor. Faculty get an afternoon back.",
            "person": "Prof. Kavindi Ranasinghe, Deputy Vice-Chancellor",
        },
    },
]

CUSTOMERS = [
    ("Meridian Holdings", "Conglomerate"),
    ("Helix Health Group", "Healthcare"),
    ("Northshore Bank", "Financial services"),
    ("Apex Retail", "Retail"),
    ("CivicCloud", "Public sector"),
    ("Lumen University", "Education"),
    ("Harbor Logistics", "Supply chain"),
    ("Nimbus Telecom", "Telecommunications"),
]

TESTIMONIALS = [
    ("The interface disappeared. That is the highest compliment I can give software.", "Anjali Fernando", "Group CIO, Meridian Holdings"),
    ("PulseMind writes like our best analyst — and cites like our best auditor.", "Rohan de Silva", "Head of Digital Risk, Northshore Bank"),
    ("We asked for sovereignty. They delivered a product that still feels inevitable.", "Ishara Perera", "Programme Director, CivicCloud"),
    ("Our clinicians stopped negotiating with forms and started finishing rounds.", "Dr. Nirmala Jayasuriya", "CMO, Helix Health Group"),
]


def pfx(depth: int) -> str:
    return "../" * depth


def absurl(path: str) -> str:
    path = path.lstrip("/")
    if path in ("", "index.html"):
        return SITE + "/"
    return f"{SITE}/{path}"


ICON_SEARCH = """<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><circle cx="6.5" cy="6.5" r="5.2" stroke="currentColor" stroke-width="1.3"/><path d="M10.4 10.4L14.2 14.2" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>"""
ICON_MENU = """<svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M2.5 4.5h11M2.5 8h11M2.5 11.5h11" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>"""


def nav(depth: int, active: str) -> str:
    pre = pfx(depth)
    links = [
        ("products", "Products", f"{pre}products/index.html"),
        ("solutions", "Solutions", f"{pre}solutions/index.html"),
        ("features", "Features", f"{pre}features.html"),
        ("customers", "Customers", f"{pre}customers.html"),
        ("about", "About", f"{pre}about.html"),
        ("contact", "Contact", f"{pre}contact.html"),
    ]
    items = "".join(
        f'<a class="nav-link{" is-active" if key == active else ""}" href="{href}">{label}</a>'
        for key, label, href in links
    )
    mobile = "".join(
        f'<a href="{href}">{label}</a>' for _, label, href in links
    ) + f'<a href="{pre}branding.html">Brand</a><a href="{pre}sitemap.html">Sitemap</a>'
    return f'''<header class="site-header">
  <a class="skip-link" href="#main">Skip to content</a>
  <nav class="site-nav" data-nav aria-label="Global">
    <div class="nav-inner">
      <a class="brand" href="{pre}index.html" aria-label="AI Pulse home">
        <svg viewBox="0 0 48 48" width="22" height="22" aria-hidden="true"><circle cx="24" cy="24" r="22" stroke="currentColor" stroke-width="1.2" fill="none"/><path d="M7.5 24h7.2l2.6-7.4 2.8 14.8L23.2 8.5 27.4 33l2.4-9h8.7" stroke="#333333" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/><circle cx="23.2" cy="8.5" r="2.1" fill="#333333"/></svg>
        <span class="brand-word">AI Pulse</span>
      </a>
      <div class="nav-links">{items}</div>
      <div class="nav-actions">
        <button class="nav-icon" type="button" data-search aria-label="Search"> {ICON_SEARCH} </button>
        <button class="nav-icon menu-btn" type="button" data-menu aria-label="Menu" aria-expanded="false"> {ICON_MENU} </button>
      </div>
    </div>
  </nav>
</header>
<div class="mobile-panel" data-panel>{mobile}</div>
<div class="search-overlay" data-search-overlay aria-hidden="true">
  <div class="search-box" role="dialog" aria-label="Search AI Pulse">
    <input data-search-input type="search" placeholder="Search AI Pulse" autocomplete="off">
    <div class="search-hits" data-search-hits></div>
    <p class="muted" style="font-size:12px;padding:8px 4px 12px">Press Esc to close. ⌘K to open.</p>
    <button class="link-more" type="button" data-close-search>Close</button>
  </div>
</div>'''


def footer(depth: int) -> str:
    pre = pfx(depth)
    cols = [
        ("Shop and explore", [("Products", f"{pre}products/index.html"), ("PulseMind", f"{pre}products/pulsemind.html"), ("PulseFlow", f"{pre}products/pulseflow.html"), ("PulseCloud", f"{pre}products/pulsecloud.html"), ("PulseSecure", f"{pre}products/pulsesecure.html")]),
        ("Solutions", [("Enterprise AI", f"{pre}solutions/enterprise.html"), ("Healthcare", f"{pre}solutions/healthcare.html"), ("Financial Services", f"{pre}solutions/finance.html"), ("Retail", f"{pre}solutions/retail.html"), ("Public Sector", f"{pre}solutions/government.html"), ("Education", f"{pre}solutions/education.html")]),
        ("Company", [("About", f"{pre}about.html"), ("Customers", f"{pre}customers.html"), ("Features", f"{pre}features.html"), ("Brand", f"{pre}branding.html"), ("Contact", f"{pre}contact.html")]),
        ("Values", [("Privacy", f"{pre}privacy.html"), ("Terms", f"{pre}terms.html"), ("Sitemap", f"{pre}sitemap.html")]),
        ("Account", [("Talk to sales", f"{pre}contact.html"), ("Support", f"{pre}contact.html"), ("Partners", f"{pre}contact.html")]),
    ]
    col_html = ""
    for title, links in cols:
        lis = "".join(f'<li><a href="{h}">{t}</a></li>' for t, h in links)
        col_html += f'<div class="footer-col" data-accordion><h3>{title}</h3><ul>{lis}</ul></div>'
    return f'''<footer class="site-footer">
  <div class="footer-wrap">
    <p class="footer-note">More ways to explore: <a href="{pre}products/index.html">view products</a>, <a href="{pre}solutions/index.html">browse solutions</a>, or <a href="{pre}contact.html">talk with AI Pulse</a>. Mock content for demonstration.</p>
    <div class="footer-cols">{col_html}</div>
    <div class="footer-bottom">
      <p>Copyright © <span data-year>2026</span> AI Pulse (Pvt) Ltd. All rights reserved.</p>
      <div class="footer-legal">
        <a href="{pre}privacy.html">Privacy Policy</a>
        <a href="{pre}terms.html">Terms of Use</a>
        <a href="{pre}sitemap.html">Sitemap</a>
        <a href="{pre}branding.html">Brand</a>
        <span>Sri Lanka</span>
      </div>
    </div>
  </div>
</footer>'''


def head(*, title: str, description: str, path: str, depth: int, keywords: str, image: str = "og-image.png", schemas: list):
    pre = pfx(depth)
    canonical = absurl(path)
    og = absurl(f"assets/{image}")
    schema_tags = "\n".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas
    )
    return f'''<!DOCTYPE html>
<html lang="en-LK">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="{keywords}">
  <meta name="author" content="AI Pulse (Pvt) Ltd">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="theme-color" content="#F5F5F5">
  <meta name="color-scheme" content="light">
  <meta name="application-name" content="AI Pulse">
  <meta name="apple-mobile-web-app-title" content="AI Pulse">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="format-detection" content="telephone=no">
  <meta name="geo.region" content="LK-11">
  <meta name="geo.placename" content="Colombo">
  <meta name="geo.position" content="6.9271;79.8612">
  <meta name="ICBM" content="6.9271, 79.8612">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" href="{canonical}" hreflang="en-LK">
  <link rel="alternate" href="{canonical}" hreflang="en">
  <link rel="alternate" href="{canonical}" hreflang="x-default">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="AI Pulse">
  <meta property="og:locale" content="en_LK">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og}">
  <meta property="og:image:width" content="1376">
  <meta property="og:image:height" content="768">
  <meta property="og:image:alt" content="AI Pulse — intelligence with a pulse">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{og}">
  <link rel="icon" href="{pre}assets/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="{pre}assets/logo-mark.png">
  <link rel="manifest" href="{pre}site.webmanifest">
  <link rel="sitemap" type="application/xml" href="{pre}sitemap.xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>tailwind.config={{theme:{{extend:{{colors:{{ink:'#333333',mist:'#666666',snow:'#f5f5f5',ash:{{0:'#000000',20:'#333333',40:'#666666',60:'#999999',80:'#cccccc',100:'#ffffff'}},pulse:{{blue:'#333333',glow:'#333333'}}}}}}}}}}</script>
  <link rel="stylesheet" href="{pre}css/style.css">
  {schema_tags}
</head>'''


ORG = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "AI Pulse",
    "legalName": "AI Pulse (Pvt) Ltd",
    "url": SITE,
    "logo": absurl("assets/logo.svg"),
    "image": absurl("assets/og-image.png"),
    "description": "AI Pulse builds enterprise software for copilots, automation, cloud AI, security, analytics, and integration.",
    "foundingDate": "2019",
    "email": "hello@aipulse.lk",
    "telephone": "+94-11-234-5678",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Level 12, World Trade Center, Echelon Square",
        "addressLocality": "Colombo",
        "postalCode": "00100",
        "addressCountry": "LK",
    },
    "areaServed": ["LK", "South Asia", "Worldwide"],
    "sameAs": ["https://aipulse.lk"],
}


def webpage_schema(name, description, path, crumbs):
    return {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": name,
        "description": description,
        "url": absurl(path),
        "isPartOf": {"@type": "WebSite", "name": "AI Pulse", "url": SITE},
        "inLanguage": "en-LK",
        "breadcrumb": {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": c[0], "item": absurl(c[1])}
                for i, c in enumerate(crumbs)
            ],
        },
    }


def crumbs_html(depth, items):
    pre = pfx(depth)
    parts = []
    for i, (label, href) in enumerate(items):
        url = href if href.startswith("http") else pre + href
        if i == len(items) - 1:
            parts.append(f'<span aria-current="page">{label}</span>')
        else:
            parts.append(f'<a href="{url}">{label}</a> <span aria-hidden="true">/</span> ')
    return f'<nav class="crumbs wrap" aria-label="Breadcrumb">{"".join(parts)}</nav>'


def render(path, *, title, description, keywords, depth, active, crumbs, body, extra_schemas=None, image="og-image.png"):
    schemas = [ORG, webpage_schema(title, description, path, crumbs)]
    if extra_schemas:
        schemas.extend(extra_schemas)
    html = head(title=title, description=description, path=path, depth=depth, keywords=keywords, image=image, schemas=schemas)
    html += f'''
<body data-depth="{depth}">
{nav(depth, active)}
<main id="main">
{body}
</main>
{footer(depth)}
<script src="{pfx(depth)}js/main.js" defer></script>
</body>
</html>
'''
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print("wrote", path)


def product_by_slug(slug):
    return next(p for p in PRODUCTS if p["slug"] == slug)


# ---------- pages ----------

def home():
    tiles = ""
    pairs = [
        (PRODUCTS[0], "dark"),
        (PRODUCTS[1], "light"),
        (PRODUCTS[2], "dark"),
        (PRODUCTS[3], "light"),
        (PRODUCTS[4], "dark"),
        (PRODUCTS[5], "light"),
    ]
    for p, tone in pairs:
        cls = "tile ash" if tone == "light" else "tile"
        tiles += f'''
        <article class="{cls} reveal">
          <p class="eyebrow">{p["kicker"]}</p>
          <h3 class="display-sm" style="font-size:clamp(28px,4vw,44px)">{p["name"]}</h3>
          <p class="subhead mt-3 max-w-md">{p["tag"]}. {p["lead"].split(".")[0]}.</p>
          <p class="mt-5 flex gap-6 justify-center"><a class="link-more" href="products/{p["slug"]}.html">Learn more</a><a class="link-more" href="contact.html">Talk to sales</a></p>
          <img src="assets/{p["image"]}" alt="{p["name"]} product visual" width="1200" height="900">
        </article>'''
    logos = "".join(f'<span class="customer-logo">{n}</span>' for n, _ in CUSTOMERS) * 2
    quotes = ""
    for i, (q, person, role) in enumerate(TESTIMONIALS):
        quotes += f'''<blockquote class="glass quote-card reveal d{i+1}">
          <p class="text-[21px] leading-snug tracking-tight">“{q}”</p>
          <footer class="mt-6 text-sm muted">{person}<br>{role}</footer>
        </blockquote>'''
    sols = ""
    for s in SOLUTIONS:
        sols += f'''<a class="glass feature-card reveal" href="solutions/{s["slug"]}.html">
          <p class="eyebrow">{s["tag"]}</p>
          <h3 class="text-[28px] font-semibold tracking-tight mt-3">{s["name"]}</h3>
          <p class="muted mt-2">{s["lead"]}</p>
          <span class="link-more mt-6">Explore</span>
        </a>'''
    body = f'''
    <div class="ribbon section-ash">PulseMind 2 is here. Grounded, private, and fluent in Sinhala, Tamil, and English. <a href="products/pulsemind.html">Learn more</a></div>
    <section class="hero section-white">
      <div class="hero-copy">
        <p class="eyebrow">AI Pulse</p>
        <h1 class="display mt-3">Intelligence<br>with a pulse.</h1>
        <svg class="pulse-svg mx-auto mt-6" width="240" height="48" viewBox="0 0 240 48" aria-hidden="true">
          <path class="pulse-path" d="M8 24h52l10-14 8 28 12-32 10 24 8-6h124" fill="none" stroke="#333333" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
          <circle class="node-pulse" cx="90" cy="6" r="3" fill="#333333"/>
        </svg>
        <p class="subhead mt-5 max-w-2xl mx-auto">Enterprise software that feels inevitable. Copilots, automation, cloud, security, insight, and integration — designed as one system.</p>
        <p class="mt-8 flex flex-wrap gap-4 justify-center">
          <a class="btn-apple" href="products/index.html">Explore products</a>
          <a class="btn-ghost" href="contact.html">Talk to sales</a>
        </p>
      </div>
      <div class="hero-visual hero-copy d2">
        <img src="assets/hero-product.png" alt="AI Pulse platform on a glass surface with a luminous pulse waveform" width="1600" height="900" fetchpriority="high">
      </div>
    </section>
    <section class="section-tight section-ash">
      <div class="wrap grid-2">{tiles}</div>
    </section>
    <section class="section section-white">
      <div class="wrap center">
        <p class="eyebrow reveal">Solutions</p>
        <h2 class="display-sm reveal d1 mt-3">Built for the work<br>that cannot wait.</h2>
        <p class="subhead reveal d2 mt-4 max-w-2xl mx-auto">Industry systems with the same restraint you expect from consumer design — and the controls an enterprise actually needs.</p>
      </div>
      <div class="wrap grid-3 mt-14">{sols}</div>
    </section>
    <section class="section section-ash center">
      <div class="wrap">
        <p class="eyebrow reveal">Customers</p>
        <h2 class="display-sm reveal d1 mt-3">Trusted in rooms<br>where trust is the product.</h2>
      </div>
      <div class="marquee mt-12 reveal d2">
        <div class="marquee-track">{logos}</div>
      </div>
      <p class="mt-10"><a class="link-more" href="customers.html">See customer stories</a></p>
    </section>
    <section class="section section-white">
      <div class="wrap center mb-12">
        <p class="eyebrow reveal">Voices</p>
        <h2 class="display-sm reveal d1 mt-3">Quiet software.<br>Loud results.</h2>
      </div>
      <div class="wrap grid-2">{quotes}</div>
    </section>
    <section class="section section-ash center">
      <div class="wrap-narrow">
        <h2 class="display-sm reveal">Ready when you are.</h2>
        <p class="subhead reveal d1 mt-4">A conversation. A workspace. A platform that already knows how to stay out of the way.</p>
        <p class="mt-8 reveal d2 flex flex-wrap gap-4 justify-center">
          <a class="btn-apple" href="contact.html">Contact AI Pulse</a>
          <a class="btn-ghost" href="about.html">Our story</a>
        </p>
      </div>
    </section>'''
    render(
        "index.html",
        title="AI Pulse — Intelligence with a pulse | aipulse.lk",
        description="AI Pulse is a Sri Lanka software company building enterprise AI products: PulseMind, PulseFlow, PulseCloud, PulseSecure, PulseInsight, and PulseConnect.",
        keywords="AI Pulse, aipulse.lk, enterprise AI Sri Lanka, copilot, automation, AI cloud, Colombo software",
        depth=0,
        active="home",
        crumbs=[("Home", "")],
        image="hero-product.png",
        extra_schemas=[{
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": "AI Pulse",
            "url": SITE,
            "potentialAction": {
                "@type": "SearchAction",
                "target": f"{SITE}/sitemap.html?q={{search_term_string}}",
                "query-input": "required name=search_term_string",
            },
        }, {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": "What does AI Pulse build?", "acceptedAnswer": {"@type": "Answer", "text": "Enterprise software for copilots, automation, AI cloud, security, analytics, and integration."}},
                {"@type": "Question", "name": "Where is AI Pulse based?", "acceptedAnswer": {"@type": "Answer", "text": "Colombo, Sri Lanka, with delivery across South Asia and globally."}},
            ],
        }],
        body=body,
    )


def products_index():
    cards = ""
    for p in PRODUCTS:
        cards += f'''<a class="tile reveal" href="{p["slug"]}.html">
          <p class="eyebrow">{p["kicker"]}</p>
          <h2 class="display-sm" style="font-size:clamp(28px,4vw,40px)">{p["name"]}</h2>
          <p class="subhead mt-3 max-w-sm">{p["tag"]}</p>
          <span class="link-more mt-5">Learn more</span>
          <img src="../assets/{p["image"]}" alt="{p["name"]}" width="800" height="600">
        </a>'''
    body = f'''
    {crumbs_html(1, [("Home", "index.html"), ("Products", "products/index.html")])}
    <section class="hero" style="min-height:auto;padding-bottom:24px">
      <h1 class="display hero-copy">The lineup.</h1>
      <p class="subhead hero-copy d mt-4 max-w-2xl mx-auto">Six products. One pulse. Each can stand alone. Together they feel like a single instrument.</p>
    </section>
    <div class="hero-visual mx-auto mb-10 px-6"><img src="../assets/products-hero.png" alt="AI Pulse product family" width="1600" height="900" class="rounded-[28px]"></div>
    <section class="section-tight"><div class="wrap grid-2">{cards}</div></section>'''
    render(
        "products/index.html",
        title="Products — AI Pulse | Copilot, automation, cloud, security",
        description="Explore AI Pulse products: PulseMind, PulseFlow, PulseCloud, PulseSecure, PulseInsight, and PulseConnect.",
        keywords="AI Pulse products, PulseMind, PulseFlow, PulseCloud, PulseSecure, PulseInsight, PulseConnect",
        depth=1,
        active="products",
        crumbs=[("Home", ""), ("Products", "products/")],
        image="products-hero.png",
        extra_schemas=[{
            "@context": "https://schema.org",
            "@type": "ItemList",
            "name": "AI Pulse products",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": absurl(f"products/{p['slug']}.html"), "name": p["name"]} for i, p in enumerate(PRODUCTS)],
        }],
        body=body,
    )


def product_page(p):
    feats = "".join(
        f'<article class="glass feature-card reveal"><h3 class="text-[21px] font-semibold tracking-tight">{t}</h3><p class="muted mt-2">{d}</p></article>'
        for t, d in p["features"]
    )
    specs = "".join(f'<div class="spec-row"><div class="muted">{k}</div><div>{v}</div></div>' for k, v in p["specs"])
    related = "".join(
        f'<a class="glass feature-card reveal" href="{o["slug"]}.html"><p class="eyebrow">{o["kicker"]}</p><h3 class="text-[22px] font-semibold mt-2">{o["name"]}</h3><span class="link-more mt-4">Learn more</span></a>'
        for o in PRODUCTS if o["slug"] != p["slug"]
    )[:1]
    related = "".join(
        f'<a class="glass feature-card reveal" href="{o["slug"]}.html"><p class="eyebrow">{o["kicker"]}</p><h3 class="text-[22px] font-semibold mt-2">{o["name"]}</h3><p class="muted mt-2">{o["tag"]}</p><span class="link-more mt-4">Learn more</span></a>'
        for o in PRODUCTS if o["slug"] != p["slug"]
    )
    body = f'''
    {crumbs_html(1, [("Home", "index.html"), ("Products", "products/index.html"), (p["name"], "products/" + p["slug"] + ".html")])}
    <section class="hero" style="min-height:auto">
      <p class="eyebrow hero-copy">{p["kicker"]}</p>
      <h1 class="display hero-copy d">{p["name"]}</h1>
      <p class="subhead hero-copy d2 mt-4 max-w-2xl mx-auto">{p["lead"]}</p>
      <p class="mt-8 flex flex-wrap gap-6 justify-center hero-copy d2">
        <a class="link-more" href="#overview">Learn more</a>
        <a class="link-more" href="../contact.html">Talk to sales</a>
      </p>
      <div class="hero-visual"><img src="../assets/{p["image"]}" alt="{p["name"]} visual" width="1200" height="900"></div>
    </section>
    <section id="overview" class="section section-light">
      <div class="wrap-narrow center">
        <h2 class="display-sm">Designed to disappear<br>into the work.</h2>
        <p class="subhead mt-4">{p["summary"]}</p>
      </div>
      <div class="wrap grid-3 mt-14">{feats}</div>
    </section>
    <section class="section">
      <div class="wrap grid md:grid-cols-2 gap-12 items-center">
        <div>
          <h2 class="display-sm">The details,<br>kept honest.</h2>
          <div class="mt-8">{specs}</div>
        </div>
        <div class="glass p-4">
          <img src="../assets/{p["image"]}" alt="" class="rounded-2xl" width="800" height="600">
        </div>
      </div>
    </section>
    <section class="section section-ink">
      <div class="wrap">
        <h2 class="display-sm">Also in the family.</h2>
        <div class="grid-3 mt-10">{related}</div>
      </div>
    </section>
    <section class="section section-light center">
      <h2 class="display-sm">Bring {p["name"]} in.</h2>
      <p class="mt-8 flex gap-4 justify-center"><a class="btn-apple" href="../contact.html">Contact sales</a><a class="btn-ghost" href="index.html">All products</a></p>
    </section>'''
    render(
        f"products/{p['slug']}.html",
        title=f"{p['name']} — {p['tag']} | AI Pulse",
        description=p["summary"][:158],
        keywords=f"{p['name']}, {p['tag']}, AI Pulse, aipulse.lk, enterprise software Sri Lanka",
        depth=1,
        active="products",
        crumbs=[("Home", ""), ("Products", "products/"), (p["name"], f"products/{p['slug']}.html")],
        image=p["image"],
        extra_schemas=[{
            "@context": "https://schema.org",
            "@type": "SoftwareApplication",
            "name": p["name"],
            "applicationCategory": "BusinessApplication",
            "operatingSystem": "Web",
            "description": p["summary"],
            "url": absurl(f"products/{p['slug']}.html"),
            "image": absurl(f"assets/{p['image']}"),
            "brand": {"@type": "Brand", "name": "AI Pulse"},
            "offers": {"@type": "Offer", "availability": "https://schema.org/OnlineOnly", "priceCurrency": "USD", "price": "0", "description": "Contact sales for pricing"},
        }],
        body=body,
    )


def solutions_index():
    cards = ""
    for s in SOLUTIONS:
        cards += f'''<a class="glass feature-card reveal" href="{s["slug"]}.html">
          <p class="eyebrow">{s["tag"]}</p>
          <h2 class="text-[32px] font-semibold tracking-tight mt-3">{s["name"]}</h2>
          <p class="muted mt-3">{s["lead"]}</p>
          <span class="link-more mt-6">Explore</span>
        </a>'''
    body = f'''
    {crumbs_html(1, [("Home", "index.html"), ("Solutions", "solutions/index.html")])}
    <section class="hero" style="min-height:auto;padding-bottom:48px">
      <h1 class="display">Solutions.</h1>
      <p class="subhead mt-4 max-w-2xl mx-auto">The same design language. Different stakes. Industry systems with a consumer-grade calm.</p>
    </section>
    <section class="section-tight"><div class="wrap grid-2">{cards}</div></section>'''
    render(
        "solutions/index.html",
        title="Solutions — Enterprise, healthcare, finance, retail | AI Pulse",
        description="AI Pulse industry solutions for enterprise, healthcare, financial services, retail, public sector, and education.",
        keywords="AI Pulse solutions, enterprise AI, healthcare AI, fintech AI Sri Lanka",
        depth=1,
        active="solutions",
        crumbs=[("Home", ""), ("Solutions", "solutions/")],
        body=body,
    )


def solution_page(s):
    def lis(items):
        return "".join(f'<li class="py-2 border-b border-white/10">{i}</li>' for i in items)

    prods = ""
    for slug in s["products"]:
        p = product_by_slug(slug)
        prods += f'<a class="glass feature-card" href="../products/{p["slug"]}.html"><p class="eyebrow">{p["kicker"]}</p><h3 class="text-[22px] font-semibold mt-2">{p["name"]}</h3><span class="link-more mt-4">Learn more</span></a>'
    body = f'''
    {crumbs_html(1, [("Home", "index.html"), ("Solutions", "solutions/index.html"), (s["name"], "solutions/" + s["slug"] + ".html")])}
    <section class="hero" style="min-height:auto">
      <p class="eyebrow">{s["tag"]}</p>
      <h1 class="display">{s["name"]}</h1>
      <p class="subhead mt-4 max-w-2xl mx-auto">{s["lead"]}</p>
      <p class="mt-8"><a class="btn-apple" href="../contact.html">Talk to an industry lead</a></p>
    </section>
    <section class="section section-light">
      <div class="wrap-narrow"><h2 class="display-sm">The brief.</h2><p class="subhead mt-4">{s["summary"]}</p></div>
      <div class="wrap grid md:grid-cols-3 gap-8 mt-16">
        <div class="reveal"><h3 class="text-lg font-semibold mb-4">Challenges</h3><ul>{lis(s["challenges"])}</ul></div>
        <div class="reveal d1"><h3 class="text-lg font-semibold mb-4">Approach</h3><ul>{lis(s["approach"])}</ul></div>
        <div class="reveal d2"><h3 class="text-lg font-semibold mb-4">Outcomes</h3><ul>{lis(s["outcomes"])}</ul></div>
      </div>
    </section>
    <section class="section">
      <div class="wrap glass p-10 md:p-16">
        <p class="eyebrow">Customer story</p>
        <blockquote class="display-sm mt-6" style="font-size:clamp(24px,4vw,40px)">“{s["story"]["quote"]}”</blockquote>
        <p class="muted mt-6">{s["story"]["person"]} · {s["story"]["org"]}</p>
      </div>
    </section>
    <section class="section section-ink">
      <div class="wrap"><h2 class="display-sm">The stack.</h2><div class="grid-2 mt-10">{prods}</div></div>
    </section>'''
    # fix light section list borders
    body = body.replace("border-white/10", "border-black/10")
    render(
        f"solutions/{s['slug']}.html",
        title=f"{s['name']} solutions — AI Pulse",
        description=s["summary"][:158],
        keywords=f"{s['name']}, AI Pulse solutions, {s['tag']}, aipulse.lk",
        depth=1,
        active="solutions",
        crumbs=[("Home", ""), ("Solutions", "solutions/"), (s["name"], f"solutions/{s['slug']}.html")],
        extra_schemas=[{
            "@context": "https://schema.org",
            "@type": "Service",
            "name": f"AI Pulse for {s['name']}",
            "provider": {"@type": "Organization", "name": "AI Pulse"},
            "description": s["summary"],
            "areaServed": "LK",
            "url": absurl(f"solutions/{s['slug']}.html"),
        }],
        body=body,
    )


def features_page():
    items = [
        ("One design language", "Every product shares type, motion, and glass. Teams learn once."),
        ("Grounding", "Answers cite approved sources. No improvisation on policy."),
        ("Residency", "Colombo region, private cloud, or keys you hold."),
        ("Human checkpoints", "Automation that knows when to pause."),
        ("Observability", "Traces, evals, and cost in the same cockpit."),
        ("Language", "Sinhala, Tamil, and English as first-class citizens."),
        ("Accessibility", "Contrast, motion, and keyboard as defaults."),
        ("Open edges", "APIs, webhooks, and exports. No ornamental lock-in."),
        ("Security fabric", "Identity, data, and model risk on one timeline."),
        ("Quiet notifications", "Fewer pings. Higher signal."),
        ("Partner ready", "Certified connectors and a governed marketplace."),
        ("Support that stays", "Named humans in your timezone."),
    ]
    cards = "".join(
        f'<article class="glass feature-card reveal"><h3 class="text-[21px] font-semibold tracking-tight">{t}</h3><p class="muted mt-2">{d}</p></article>'
        for t, d in items
    )
    body = f'''
    {crumbs_html(0, [("Home", "index.html"), ("Features", "features.html")])}
    <section class="hero" style="min-height:auto;padding-bottom:20px">
      <h1 class="display">Features.</h1>
      <p class="subhead mt-4 max-w-2xl mx-auto">The system underneath the products. Restraint as a feature.</p>
    </section>
    <section class="section-tight"><div class="wrap grid-3">{cards}</div></section>
    <section class="section section-light center">
      <h2 class="display-sm">See them in a product.</h2>
      <p class="mt-8"><a class="btn-apple" href="products/index.html">Browse the lineup</a></p>
    </section>'''
    render("features.html", title="Features — AI Pulse platform capabilities", description="Platform features of AI Pulse: grounding, residency, observability, multilingual support, security, and human-in-the-loop automation.", keywords="AI Pulse features, enterprise AI platform, data residency Sri Lanka", depth=0, active="features", crumbs=[("Home", ""), ("Features", "features.html")], body=body)


def customers_page():
    cards = ""
    for name, sector in CUSTOMERS:
        cards += f'<article class="glass feature-card reveal"><p class="eyebrow">{sector}</p><h3 class="text-[28px] font-semibold tracking-tight mt-3">{name}</h3><p class="muted mt-2">Mock customer used to demonstrate the AI Pulse experience.</p></article>'
    quotes = "".join(
        f'<blockquote class="glass quote-card reveal"><p class="text-[22px] tracking-tight">“{q}”</p><footer class="muted mt-5 text-sm">{p}<br>{r}</footer></blockquote>'
        for q, p, r in TESTIMONIALS
    )
    body = f'''
    {crumbs_html(0, [("Home", "index.html"), ("Customers", "customers.html")])}
    <section class="hero" style="min-height:auto">
      <h1 class="display">Customers.</h1>
      <p class="subhead mt-4">Institutions that prefer their software quiet.</p>
    </section>
    <section class="section-tight"><div class="wrap grid-2">{cards}</div></section>
    <section class="section section-ink"><div class="wrap grid-2">{quotes}</div></section>'''
    render("customers.html", title="Customers & stories — AI Pulse", description="Customer stories and testimonials for AI Pulse, including healthcare, banking, retail, public sector, and education.", keywords="AI Pulse customers, testimonials, case studies Sri Lanka", depth=0, active="customers", crumbs=[("Home", ""), ("Customers", "customers.html")], extra_schemas=[{
        "@context": "https://schema.org",
        "@type": "Review",
        "itemReviewed": {"@type": "Organization", "name": "AI Pulse"},
        "reviewBody": TESTIMONIALS[0][0],
        "author": {"@type": "Person", "name": TESTIMONIALS[0][1]},
        "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
    }], body=body)


def about_page():
    body = f'''
    {crumbs_html(0, [("Home", "index.html"), ("About", "about.html")])}
    <section class="hero" style="min-height:auto">
      <h1 class="display">About AI Pulse.</h1>
      <p class="subhead mt-4 max-w-2xl mx-auto">A software company in Colombo, building enterprise intelligence with the calm of a consumer product.</p>
    </section>
    <div class="wrap mb-8"><img src="assets/about-hero.png" alt="AI Pulse studio atmosphere" class="rounded-[28px]" width="1600" height="900"></div>
    <section class="section section-light">
      <div class="wrap grid md:grid-cols-2 gap-16">
        <div>
          <h2 class="display-sm">The idea.</h2>
          <p class="mt-5 text-[19px] leading-relaxed">Most enterprise software announces itself. We wanted the opposite: tools that feel as considered as a phone you already know, with the gravity a bank or a hospital actually needs.</p>
          <p class="mt-4 muted">Founded in 2019. 180 people. Design, research, and engineering in the same rooms.</p>
        </div>
        <div>
          <h2 class="display-sm">The craft.</h2>
          <p class="mt-5 text-[19px] leading-relaxed">We ship slowly enough to stay precise. Glass, type, and motion are not decoration — they are how trust shows up on a screen.</p>
          <p class="mt-4"><a class="link-more" href="branding.html">See the brand</a></p>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="wrap grid-3">
        <article class="glass feature-card"><h3 class="text-4xl font-semibold">2019</h3><p class="muted mt-2">Founded in Colombo</p></article>
        <article class="glass feature-card"><h3 class="text-4xl font-semibold">180+</h3><p class="muted mt-2">People across product teams</p></article>
        <article class="glass feature-card"><h3 class="text-4xl font-semibold">6</h3><p class="muted mt-2">Products. One pulse.</p></article>
      </div>
    </section>'''
    render("about.html", title="About AI Pulse — Colombo software company", description="AI Pulse is a Colombo-based software company founded in 2019, building enterprise AI products with a minimal, Apple-like design language.", keywords="about AI Pulse, Colombo software company, aipulse.lk", depth=0, active="about", crumbs=[("Home", ""), ("About", "about.html")], image="about-hero.png", extra_schemas=[{
        "@context": "https://schema.org",
        "@type": "AboutPage",
        "url": absurl("about.html"),
        "name": "About AI Pulse",
    }], body=body)


def contact_page():
    body = f'''
    {crumbs_html(0, [("Home", "index.html"), ("Contact", "contact.html")])}
    <section class="hero" style="min-height:auto;padding-bottom:12px">
      <h1 class="display">Contact.</h1>
      <p class="subhead mt-4">A short note. A precise reply.</p>
    </section>
    <section class="section-tight">
      <div class="wrap grid md:grid-cols-2 gap-10">
        <form class="glass p-8 form-grid" data-contact-form novalidate>
          <div class="form-success" data-form-success>Thank you. A human at AI Pulse will reply within one business day.</div>
          <div class="form-grid two">
            <label class="field"><span>Name</span><input name="name" required autocomplete="name"></label>
            <label class="field"><span>Email</span><input name="email" type="email" required autocomplete="email"></label>
          </div>
          <div class="form-grid two">
            <label class="field"><span>Company</span><input name="company" autocomplete="organization"></label>
            <label class="field"><span>Interest</span>
              <select name="interest">
                <option>PulseMind</option><option>PulseFlow</option><option>PulseCloud</option>
                <option>PulseSecure</option><option>PulseInsight</option><option>PulseConnect</option>
                <option>Solutions</option><option>Partnerships</option>
              </select>
            </label>
          </div>
          <label class="field"><span>Message</span><textarea name="message" rows="5" required></textarea></label>
          <button class="btn-apple" type="submit">Send</button>
        </form>
        <aside class="glass p-8">
          <h2 class="text-[28px] font-semibold tracking-tight">Visit</h2>
          <p class="muted mt-3">Level 12, World Trade Center<br>Echelon Square, Colombo 01<br>Sri Lanka</p>
          <p class="mt-6"><a class="link-more" href="mailto:hello@aipulse.lk">hello@aipulse.lk</a></p>
          <p class="mt-2"><a class="link-more" href="tel:+94112345678">+94 11 234 5678</a></p>
          <p class="muted mt-8 text-sm">Weekdays 09:00–18:00 IST. Mock contact details for this demonstration site.</p>
        </aside>
      </div>
    </section>'''
    render("contact.html", title="Contact AI Pulse — Colombo, Sri Lanka", description="Contact AI Pulse in Colombo. Talk to sales about PulseMind, PulseFlow, PulseCloud, and other enterprise AI products.", keywords="contact AI Pulse, aipulse.lk, Colombo AI company", depth=0, active="contact", crumbs=[("Home", ""), ("Contact", "contact.html")], extra_schemas=[{
        "@context": "https://schema.org",
        "@type": "ContactPage",
        "url": absurl("contact.html"),
        "name": "Contact AI Pulse",
    }], body=body)


def branding_page():
    swatches = [
        ("#FFFFFF", "White 1.0", "Primary surface"),
        ("#F5F5F5", "Ash 0.96", "Page wash"),
        ("#EBEBEB", "Ash 0.92", "Alt bands"),
        ("#CCCCCC", "Ash 0.8", "Lines"),
        ("#999999", "Ash 0.6", "Quiet text"),
        ("#666666", "Ash 0.4", "Secondary text"),
        ("#333333", "Ash 0.2", "Pulse, links"),
        ("#000000", "Black 0.0", "Headlines, buttons"),
    ]
    sw = "".join(
        f'<article class="glass overflow-hidden"><div class="swatch" style="background:{hexv}"></div><div class="p-4"><h3 class="font-semibold">{name}</h3><p class="muted text-sm">{hexv}<br>{use}</p></div></article>'
        for hexv, name, use in swatches
    )
    body = f'''
    {crumbs_html(0, [("Home", "index.html"), ("Brand", "branding.html")])}
    <section class="hero" style="min-height:auto">
      <h1 class="display">Brand.</h1>
      <p class="subhead mt-4 max-w-2xl mx-auto">The mark is a pulse with a mind. A single waveform, a node at the peak, a wordmark that stays quiet.</p>
    </section>
    <section class="section-tight">
      <div class="wrap grid md:grid-cols-2 gap-6">
        <figure class="brand-frame bg-black p-10 flex items-center justify-center min-h-[280px]">
          <img src="assets/logo-dark.png" alt="AI Pulse logo on black" class="max-h-40 w-auto mx-auto">
        </figure>
        <figure class="brand-frame bg-[#f5f5f7] p-10 flex items-center justify-center min-h-[280px]">
          <img src="assets/logo-light.png" alt="AI Pulse logo on light" class="max-h-40 w-auto mx-auto">
        </figure>
      </div>
      <div class="wrap grid md:grid-cols-3 gap-6 mt-6">
        <figure class="glass p-10 flex items-center justify-center"><img src="assets/logo-mark.png" alt="AI Pulse icon mark" class="w-40 h-40 object-contain"></figure>
        <figure class="glass p-10 flex items-center justify-center">
          <img src="assets/logo-on-light.svg" alt="AI Pulse SVG wordmark" class="w-64">
        </figure>
        <figure class="glass p-10 flex flex-col items-center justify-center gap-4">
          <img src="assets/logo-mark.svg" alt="AI Pulse SVG mark" class="w-20 h-20">
          <p class="muted text-sm">Clear space: one mark-width on all sides.</p>
        </figure>
      </div>
    </section>
    <section class="section section-light">
      <div class="wrap">
        <h2 class="display-sm">Colour.</h2>
        <div class="grid-3 mt-10">{sw}</div>
      </div>
    </section>
    <section class="section">
      <div class="wrap grid md:grid-cols-2 gap-12">
        <div>
          <h2 class="display-sm">Type.</h2>
          <p class="mt-6 text-5xl font-semibold tracking-tight">Inter / SF Pro</p>
          <p class="muted mt-3">System UI first. Inter as the web face. Tracking tight. Weight 400 and 600.</p>
        </div>
        <div>
          <h2 class="display-sm">Voice.</h2>
          <p class="mt-6 text-[21px] leading-relaxed">Short sentences. No slogans that shout. Prefer nouns you can ship. Never claim magic. Intelligence, with a pulse.</p>
        </div>
      </div>
    </section>
    <section class="section section-ink">
      <div class="wrap">
        <h2 class="display-sm">Please don’t.</h2>
        <div class="grid-3 mt-10">
          <article class="glass feature-card dont"><p>Don’t stretch the mark.</p></article>
          <article class="glass feature-card dont"><p>Don’t recolour the pulse away from ash 0.2.</p></article>
          <article class="glass feature-card dont"><p>Don’t add slogans inside the lockup.</p></article>
        </div>
        <p class="mt-10 flex flex-wrap gap-6">
          <a class="link-more" href="assets/logo.svg" download>Download SVG wordmark</a>
          <a class="link-more" href="assets/logo-on-light.svg" download>Download SVG (light)</a>
          <a class="link-more" href="assets/logo-mark.svg" download>Download SVG mark</a>
          <a class="link-more" href="assets/logo-dark.png" download>Download PNG (dark)</a>
        </p>
      </div>
    </section>'''
    render("branding.html", title="Brand & logo — AI Pulse identity", description="Official AI Pulse brand guidelines: logo, colour, type, and usage. Download SVG and PNG marks for aipulse.lk.", keywords="AI Pulse logo, brand guidelines, aipulse.lk branding", depth=0, active="about", crumbs=[("Home", ""), ("Brand", "branding.html")], image="logo-light.png", extra_schemas=[{
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": "AI Pulse brand",
        "primaryImageOfPage": absurl("assets/logo-light.png"),
    }], body=body)


def sitemap_page():
    prod_lis = "".join(f'<li><a href="products/{p["slug"]}.html">{p["name"]}</a> — {p["tag"]}</li>' for p in PRODUCTS)
    sol_lis = "".join(f'<li><a href="solutions/{s["slug"]}.html">{s["name"]}</a> — {s["tag"]}</li>' for s in SOLUTIONS)
    body = f'''
    {crumbs_html(0, [("Home", "index.html"), ("Sitemap", "sitemap.html")])}
    <section class="hero" style="min-height:auto">
      <h1 class="display">Sitemap.</h1>
      <p class="subhead mt-4">Every public page on aipulse.lk</p>
    </section>
    <section class="section-tight">
      <div class="wrap grid md:grid-cols-2 gap-10 text-[17px] leading-8">
        <div class="glass p-8">
          <h2 class="text-xl font-semibold mb-3">Company</h2>
          <ul>
            <li><a class="link-more" href="index.html">Home</a></li>
            <li><a href="about.html">About</a></li>
            <li><a href="features.html">Features</a></li>
            <li><a href="customers.html">Customers</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="branding.html">Brand</a></li>
            <li><a href="privacy.html">Privacy</a></li>
            <li><a href="terms.html">Terms</a></li>
          </ul>
        </div>
        <div class="glass p-8">
          <h2 class="text-xl font-semibold mb-3">Products</h2>
          <ul><li><a href="products/index.html">All products</a></li>{prod_lis}</ul>
          <h2 class="text-xl font-semibold mb-3 mt-8">Solutions</h2>
          <ul><li><a href="solutions/index.html">All solutions</a></li>{sol_lis}</ul>
        </div>
      </div>
    </section>'''
    render("sitemap.html", title="Sitemap — AI Pulse", description="HTML sitemap of all AI Pulse pages including products, solutions, brand, and legal.", keywords="AI Pulse sitemap, aipulse.lk pages", depth=0, active="", crumbs=[("Home", ""), ("Sitemap", "sitemap.html")], extra_schemas=[{
        "@context": "https://schema.org",
        "@type": "SiteNavigationElement",
        "name": "AI Pulse sitemap",
        "url": absurl("sitemap.html"),
    }], body=body)


def legal(name, filename, paras):
    blocks = "".join(f'<p class="mt-4 text-[17px] leading-relaxed muted">{p}</p>' for p in paras)
    body = f'''
    {crumbs_html(0, [("Home", "index.html"), (name, filename)])}
    <section class="section">
      <div class="wrap-narrow">
        <h1 class="display-sm">{name}</h1>
        <p class="muted mt-2">Last updated 18 August 2026. Demonstration copy for aipulse.lk.</p>
        {blocks}
      </div>
    </section>'''
    render(filename, title=f"{name} — AI Pulse", description=f"{name} for AI Pulse (Pvt) Ltd, aipulse.lk.", keywords=f"AI Pulse {name.lower()}", depth=0, active="", crumbs=[("Home", ""), (name, filename)], extra_schemas=[{
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": name,
        "url": absurl(filename),
    }], body=body)


def notfound():
    body = '''
    <section class="notfound">
      <div>
        <p class="eyebrow">404</p>
        <h1 class="display mt-3">This page<br>is missing.</h1>
        <p class="subhead mt-4">It may have moved with the product lineup.</p>
        <p class="mt-8"><a class="btn-apple" href="index.html">Back to AI Pulse</a></p>
      </div>
    </section>'''
    render("404.html", title="Page not found — AI Pulse", description="The requested AI Pulse page could not be found.", keywords="404 AI Pulse", depth=0, active="", crumbs=[("Home", "")], body=body)


def write_aux():
    urls = [""]
    urls += ["about.html", "features.html", "customers.html", "contact.html", "branding.html", "sitemap.html", "privacy.html", "terms.html", "products/", "solutions/"]
    urls += [f"products/{p['slug']}.html" for p in PRODUCTS]
    urls += [f"solutions/{s['slug']}.html" for s in SOLUTIONS]
    xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        loc = absurl(u)
        xml.append(f"  <url><loc>{loc}</loc><lastmod>2026-08-18</lastmod><changefreq>weekly</changefreq><priority>{'1.0' if u=='' else '0.8'}</priority></url>")
    xml.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(xml), encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\nDisallow: /404.html\nSitemap: https://aipulse.lk/sitemap.xml\n",
        encoding="utf-8",
    )
    (ROOT / "site.webmanifest").write_text(json.dumps({
        "name": "AI Pulse",
        "short_name": "AI Pulse",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#F5F5F5",
        "theme_color": "#F5F5F5",
        "lang": "en-LK",
        "description": "Intelligence with a pulse. Enterprise software by AI Pulse.",
        "icons": [{"src": "assets/favicon.svg", "sizes": "any", "type": "image/svg+xml"}, {"src": "assets/logo-mark.png", "sizes": "512x512", "type": "image/png"}],
    }, indent=2), encoding="utf-8")
    print("wrote aux")


if __name__ == "__main__":
    home()
    products_index()
    for p in PRODUCTS:
        product_page(p)
    solutions_index()
    for s in SOLUTIONS:
        solution_page(s)
    features_page()
    customers_page()
    about_page()
    contact_page()
    branding_page()
    sitemap_page()
    legal("Privacy Policy", "privacy.html", [
        "AI Pulse (Pvt) Ltd respects your privacy. This demonstration site stores no form submissions on a server. Messages entered in the contact form remain in your browser unless you send them elsewhere.",
        "If we processed personal data in a production service, we would do so under the Personal Data Protection Act of Sri Lanka and, where applicable, GDPR. You would have rights to access, correct, and erase.",
        "We use only essential cookies on this static site. Analytics, if added later, will be disclosed here.",
        "Contact privacy@aipulse.lk for questions. Address: Level 12, World Trade Center, Colombo 01, Sri Lanka.",
    ])
    legal("Terms of Use", "terms.html", [
        "This website is a design demonstration for AI Pulse. Product names, customers, and metrics are mock data unless otherwise stated.",
        "You may browse these pages. You may not copy the brand marks for other companies. The AI Pulse name, pulse mark, and layout are presented as the identity of aipulse.lk.",
        "Software products are offered under separate agreements. Nothing on these pages is an offer of regulated financial, medical, or legal advice.",
        "Governing law: Sri Lanka. Venue: Colombo.",
    ])
    notfound()
    write_aux()
