#!/usr/bin/env python3
"""Static-site generator for the Rosora marketing website (local preview build).
Run: python3 generate.py   (writes *.html files into this directory)
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# Navigation & footer structure (mirrors the client's approved sitemap, §25
# of Rosora_Simple_Website_Brief_for_IT_Consultant.docx)
# ---------------------------------------------------------------------------
NAV = [
    ("Adult", "assessment-adults.html", [
        ("Free Screening Call", "free-screening-call.html"),
        ("Adult Assessments (overview)", "assessment-adults.html"),
        ("ADHD Assessment", "assessment-adhd.html"),
        ("Autism Assessment", "assessment-autism.html"),
        ("Combined ADHD + Autism", "assessment-combined.html"),
        ("QbTest / QbCheck", "assessment-qbtest.html"),
    ]),
    ("Children & Young People", "assessment-children.html", [
        ("Children & Young People (overview)", "assessment-children.html"),
        ("ADHD Assessment", "assessment-adhd.html"),
        ("Autism Assessment", "assessment-autism.html"),
        ("Combined ADHD + Autism", "assessment-combined.html"),
    ]),
    ("Medication", "medication.html", [
        ("ADHD Treatment & Medication Options", "adhd-treatment.html"),
        ("ADHD Coaching", "adhd-coaching.html"),
        ("Transfer Your ADHD Care", "medication-transfer.html"),
        ("ADHD Medication", "medication-assessment.html"),
        ("Titration & Monitoring", "medication-titration.html"),
        ("Medication FAQs", "medication-faqs.html"),
    ]),
    ("Workplace Support", "workplace.html", [
        ("Workplace Needs Assessment", "workplace-needs-assessment.html"),
        ("Access to Work", "access-to-work.html"),
        ("Workplace Coaching", "workplace-coaching.html"),
        ("Employer Support", "employer-support.html"),
    ]),
    ("Coaching", "coaching.html", None),
    ("Fees", "fees.html", None),
    ("Resources", "resources.html", [
        ("Resource Centre", "resources.html"),
        ("Blog", "blog.html"),
        ("FAQs", "faqs.html"),
    ]),
    ("About", "about.html", [
        ("About Rosora", "about.html"),
        ("Our Approach", "our-approach.html"),
        ("Meet the Team", "meet-the-team.html"),
        ("Clinical Standards & Governance", "clinical-governance.html"),
    ]),
    ("Contact", "contact.html", None),
]

FOOTER = {
    "How we help": [
        ("ADHD Assessment", "assessment-adhd.html"),
        ("Autism Assessment", "assessment-autism.html"),
        ("Combined ADHD + Autism", "assessment-combined.html"),
        ("QbTest / QbCheck", "assessment-qbtest.html"),
    ],
    "Useful links": [
        ("About", "about.html"),
        ("Meet The Team", "meet-the-team.html"),
        ("Coaching", "coaching.html"),
        ("Fees", "fees.html"),
        ("Contact", "contact.html"),
        ("Blog", "blog.html"),
        ("FAQs", "faqs.html"),
    ],
    "Policies": [
        ("Privacy Policy", "privacy-policy.html"),
        ("Cookies Policy", "cookies.html"),
        ("Terms & Conditions", "terms.html"),
        ("Cancellation & Refunds", "cancellation-refunds.html"),
        ("Complaints", "complaints.html"),
        ("Safeguarding", "safeguarding.html"),
        ("Accessibility", "accessibility.html"),
        ("Clinical Governance", "clinical-governance.html"),
        ("Duty of Candour", "duty-of-candour.html"),
        ("Regulatory Status", "regulatory-status.html"),
    ],
}

SOCIAL = [("Facebook", "#"), ("Instagram", "#"), ("LinkedIn", "#"), ("Youtube", "#")]

SITE_NAME = "Rosora"
SITE_TAGLINE = "Autism & ADHD Assessment Practice"


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------
def nav_html(current):
    items = []
    for label, href, children in NAV:
        current_attr = ' aria-current="page"' if href == current else ""
        if children:
            sub = "".join(
                '<a href="{}">{}</a>'.format(chref, clabel) for clabel, chref in children
            )
            items.append(
                '<li class="nav-item-dropdown">'
                '<a class="nav-link" href="{href}"{cur}>{label}</a>'
                '<div class="nav-dropdown">{sub}</div>'
                "</li>".format(href=href, cur=current_attr, label=label, sub=sub)
            )
        else:
            items.append(
                '<li><a class="nav-link" href="{href}"{cur}>{label}</a></li>'.format(
                    href=href, cur=current_attr, label=label
                )
            )
    return "".join(items)


def footer_html():
    cols = []
    for heading, links in FOOTER.items():
        items = "".join('<li><a href="{}">{}</a></li>'.format(h, l) for l, h in links)
        cols.append('<div><h4>{}</h4><ul>{}</ul></div>'.format(heading, items))

    social_items = "".join('<li><a href="{}">{}</a></li>'.format(h, l) for l, h in SOCIAL)
    cols.append('<div><h4>Social</h4><ul>{}</ul></div>'.format(social_items))

    contact_col = """
    <div>
      <h4>Get in touch</h4>
      <div class="footer-contact-item"><span class="icon">&#128337;</span><span>Mon&ndash;Fri: 9:00 &ndash; 19:00<br>Sat: 10:00 &ndash; 16:00</span></div>
      <div class="footer-contact-item"><span class="icon">&#128222;</span><span>0330 838 3105</span></div>
      <div class="footer-contact-item"><span class="icon">&#9993;</span><span>enquiries@rosora.co.uk</span></div>
      <div class="footer-contact-item"><span class="icon">&#128205;</span><span>15&ndash;17 New Dover Road<br>Canterbury, Kent<br>CT1 3AS</span></div>
    </div>
    """
    cols.append(contact_col)
    return "".join(cols)


HEAD_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Rosora Autism & ADHD Assessment Practice</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@500;600;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<link rel="icon" href="data:,">
</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
<div class="a11y-overlay"></div>
<aside class="a11y-panel" aria-hidden="true" aria-label="Accessibility settings">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
    <h2>Accessibility</h2>
    <button class="a11y-close" aria-label="Close accessibility panel">✕</button>
  </div>
  <p style="font-size:0.85rem;">Adjust how Rosora's website looks and behaves. Your preferences are saved on this device.</p>

  <div class="a11y-row">
    <span>Text size</span>
    <div class="a11y-btn-group">
      <button data-font-btn="1" aria-pressed="true" aria-label="Default text size">A</button>
      <button data-font-btn="1.15" aria-label="Larger text">A+</button>
      <button data-font-btn="1.3" aria-label="Largest text">A++</button>
    </div>
  </div>
  <div class="a11y-row">
    <span>High contrast</span>
    <label class="switch"><input type="checkbox" data-a11y-switch="contrast"><span class="track"></span></label>
  </div>
  <div class="a11y-row">
    <span>Wider text spacing</span>
    <label class="switch"><input type="checkbox" data-a11y-switch="spacing"><span class="track"></span></label>
  </div>
  <div class="a11y-row">
    <span>Reduce motion</span>
    <label class="switch"><input type="checkbox" data-a11y-switch="motion"><span class="track"></span></label>
  </div>
  <div class="a11y-row" style="border-bottom:none;">
    <span>Highlight links</span>
    <label class="switch"><input type="checkbox" data-a11y-switch="links"><span class="track"></span></label>
  </div>
  <button class="btn btn-outline btn-block btn-sm" style="margin-top:20px;" data-a11y-reset type="button">Reset to default</button>
  <p style="font-size:0.8rem;margin-top:18px;"><a href="accessibility.html">Read our full accessibility statement →</a></p>
</aside>

<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="index.html">
      <span class="brand-mark" aria-hidden="true">R</span>
      <span class="brand-text">
        <span class="brand-name">Rosora</span>
        <span class="brand-sub">Autism &amp; ADHD Assessment</span>
      </span>
    </a>
    <nav class="main-nav" aria-label="Main">
      <ul>{nav}</ul>
      <div class="nav-mobile-actions">
        <a class="btn btn-outline btn-block" href="patient-login.html">Patient Login</a>
        <a class="btn btn-primary btn-block" href="start-your-journey.html">Start Your Journey</a>
      </div>
    </nav>
    <div class="header-actions">
      <button class="a11y-toggle" aria-label="Open accessibility settings" title="Accessibility">♿</button>
      <a href="patient-login.html" class="btn btn-outline btn-sm">Patient Login</a>
      <a href="start-your-journey.html" class="btn btn-primary btn-sm">Start Your Journey</a>
      <button class="nav-toggle" aria-label="Open menu" aria-expanded="false">☰</button>
    </div>
  </div>
</header>
<main id="main">
"""

FOOT_TEMPLATE = """
</main>
<footer class="site-footer-v2">
  <div class="container">
    <div class="footer-grid-v2">
      {footer_cols}
    </div>
    <div class="footer-bottom-v2">
      <span>© 2026 Rosora Autism &amp; ADHD Assessment Practice. All rights reserved.</span>
      <span>Website by <a href="https://devflow.co.uk">Devflow</a></span>
    </div>
  </div>
  <div class="footer-watermark" aria-hidden="true">Rosora</div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
"""


def page(title, description, slug, body):
    html = HEAD_TEMPLATE.format(nav=nav_html(slug), title=title, description=description)
    html += body
    html += FOOT_TEMPLATE.format(footer_cols=footer_html())
    with open(os.path.join(ROOT, slug), "w", encoding="utf-8") as f:
        f.write(html)


# ---------------------------------------------------------------------------
# Reusable content components
# ---------------------------------------------------------------------------
def breadcrumb(parent_label, parent_href, current):
    return (
        '<div class="container"><p class="breadcrumb">'
        '<a href="index.html">Home</a> / <a href="{}">{}</a> / {}'
        "</p></div>"
    ).format(parent_href, parent_label, current)


def page_hero(eyebrow, title, lede, cta_label="Start Your Journey", cta_href="start-your-journey.html", show_ask=True):
    primary_btn = (
        '<a class="btn btn-primary" href="{cta_href}">{cta_label}</a>'.format(cta_href=cta_href, cta_label=cta_label)
        if cta_label else ""
    )
    ask_btn = '<a class="btn btn-outline" href="contact.html">Ask a Question</a>' if show_ask else ""
    cta_row = (
        '<div class="hero-cta-row">{primary}{ask}</div>'.format(primary=primary_btn, ask=ask_btn)
        if (primary_btn or ask_btn) else ""
    )
    return """
    <section class="page-hero">
      <div class="container">
        <span class="eyebrow">{eyebrow}</span>
        <h1>{title}</h1>
        <p class="lede">{lede}</p>
        {cta_row}
      </div>
    </section>
    """.format(eyebrow=eyebrow, title=title, lede=lede, cta_row=cta_row)


def content_block(title, paragraphs, alt=False):
    ps = "".join("<p>{}</p>".format(p) for p in paragraphs)
    return """
    <section class="{alt}">
      <div class="container-narrow">
        <h2>{title}</h2>
        {ps}
      </div>
    </section>
    """.format(title=title, ps=ps, alt="section-alt" if alt else "")


def bullet_section(title, items, alt=False, lede=""):
    lis = "".join("<li>{}</li>".format(i) for i in items)
    lede_html = '<p class="lede">{}</p>'.format(lede) if lede else ""
    return """
    <section class="{alt}">
      <div class="container-narrow">
        <h2>{title}</h2>
        {lede}
        <ul class="list-check">{lis}</ul>
      </div>
    </section>
    """.format(title=title, lis=lis, alt="section-alt" if alt else "", lede=lede_html)


def pathway(title, steps, alt=False):
    nodes = ""
    for i, s in enumerate(steps):
        if i > 0:
            nodes += '<span class="pathway-arrow">→</span>'
        nodes += '<span class="pathway-node">{}</span>'.format(s)
    return """
    <section class="{alt}">
      <div class="container">
        <h2>{title}</h2>
        <div class="pathway-strip">{nodes}</div>
      </div>
    </section>
    """.format(title=title, nodes=nodes, alt="section-alt" if alt else "")


def cards_grid(title, cards, cols=3, alt=False, lede=""):
    """cards: list of (icon, heading, text, href, link_label)"""
    items = ""
    for icon, heading, text, href, link_label in cards:
        items += """
        <a class="card service-card" href="{href}" style="text-decoration:none;display:block;">
          <div class="card-icon">{icon}</div>
          <h3>{heading}</h3>
          <p>{text}</p>
          <span class="card-link">{link_label} →</span>
        </a>
        """.format(icon=icon, heading=heading, text=text, href=href, link_label=link_label)
    lede_html = '<p class="lede">{}</p>'.format(lede) if lede else ""
    return """
    <section class="{alt}">
      <div class="container">
        <h2>{title}</h2>
        {lede}
        <div class="grid grid-{cols}">{items}</div>
      </div>
    </section>
    """.format(title=title, items=items, cols=cols, alt="section-alt" if alt else "", lede=lede_html)


def faq_section(title, qa, alt=False):
    items = ""
    for q, a in qa:
        items += """
        <details class="faq-item"><summary>{q}</summary><p>{a}</p></details>
        """.format(q=q, a=a)
    return """
    <section class="{alt}">
      <div class="container-narrow">
        <h2>{title}</h2>
        {items}
      </div>
    </section>
    """.format(title=title, items=items, alt="section-alt" if alt else "")


def cta_band(title, text, cta_label="Start Your Journey", cta_href="start-your-journey.html"):
    return """
    <section>
      <div class="container">
        <div class="cta-band">
          <h2>{title}</h2>
          <p>{text}</p>
          <a class="btn btn-outline-white" href="{href}">{label}</a>
        </div>
      </div>
    </section>
    """.format(title=title, text=text, href=cta_href, label=cta_label)


def note(text):
    return '<div class="important-note"><strong>Important:</strong> {}</div>'.format(text)
