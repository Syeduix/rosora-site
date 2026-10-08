#!/usr/bin/env python3
import os
from generate import ROOT
from generate import (
    page, breadcrumb, page_hero, content_block, bullet_section, pathway,
    cards_grid, faq_section, cta_band, note,
)

# ===========================================================================
# HOME
# ===========================================================================
def img(seed, w, h):
    return "https://picsum.photos/seed/{}/{}/{}".format(seed, w, h)



def screener_cards(heading="For adults"):
    arrow = '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M3 11L11 3M11 3H4.5M11 3V9.5" stroke="#0C1429" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    items = [("ADHD", "adhd", "Attention, focus, organisation, restlessness and impulsivity.", "t1"),
             ("Autism", "autism", "Social communication, sensory experience, routines and interests.", "t2"),
             ("AuDHD", "audhd", "Where ADHD and Autism traits may both be part of the picture.", "t3")]
    cards = "".join(
        '<a class="sc-card %s" href="screener.html?type=%s"><span class="sc-card-tag">Free screener</span>'
        '<h3>%s</h3><p>%s</p><span class="sc-card-link">Start Your Free %s Screener<span class="arr">%s</span></span></a>'
        % (c, k, t, d, t, arrow) for t, k, d, c in items)
    return ('<section><div class="container"><div class="sc-head"><div><div class="hp-eyebrow">%s</div>'
            '<h2>Start with a free screener</h2></div>'
            '<p>Your answers are sent to your email and to the Rosora team, who will call you to offer a free consultation.</p></div>'
            '<div class="sc-cards">%s</div></div></section>') % (heading, cards)

home_body = """
<section class="hp-hero">
  <div class="container hp-hero-grid">
    <div>
      <div class="hp-hero-eyebrow">Welcome to Rosora Autism &amp; ADHD Assessment Practice</div>
      <h1>From Questions to Clarity</h1>
      <p class="lede">Rosora provides specialist, clinician-led Autism and ADHD assessments for children,
      young people and adults.</p>
      <div class="hero-cta-row">
        <a class="btn btn-navy" href="assessment-adults.html">Explore Assessments</a>
        <a class="btn btn-outline" href="start-your-journey.html">Start Your Journey</a>
      </div>
      <div class="hp-nice-note">Informed by NICE guidance and recognised diagnostic standards.</div>
    </div>
    <div class="hp-hero-img">
      <img src="{hero_img}" alt="A family laughing together outdoors" loading="eager">
    </div>
  </div>
</section>

<div class="hp-marquee-wrap" aria-hidden="true">
  <div class="hp-marquee">
    <span>Healing</span><span class="dot"></span><span>Recovery</span><span class="dot"></span>
    <span>Wellness</span><span class="dot"></span><span>Support</span><span class="dot"></span>
    <span>Growth</span><span class="dot"></span><span>Clarity</span><span class="dot"></span>
    <span>Healing</span><span class="dot"></span><span>Recovery</span><span class="dot"></span>
    <span>Wellness</span><span class="dot"></span><span>Support</span><span class="dot"></span>
    <span>Growth</span><span class="dot"></span><span>Clarity</span><span class="dot"></span>
  </div>
</div>

<section class="hp-about">
  <div class="container">
    <div class="hp-about-top">
      <div>
        <div class="hp-eyebrow">Who We Are</div>
        <h2>Assessment that considers the whole person</h2>
      </div>
      <div class="hp-about-copy">
        <p class="hp-about-lead">We carry out our assessments in line with relevant NICE guidance and recognised diagnostic standards, using a comprehensive, evidence-informed approach that considers the whole person, not just scores on questionnaires or screening tools.</p>
        <p>We take time to understand developmental history, current experiences, strengths, challenges and the impact of symptoms or characteristics across everyday life, including home, education, work, relationships and social settings. Where appropriate, we also consider information from parents, carers, partners, schools, or other informants as part of the assessment.</p>
        <p>We also consider alternative explanations and coexisting conditions to support careful clinical formulation and diagnostic decision-making.</p>
      </div>
    </div>

  </div>
</section>

<div class="hp-break-img">
  <img src="{break_img}" alt="A parent and child working together at a table" loading="lazy">
</div>

<section class="hp-outcome-wrap">
  <div class="container">
    <div class="hp-outcome">
      <div>
        <div class="hp-eyebrow">Your experience</div>
        <h2>What you can expect</h2>
        <p>From your first enquiry through assessment, diagnostic feedback, and recommendations, our aim is to provide a clear, compassionate, person-centred experience.</p>
      </div>
      <div>
        <p class="hp-outcome-lead">Where diagnostic criteria are met, you will receive:</p>
        <ul class="hp-outcome-list">
          <li><span>1</span>A clear diagnostic outcome</li>
          <li><span>2</span>A comprehensive clinical report</li>
          <li><span>3</span>Personalised recommendations to help you understand the next steps</li>
        </ul>
      </div>
    </div>
    <div class="hp-tagline">
      <b>Clear assessment. Compassionate care. Greater understanding.</b>
      <div class="hp-nice-row">
        <span class="hp-nice-label">Assessment pathways are informed by NICE guidance:</span>
        <span class="hp-nice-pill"><b>NG87</b> ADHD</span>
        <span class="hp-nice-pill"><b>CG128</b> Autism in children and young people</span>
        <span class="hp-nice-pill"><b>CG142</b> Autism in adults</span>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="hp-section-head">
      <div>
        <div class="hp-eyebrow">How We Can Help</div>
        <h2>Specialized care<br>for adults and children</h2>
      </div>
      <a class="btn-arrow" href="start-your-journey.html">Start Your Journey<span class="arr">↗</span></a>
    </div>

    <div class="hp-service-row">
      <div class="hp-service-row-img"><img src="{svc1_img}" alt="A clinician talking with an adult client" loading="lazy"></div>
      <div>
        <h3>Adult Assessment</h3>
        <p>Comprehensive ADHD, Autism, and Combined evaluations tailored for adults, high-masking individuals, and professionals.</p>
        <a class="hp-book-link" href="assessment-adults.html">Book Now →</a>
      </div>
    </div>
    <div class="hp-service-row">
      <div class="hp-service-row-img"><img src="{svc2_img}" alt="A clinician talking with a parent and child" loading="lazy"></div>
      <div>
        <h3>Children Assessment</h3>
        <p>Gentle, age-adapted evaluations for children and teens (aged 5–17), integrating parent insights and school observer data.</p>
        <a class="hp-book-link" href="assessment-children.html">Book Now →</a>
      </div>
    </div>
    <div class="hp-service-row">
      <div class="hp-service-row-img"><img src="{svc3_img}" alt="A workplace coaching session" loading="lazy"></div>
      <div>
        <h3>Workplace Assessment</h3>
        <p>Specialized evaluations and practical accommodation guidance to help neurodivergent employees thrive at work.</p>
        <a class="hp-book-link" href="workplace-needs-assessment.html">Book Now →</a>
      </div>
    </div>
    <div class="hp-service-row">
      <div class="hp-service-row-img"><img src="{svc4_img}" alt="A clinician preparing an assessment" loading="lazy"></div>
      <div>
        <h3>Qb Test/Qb Check</h3>
        <p>FDA-cleared computerized motion tracking that provides objective visual data on focus, impulsivity, and motor activity.</p>
        <a class="hp-book-link" href="assessment-qbtest.html">Book Now →</a>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <h2 style="text-align:center;max-width:780px;margin:0 auto 44px;">Assessment that feels like it was built around you</h2>
    <div class="hp-feature-grid">
      <div class="hp-feature-col">
        <div class="hp-feature-card hp-feature-tint-1">
          <div class="hp-feature-icon">🩺</div>
          <h3>GMC-registered Consultant Psychiatrists and clinicians</h3>
          <p>Experienced, UK-registered clinical specialists conducting gold-standard assessments in accordance with NICE guidelines.</p>
        </div>
        <div class="hp-feature-card hp-feature-tint-3">
          <div class="hp-feature-icon">🛡️</div>
          <h3>Transparent, published fees with no hidden costs</h3>
          <p>Clear pricing structures from the start so you can make informed care decisions with total confidence.</p>
        </div>
      </div>
      <div class="hp-feature-img"><img src="{feature_img}" alt="A woman looking thoughtfully into the distance" loading="lazy"></div>
      <div class="hp-feature-col">
        <div class="hp-feature-card hp-feature-tint-2">
          <div class="hp-feature-icon">👤</div>
          <h3>Individualised assessments — not a one-size-fits-all checklist</h3>
          <p>We tailor every evaluation to your unique developmental history, communication preferences, and personal needs.</p>
        </div>
        <div class="hp-feature-card hp-feature-tint-4">
          <div class="hp-feature-icon">🤝</div>
          <h3>Support that continues after diagnosis, not just up to it</h3>
          <p>Post-diagnostic coaching, medication titration pathways, and workplace guidance to ensure long-term progress.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container hp-journey-grid">
    <div class="hp-journey-img"><img src="{journey_img}" alt="Two people talking warmly together" loading="lazy"></div>
    <div>
      <div class="hp-eyebrow">The Process</div>
      <h2>A Simple Patient Journey</h2>
      <ul class="hp-journey-list">
        <li><span class="hp-journey-num">01</span><div class="hp-journey-body"><h3>Enquiry &amp; Triage</h3><p>Complete our brief online form. Our care team reviews your details within 24 hours to match you with the appropriate clinical pathway (Adult, Child, or Combined).</p></div></li>
        <li><span class="hp-journey-num">02</span><div class="hp-journey-body"><h3>Pre-Assessment Information Gathering</h3></div></li>
        <li><span class="hp-journey-num">03</span><div class="hp-journey-body"><h3>Objective Computerized Testing (QbCheck)</h3></div></li>
        <li><span class="hp-journey-num">04</span><div class="hp-journey-body"><h3>Clinical Assessment Consultation</h3></div></li>
        <li><span class="hp-journey-num">05</span><div class="hp-journey-body"><h3>Diagnostic Outcome &amp; Continuous Aftercare</h3></div></li>
      </ul>
      <a class="btn btn-navy" href="start-your-journey.html">Start Your Journey</a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="hp-coaching-band">
      <div class="hp-section-head">
        <div>
          <div class="hp-eyebrow">Aftercare</div>
          <h2>Coaching &amp; Post-<br>Diagnostic Support</h2>
        </div>
        <a class="btn btn-primary" href="coaching.html">Learn More About Coaching</a>
      </div>
      <div class="grid grid-3">
        <a class="hp-blog-card" href="coaching.html">
          <div class="hp-blog-thumb"><img src="{coach1_img}" alt="A person smiling at their laptop" loading="lazy"></div>
          <h3>ADHD, Autism &amp; AuDHD Coaching</h3>
          <p style="margin-bottom:18px;">One-on-one coaching to understand your neurotype, prevent burnout, and build sustainable routines.</p>
          <span class="hp-book-link">Enquire Now →</span>
        </a>
        <a class="hp-blog-card" href="coaching.html">
          <div class="hp-blog-thumb"><img src="{coach2_img}" alt="A person practising mindfulness" loading="lazy"></div>
          <h3>Executive Function &amp; Wellbeing</h3>
          <p style="margin-bottom:18px;">Practical strategies for task initiation, organization, sensory balance, and energy regulation.</p>
          <span class="hp-book-link">Enquire Now →</span>
        </a>
        <a class="hp-blog-card" href="coaching.html">
          <div class="hp-blog-thumb"><img src="{coach3_img}" alt="A person working at a desk" loading="lazy"></div>
          <h3>Career &amp; Workplace Coaching</h3>
          <p style="margin-bottom:18px;">Guidance for defining reasonable adjustments, managing deadlines, and navigating corporate communication.</p>
          <span class="hp-book-link">Enquire Now →</span>
        </a>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container hp-testimonial-grid">
    <div>
      <div class="hp-eyebrow">Testimonials</div>
      <h2>Here's what our patients have to say</h2>
    </div>
    <div>
      <div class="hp-quote-mark">&ldquo;</div>
      <p class="hp-testimonial-text">Rosora provided an environment where I finally felt completely understood. From the initial pre-assessment questionnaires to the clinical interview, everything was handled with immense warmth, clarity, and professionalism.</p>
      <div class="hp-testimonial-person">
        <div class="hp-testimonial-who">
          <div class="hp-testimonial-photo"><img src="{testimonial_img}" alt="Photo of Julia Hendrick" loading="lazy"></div>
          <div>
            <div class="hp-testimonial-name">Julia Hendrick</div>
            <div class="hp-testimonial-role">Adult ADHD Assessment Patient</div>
          </div>
        </div>
        <div class="hp-carousel-nav">
          <button type="button" aria-label="Previous testimonial">&#8592;</button>
          <button type="button" aria-label="Next testimonial">&#8594;</button>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="hp-faq-dark">
      <div class="hp-faq-grid">
        <div>
          <div class="hp-eyebrow">Frequently Asked Questions</div>
          <h2>Common ADHD &amp; Autism questions answered</h2>
          <a class="btn btn-primary" href="faqs.html">See All FAQs</a>
          <div class="hp-stat-card">
            <div class="hp-stat-photo"><img src="{stat_img}" alt="A smiling Rosora patient" loading="lazy"></div>
            <div>
              <div class="hp-stat-number">100%</div>
              <div class="hp-stat-label">Committed to care</div>
            </div>
          </div>
        </div>
        <div>
          <details class="faq-item" open><summary>What can I expect during my first clinical consultation?</summary><p>A clear conversation about your history and current functioning, led by an appropriately qualified clinician.</p></details>
          <details class="faq-item"><summary>How long does the assessment process take from start to finish?</summary><p>This varies by pathway; we explain the timeline at your first contact.</p></details>
          <details class="faq-item"><summary>Are private assessments recognized by schools, employers, and the NHS?</summary><p>Answer to be confirmed by Rosora.</p></details>
          <details class="faq-item"><summary>Do I need a GP referral to book an assessment with Rosora?</summary><p>Both self-referral and professional referral are welcome.</p></details>
          <details class="faq-item"><summary>What support options are available after a formal diagnosis?</summary><p>Coaching, medication pathways and workplace guidance are available after diagnosis.</p></details>
        </div>
      </div>
    </div>
  </div>
</section>
""" + f"""
<section>
  <div class="container">
    <div class="hp-section-head">
      <div>
        <div class="hp-eyebrow">Blogs</div>
        <h2>News and everyday<br>advice for managing life<br>with ADHD &amp; Autism</h2>
      </div>
      <a class="btn btn-navy" href="blog.html">See All Blogs</a>
    </div>
    <div class="grid grid-3">
      <a class="hp-blog-card" href="blog-post-understanding-adult-adhd.html">
        <div class="hp-blog-thumb"><img src="{img('rosora-blog-1', 500, 340)}" alt="A woman smiling while drinking coffee" loading="lazy"></div>
        <div class="hp-tag-row"><span class="hp-tag-pill">ADHD</span><span class="hp-tag-pill">Autism</span><span class="hp-tag-pill">Children &amp; Teenagers</span></div>
        <h3>The Role of Qualified Professionals in ADHD Assessments</h3>
        <div class="hp-blog-byline">By Carl Baron &nbsp;&bull;&nbsp; 14 Jan 2026</div>
      </a>
      <a class="hp-blog-card" href="blog-post-preparing-for-assessment.html">
        <div class="hp-blog-thumb"><img src="{img('rosora-blog-2', 500, 340)}" alt="A family laughing together" loading="lazy"></div>
        <div class="hp-tag-row"><span class="hp-tag-pill">ADHD</span><span class="hp-tag-pill">Autism</span><span class="hp-tag-pill">Children &amp; Teenagers</span></div>
        <h3>Understanding ADHD Assessments for Children: What Parents Need to Know</h3>
        <div class="hp-blog-byline">By Carl Baron &nbsp;&bull;&nbsp; 14 Jan 2026</div>
      </a>
      <a class="hp-blog-card" href="blog.html">
        <div class="hp-blog-thumb"><img src="{img('rosora-blog-3', 500, 340)}" alt="A clinician talking with a client" loading="lazy"></div>
        <div class="hp-tag-row"><span class="hp-tag-pill">ADHD</span><span class="hp-tag-pill">Autism</span><span class="hp-tag-pill">Children &amp; Teenagers</span></div>
        <h3>Signs Your Child Might be Autistic and How to Support Them Through Daily Transitions</h3>
        <div class="hp-blog-byline">By Carl Baron &nbsp;&bull;&nbsp; 14 Jan 2026</div>
      </a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="hp-cta-band">
      <div class="hp-cta-photo left"><img src="{img('rosora-cta-left', 220, 300)}" alt=""></div>
      <div class="hp-eyebrow" style="justify-content:center;">Start Your Journey</div>
      <h2>Ready to take the first step?</h2>
      <p>Tell us a little about what's brought you here, and our team will review your information
      and be in touch to discuss the most appropriate next step.</p>
      <a class="btn btn-primary" href="start-your-journey.html">Start Your Journey</a>
      <div class="hp-cta-photo right"><img src="{img('rosora-cta-right', 300, 260)}" alt=""></div>
    </div>
  </div>
</section>
"""

home_body = home_body.format(
    hero_img=img("rosora-hero-family", 800, 660),
    break_img=img("rosora-homework", 1400, 620),
    svc1_img=img("rosora-svc-adult", 600, 440),
    svc2_img=img("rosora-svc-children", 600, 440),
    svc3_img=img("rosora-svc-workplace", 600, 440),
    svc4_img=img("rosora-svc-qbtest", 600, 440),
    feature_img=img("rosora-feature-woman", 560, 780),
    journey_img=img("rosora-journey", 640, 760),
    coach1_img=img("rosora-coach-1", 500, 340),
    coach2_img=img("rosora-coach-2", 500, 340),
    coach3_img=img("rosora-coach-3", 500, 340),
    testimonial_img=img("rosora-testimonial", 200, 200),
    stat_img=img("rosora-stat", 200, 200),
)

page("Home", "Rosora provides specialist, clinician-led Autism and ADHD assessments for children, young people and adults — clear, compassionate and person-centred.", "index.html", home_body)


# ===========================================================================
# ASSESSMENTS HUB
# ===========================================================================
assessments_body = page_hero(
    "Assessments",
    "Autism &amp; ADHD Assessments",
    "Every assessment at Rosora is led by an appropriately qualified clinician and shaped around "
    "your history, your current functioning, and what matters to you — not a fixed checklist.",
) + cards_grid(
    "Choose an Assessment Pathway",
    [
        ("🧠", "ADHD Assessment", "For adults, children and young people — a thorough look at attention, activity and impulsivity across your life.", "assessment-adhd.html", "About ADHD assessment"),
        ("🧩", "Autism Assessment", "Exploring communication, interaction, sensory experience and developmental history.", "assessment-autism.html", "About Autism assessment"),
        ("🔗", "Combined ADHD + Autism", "One coordinated pathway when both may be relevant, without repeating information.", "assessment-combined.html", "About combined assessment"),
        ("🧑", "Adult Assessments", "What to expect if you are seeking assessment as an adult.", "assessment-adults.html", "For adults"),
        ("🧒", "Children &amp; Young People", "How the process differs for children and young people, and the role of parents/carers and schools.", "assessment-children.html", "For children & young people"),
        ("📊", "QbTest / QbCheck", "A computer-based measure that may support — but never replaces — clinical judgement.", "assessment-qbtest.html", "About QbTest/QbCheck"),
    ],
    cols=3,
) + content_block(
    "What every assessment considers",
    [
        "Regardless of pathway, a Rosora assessment brings together your developmental history, "
        "your current day-to-day functioning, and — where appropriate — information from someone "
        "who knows you well (an informant). We consider supporting evidence such as school reports, "
        "an EHCP, or previous clinical letters where these are available.",
        "You will always receive clear feedback on the outcome, and a written report you can share "
        "with your GP or other professionals involved in your care.",
    ],
    alt=True,
) + cta_band("Not sure which pathway is right for you?", "Start your journey and let our team guide you to the most appropriate assessment.")

page("Assessments", "Explore ADHD, Autism and Combined assessment pathways at Rosora, for adults, children and young people.", "assessments.html", assessments_body)


# ===========================================================================
# ADHD ASSESSMENT
# ===========================================================================
adhd_body = breadcrumb("Assessments", "assessments.html", "ADHD Assessment") + page_hero(
    "ADHD Assessment",
    "ADHD Assessment",
    "ADHD (Attention Deficit Hyperactivity Disorder) can affect attention, activity levels and "
    "impulsivity in ways that shape daily life. Assessment may help if these patterns have been "
    "present since childhood and are affecting you now.",
) + content_block(
    "What ADHD is, and when assessment may help",
    [
        "ADHD is a recognised neurodevelopmental condition. It can look different in different "
        "people — some struggle most with focus and organisation, others with restlessness or "
        "impulsive decisions, and many experience a mix of both. Assessment may be helpful if these "
        "patterns have been present since childhood, occur across more than one area of life (such "
        "as work, home or relationships), and are having a meaningful impact on you.",
    ],
) + cards_grid(
    "Assessment for every age",
    [
        ("🧑", "Adult ADHD Assessment", "For adults seeking assessment for the first time, or exploring whether earlier difficulties may be ADHD.", "assessment-adults.html", "Read more"),
        ("🧒", "Child/Young Person ADHD Assessment", "A developmentally appropriate process involving parents/carers and, where relevant, school.", "assessment-children.html", "Read more"),
    ],
    cols=2,
) + bullet_section(
    "What the assessment considers",
    [
        "Your developmental history and how things have changed over time",
        "Current functioning across home, work/education and relationships",
        "Informant or supporting information from someone who knows you well, where appropriate",
        "QbTest/QbCheck, where clinically indicated, as one part of the wider picture",
        "A full clinical assessment, leading to an outcome, feedback and a written report",
    ],
    alt=True,
) + note("QbTest/QbCheck and other tools support clinical judgement — they do not diagnose ADHD by themselves. See our QbTest/QbCheck page for more detail.") \
+ """<section><div class="container" style="text-align:center;">
<a class="btn btn-primary" href="start-your-journey.html">Start Your Journey</a>
</div></section>"""

page("ADHD Assessment", "Understand what an ADHD assessment at Rosora involves, for adults, children and young people.", "assessment-adhd.html", adhd_body)


# ===========================================================================
# AUTISM ASSESSMENT
# ===========================================================================
autism_body = breadcrumb("Assessments", "assessments.html", "Autism Assessment") + page_hero(
    "Autism Assessment",
    "Autism Assessment",
    "Autism is a lifelong way of experiencing and interacting with the world. Assessment can bring "
    "clarity to lifelong patterns in communication, social interaction and sensory experience.",
) + cards_grid(
    "Assessment for every age",
    [
        ("🧑", "Adult Autism Assessment", "For adults exploring whether autism may explain lifelong patterns and experiences.", "assessment-adults.html", "Read more"),
        ("🧒", "Children &amp; Young People's Autism Assessment", "A developmentally appropriate process involving parents/carers and school where relevant.", "assessment-children.html", "Read more"),
    ],
    cols=2,
) + bullet_section(
    "What the assessment considers",
    [
        "Developmental history, from early childhood to the present day",
        "Communication, social interaction and sensory experiences",
        "Masking or camouflaging, where relevant — and how this may have shaped earlier impressions of you",
        "Informant and supporting information from people who know you well",
        "Clinical assessment and, where required, additional components",
        "A considered outcome, feedback session and written report",
    ],
    alt=True,
) + """<section><div class="container" style="text-align:center;">
<a class="btn btn-primary" href="start-your-journey.html">Start Your Journey</a>
</div></section>"""

page("Autism Assessment", "Understand what an Autism assessment at Rosora involves, for adults, children and young people.", "assessment-autism.html", autism_body)


# ===========================================================================
# COMBINED ADHD + AUTISM
# ===========================================================================
combined_body = breadcrumb("Assessments", "assessments.html", "Combined ADHD + Autism") + page_hero(
    "Combined Assessment",
    "Combined ADHD + Autism Assessment",
    "ADHD and Autism can and do co-occur. When both may be relevant, a combined assessment offers "
    "one coordinated pathway rather than two separate processes.",
) + content_block(
    "When a combined assessment may be appropriate",
    [
        "If your history and current experience suggest that both ADHD and Autism may be relevant, "
        "our clinical team can consider both within a single, coordinated pathway. This means your "
        "background and current functioning are considered together — by clinicians thinking about "
        "how the two may interact — rather than through two disconnected assessments.",
    ],
) + bullet_section(
    "How the combined pathway works",
    [
        "One registration and one shared intake — you are not asked to repeat the same background information twice",
        "ADHD-specific and Autism-specific components, each led by an appropriately qualified clinician",
        "Informant and supporting information gathered once, used across both parts of the assessment",
        "A single clinical formulation considering both conditions together",
        "One outcome, one feedback session, and one written report",
    ],
    alt=True,
) + """<section><div class="container" style="text-align:center;">
<a class="btn btn-primary" href="start-your-journey.html">Start Your Journey</a>
</div></section>"""

page("Combined ADHD + Autism Assessment", "A single, coordinated assessment pathway when both ADHD and Autism may be relevant.", "assessment-combined.html", combined_body)


# ===========================================================================
# ADULT ASSESSMENTS (overview across pathways)
# ===========================================================================
adults_body = breadcrumb("Assessments", "assessments.html", "Adult Assessments") + page_hero(
    "For Adults",
    "Adult Assessments",
    "Many adults reach out to Rosora after years of feeling that something doesn't quite add up — "
    "at work, in relationships, or in day-to-day life. It's never too late to seek clarity.",
) + content_block(
    "What to expect as an adult client",
    [
        "As an adult, you can self-refer or be referred by a GP or another professional. We'll ask "
        "about your developmental history as far back as you can recall, alongside how things affect "
        "you now — at work, at home, and in relationships. Where possible, an informant such as a "
        "parent, partner or close friend can add useful context, though this isn't always essential.",
        "Adult assessment is available for ADHD, Autism, or both together through our Combined pathway.",
    ],
) + cards_grid(
    "Choose your pathway",
    [
        ("🧠", "Adult ADHD Assessment", "Explore the ADHD assessment pathway for adults.", "assessment-adhd.html", "Learn more"),
        ("🧩", "Adult Autism Assessment", "Explore the Autism assessment pathway for adults.", "assessment-autism.html", "Learn more"),
        ("🔗", "Combined Assessment", "One coordinated pathway for both.", "assessment-combined.html", "Learn more"),
    ],
    cols=3,
    alt=True,
)

adults_body = adults_body + screener_cards("For adults")
page("Adult Assessments", "What to expect from an ADHD, Autism or combined assessment at Rosora as an adult.", "assessment-adults.html", adults_body)


# ===========================================================================
# CHILDREN & YOUNG PEOPLE
# ===========================================================================
children_body = breadcrumb("Assessments", "assessments.html", "Children & Young People") + page_hero(
    "For Families",
    "Children &amp; Young People",
    "Assessment for children and young people is a family-centred process — we work closely with "
    "parents, carers and, where appropriate, school, to build a full and fair picture.",
) + bullet_section(
    "How the process works for children and young people",
    [
        "ADHD, Autism and Combined assessment pathways are all available for children and young people",
        "Parents and carers are involved throughout, and are usually the primary source of developmental history",
        "School, teachers or a SENCO may be asked to contribute information where this is helpful and appropriate",
        "We consider supporting evidence such as school reports, an Education, Health and Care Plan (EHCP), and any previous assessments or reports",
        "The pace and format of the assessment is adapted to the child or young person's age and needs",
    ],
) + content_block(
    "Working with schools",
    [
        "With your consent, we may ask your child's school for observations relevant to the "
        "assessment. This is never a substitute for your own knowledge of your child, but it adds a "
        "valuable second perspective on how they present across different settings.",
    ],
    alt=True,
) + """<section><div class="container" style="text-align:center;">
<a class="btn btn-primary" href="start-your-journey.html">Start Your Journey for Your Child</a>
</div></section>"""

page("Children & Young People", "How ADHD and Autism assessment works for children and young people at Rosora, including the role of parents, carers and schools.", "assessment-children.html", children_body)


# ===========================================================================
# QBTEST / QBCHECK
# ===========================================================================
qbtest_body = breadcrumb("Assessments", "assessments.html", "QbTest / QbCheck") + page_hero(
    "A Clinical Tool, Not a Diagnosis",
    "QbTest &amp; QbCheck",
    "QbTest and QbCheck are computer-based tools that measure attention, activity and impulse "
    "control. They can add useful, objective information to an ADHD assessment.",
) + content_block(
    "What QbTest/QbCheck involves",
    [
        "During QbTest or QbCheck, you complete a short computer-based task while a motion sensor "
        "tracks movement, and the software measures attention and impulse control. It's straightforward "
        "and non-invasive, and results are available quickly.",
        "We may use QbTest or QbCheck where it's clinically indicated — that is, where your clinician "
        "feels it will meaningfully add to the wider assessment, not as a routine step for everyone.",
    ],
) + """<section class="section-alt"><div class="container-narrow">""" + note(
    "QbTest/QbCheck does not diagnose ADHD on its own. Results are always considered alongside your "
    "history, current functioning and the rest of the clinical assessment — never in isolation."
) + "</div></section>" + content_block(
    "How results are used",
    [
        "Your clinician reviews QbTest/QbCheck results alongside everything else gathered during "
        "your assessment — your developmental history, informant information, and clinical "
        "observation — to reach a considered, whole-picture outcome.",
    ],
) + """<section><div class="container" style="text-align:center;">
<a class="btn btn-outline" href="assessment-adhd.html">← Back to ADHD Assessment</a>
</div></section>"""

page("QbTest / QbCheck", "Understand what QbTest and QbCheck are, and how they support — but don't replace — a full ADHD assessment.", "assessment-qbtest.html", qbtest_body)


# ===========================================================================
# MEDICATION HUB
# ===========================================================================
medication_body = page_hero(
    "Medication",
    "Medication Support",
    "If medication may help following an ADHD diagnosis, we make the pathway clear from the outset "
    "— including what Rosora does and doesn't do.",
) + """<section><div class="container-narrow">""" + note(
    "Rosora does not hold or dispense medication directly, and shared-care arrangements are not "
    "currently available through Rosora. Medication is prescribed and monitored via your nominated "
    "pharmacy and prescriber, following the pathway below."
) + "</div></section>" + pathway(
    "The Medication Pathway",
    ["Diagnosis", "Medication Assessment", "Prescriber Review", "Treatment Decision", "Prescription", "Nominated Pharmacy", "Titration &amp; Monitoring", "Ongoing Review"],
    alt=True,
) + cards_grid(
    "Learn more",
    [
        ("🧭", "ADHD Treatment &amp; Medication Options", "Personalised treatment, medication, titration and non-medication support.", "adhd-treatment.html", "Read more"),
        ("🔁", "Transfer Your ADHD Care", "Already diagnosed elsewhere? How Rosora can take over your medication care.", "medication-transfer.html", "Read more"),
        ("💊", "ADHD Medication Assessment", "What happens at the medication assessment stage, following diagnosis.", "medication-assessment.html", "Read more"),
        ("📈", "Titration &amp; Monitoring", "How dosage is reviewed and adjusted, and what ongoing monitoring involves.", "medication-titration.html", "Read more"),
        ("❓", "Medication FAQs", "Common questions about ADHD medication, answered plainly.", "medication-faqs.html", "Read more"),
    ],
    cols=3,
)

page("Medication Support", "Understand the ADHD medication pathway at Rosora, from diagnosis through to ongoing review.", "medication.html", medication_body)

# ===========================================================================
# MEDICATION — TRANSFER OF CARE
# ===========================================================================
_ARROW = '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M3 11L11 3M11 3H4.5M11 3V9.5" stroke="#0C1429" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
_CHECK = '<svg width="18" height="18" viewBox="0 0 18 18" fill="none" aria-hidden="true"><path d="M4 9.5l3.2 3.2L14 5.8" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def _cta(label, href="start-your-journey.html"):
    return '<a class="btn-arrow" href="%s">%s<span class="arr">%s</span></a>' % (href, label, _ARROW)

def _check_item(title, text):
    return ('<div class="tx-check"><div class="ic">%s</div><div><b>%s</b><span>%s</span></div></div>' % (_CHECK, title, text))

def _step(num, title, body, fee=None, extra=""):
    fee_html = '<span class="tx-fee">%s</span>' % fee if fee else ""
    return ('<li class="tx-step"><div class="tx-step-top"><span class="tx-step-tag">Step %d</span>%s</div>'
            '<h3>%s</h3>%s%s</li>') % (num, fee_html, title, body, extra)

def _ul(items, cols=False):
    return '<ul class="co-bullets%s">%s</ul>' % (" tx-bul2" if cols else "", "".join("<li>%s</li>" % i for i in items))

def _li_check(text):
    return '<div class="tx-check"><div class="ic">%s</div><div><b style="font-weight:500">%s</b></div></div>' % (_CHECK, text)

def _feebox(label, price, note=""):
    return ('<div class="tx-feebox"><div><span>%s</span><b>%s</b></div>%s</div>' % (label, price, ("<p>%s</p>" % note) if note else ""))

transfer_body = """
<section class="tx-hero">
  <div class="container">
    <div class="hp-eyebrow">Treatment &amp; Medication</div>
    <h1>Already diagnosed with ADHD? Transfer your medication care to Rosora</h1>
    <p class="lede">If you are 18 or over and already have an ADHD diagnosis from another provider, Rosora may be able to
    support you with ongoing medication treatment, titration and clinical monitoring.</p>
    __CTA_START__
    <div class="tx-facts">
      <div class="tx-fact"><b>18+</b><span>Adults with an existing ADHD diagnosis</span></div>
      <div class="tx-fact"><b>£50</b><span>Clinical document review</span></div>
      <div class="tx-fact"><b>£295</b><span>Initial transfer appointment</span></div>
      <div class="tx-fact"><b>£150</b><span>Titration / follow-up review</span></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="tx-callouts">
      <div class="tx-callout tx-c1"><h3>Why we review first</h3>
        <p>Before we take over your care, we first need to review your existing diagnostic assessment and relevant medical information. This helps us confirm that we have enough clinical evidence to provide treatment safely and that your previous assessment meets the standards required within the Rosora service.</p></div>
      <div class="tx-callout tx-c2"><h3>No need to start again</h3>
        <p>Already diagnosed does not mean you need to start your assessment again. Where your existing diagnostic evidence is sufficient, you can move directly into our medication transfer pathway.</p></div>
      <div class="tx-callout tx-c3"><h3>Medication is never automatic</h3>
        <p>Medication is not automatically prescribed simply because a previous ADHD diagnosis has been accepted. Your clinician decides whether it is clinically appropriate.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="tx-steps-panel">
      <div class="tx-steps-grid">
        <div class="tx-steps-side">
          <div class="hp-eyebrow">The Process</div>
          <h2>How the Rosora transfer of care process works</h2>
          <p style="color:var(--rosora-navy);margin-bottom:26px">Six clear steps, from submitting your documents to stable treatment and ongoing care.</p>
          __CTA_START__
        </div>
        <ol class="tx-steps">
          __STEPS__
        </ol>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="tx-stable">
      <div>
        <div class="hp-eyebrow" style="color:#8a3a2f">Already stable?</div>
        <h2>Already stable on ADHD medication?</h2>
        <p style="margin-top:14px">If you are already taking ADHD medication and wish to transfer ongoing treatment to Rosora, we still need to complete the document review and clinical transfer appointment.</p>
      </div>
      <div>
        <p style="font-weight:700;color:var(--rosora-teal-deepest)">Your clinician will review:</p>
        __STABLE_LIST__
        <p style="margin-top:14px">If treatment is stable and Rosora is able to accept your care, you may not require a full titration pathway. You will still require appropriate ongoing medication monitoring.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div style="max-width:760px;margin-bottom:30px">
      <div class="hp-eyebrow">Your documents</div>
      <h2>What documents should I upload?</h2>
      <p style="color:var(--rosora-navy);margin:0">To help us review your transfer efficiently, please provide as much relevant information as possible.</p>
    </div>
    <div class="tx-two">
      <div class="tx-info-card"><h3>Essential</h3>__ESSENTIAL__</div>
      <div class="tx-info-card"><h3>Where available</h3>__AVAILABLE__</div>
    </div>
    <p style="margin:22px 0 0;color:var(--rosora-navy);font-weight:600">If anything important is missing, we will let you know.</p>
  </div>
</section>

<section class="section-alt">
  <div class="container tx-two">
    <div>
      <div class="hp-eyebrow">If the answer is not yet</div>
      <h2>What if my previous ADHD assessment is not accepted?</h2>
      <p style="color:var(--rosora-navy)">Rosora has a responsibility to make sure there is sufficient clinical evidence before taking responsibility for ADHD medication treatment.</p>
      <p style="color:var(--rosora-navy)"><b>This does not automatically mean your previous diagnosis is incorrect.</b> It means Rosora requires enough evidence to safely take responsibility for your ongoing treatment.</p>
      <p style="color:var(--rosora-navy);margin:0">Where additional assessment is recommended, we will explain the reasons and any associated costs before you decide whether to proceed.</p>
    </div>
    <div class="tx-info-card">
      <p style="font-weight:700;color:var(--rosora-teal-deepest)">We may recommend further assessment where:</p>
      __NOTACCEPTED__
    </div>
  </div>
</section>

<section>
  <div class="container tx-two">
    <div>
      <div class="hp-eyebrow">Safety</div>
      <h2>Physical health &amp; medication safety</h2>
      <p style="color:var(--rosora-navy)">Before ADHD medication can be initiated or continued, your prescribing clinician will need appropriate physical-health information. This may include:</p>
      <p style="color:var(--rosora-navy);margin:0">Additional information or medical investigations may be requested where clinically indicated.</p>
    </div>
    <div class="tx-check-list">__SAFETY__</div>
  </div>
</section>

<section class="section-alt">
  <div class="container tx-two">
    <div class="tx-info-card">
      <h3>Private prescriptions &amp; medication costs</h3>
      <p>The cost of ADHD medication is separate from your Rosora appointment fee. Medication costs are set by the dispensing pharmacy and can vary depending on:</p>
      __COSTS__
      <p style="margin:14px 0 0">Any Rosora private prescription or administration fee will be clearly explained before treatment begins.</p>
    </div>
    <div class="tx-info-card">
      <h3>Shared care with your NHS GP</h3>
      <p>Once treatment is stable, your clinician may consider whether it is appropriate to approach your GP regarding a shared-care arrangement. Where appropriate, Rosora can provide relevant clinical documentation to support this request.</p>
      <p style="font-weight:700;color:var(--rosora-teal-deepest)">However, shared care cannot be guaranteed.</p>
      <p>Your GP remains responsible for deciding whether they are willing to enter into a shared-care arrangement, taking account of local NHS policies and prescribing arrangements.</p>
      <p style="margin:0">If your GP does not accept shared care, you may continue treatment privately through Rosora where clinically appropriate.</p>
    </div>
  </div>
</section>

<section>
  <div class="container-narrow">
    <div class="hp-eyebrow">Pricing</div>
    <h2>Rosora transfer of care fees</h2>
    <div class="tx-fees" style="margin-top:22px">
      <div class="tx-fee-row head"><span>Service</span><span>Rosora fee</span></div>
      <div class="tx-fee-row"><span class="tx-fee-name">Clinical document review<small>Step 2 — review of your existing diagnostic report</small></span><span class="tx-fee-price">£50</span></div>
      <div class="tx-fee-row"><span class="tx-fee-name">Initial transfer of care medication appointment<small>Step 4 — with a prescribing clinician</small></span><span class="tx-fee-price">£295</span></div>
      <div class="tx-fee-row"><span class="tx-fee-name">Titration / medication follow-up review<small>Step 5 — per review</small></span><span class="tx-fee-price">£150</span></div>
      <div class="tx-fee-row"><span class="tx-fee-name">Annual medication review</span><span class="tx-fee-price">£225</span></div>
      <div class="tx-fee-row"><span class="tx-fee-name">Private prescription administration</span><span class="tx-fee-price">£25</span></div>
      <div class="tx-fee-row"><span class="tx-fee-name">Medication<small>Charged by your dispensing pharmacy, not Rosora</small></span><span class="tx-fee-price alt">Paid separately to pharmacy</span></div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div style="text-align:center;margin-bottom:28px">
      <div class="hp-eyebrow" style="justify-content:center">At a glance</div>
      <h2>Your transfer journey</h2>
    </div>
    <div class="tx-flow">
      <span class="n">Upload documents</span><span class="a">→</span>
      <span class="n">Clinical review</span><span class="a">→</span>
      <span class="n">Transfer decision</span><span class="a">→</span>
      <span class="n">Prescriber appointment</span><span class="a">→</span>
      <span class="n">Medication / titration if required</span><span class="a">→</span>
      <span class="n">Stable treatment</span><span class="a">→</span>
      <span class="n">Ongoing monitoring</span>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="tx-final">
      <div class="hp-eyebrow" style="justify-content:center;color:#CFF8FE">Adults aged 18+</div>
      <h2>Ready to transfer your ADHD care?</h2>
      <p>If you already have an ADHD diagnosis and would like Rosora to consider taking over your medication treatment, start by submitting your diagnostic documentation for clinical review.</p>
      __CTA_FINAL__
    </div>
    <div class="tx-tagline">
      <b>Clear Assessment. Compassionate Care. Greater Understanding.</b>
      <span>Rosora's ADHD medication pathway is informed by NICE NG87: Attention deficit hyperactivity disorder — diagnosis and management.</span>
    </div>
  </div>
</section>
"""

_n = lambda t: '<p class="tx-note">%s</p>' % t

s1 = _step(1, "Submit your documents",
    '<p>Upload your existing ADHD diagnostic report and relevant clinical information securely through the Rosora patient portal.</p><p>We may ask you to provide:</p>'
    + _ul(["Your full ADHD diagnostic report", "Recent clinic letters, where available", "Current or previous ADHD medication information",
           "Current medication list", "Relevant medical history", "Recent blood pressure and pulse readings",
           "Height and weight where clinically appropriate", "Relevant GP or specialist correspondence"], True),
    extra=_n("Secure upload. No live appointment is required at this stage."))
s2 = _step(2, "Clinical document review",
    '<p>A Rosora clinician reviews the information you have provided. The purpose of this review is to determine whether:</p>'
    + _ul(["Your previous ADHD assessment contains sufficient diagnostic evidence", "The diagnosis is adequately documented",
           "Appropriate diagnostic criteria were considered", "Relevant developmental history and functional impairment were assessed",
           "Differential diagnoses and coexisting conditions were appropriately considered",
           "There is sufficient information for Rosora to safely consider taking over medication treatment"])
    + _feebox("Document review fee", "£50", "This is a clinical records review and does not guarantee acceptance for medication treatment. Following the review, we will explain the appropriate next step.")
    + '<div style="margin-top:14px">__CTA_BOOK_REVIEW__</div>',
    fee="£50")
s3 = _step(3, "Receive your clinical review outcome",
    '<p>Once your documents have been reviewed, we will contact you with the outcome. There are usually three possible pathways:</p>'
    '<div class="tx-outcomes">'
    '<div class="tx-outcome"><b>Pathway A — Accepted for transfer of care</b>Your previous diagnostic assessment provides sufficient evidence and you will be invited to book an Initial Transfer of Care Medication Appointment.</div>'
    '<div class="tx-outcome"><b>Pathway B — Further information required</b>We may ask for additional reports, questionnaires, medical information or clarification before a decision can be made.</div>'
    '<div class="tx-outcome"><b>Pathway C — Further ADHD assessment recommended</b>If your previous report does not contain enough information for Rosora to safely rely upon the diagnosis, we may recommend additional assessment or a new ADHD diagnostic assessment.</div>'
    '</div>',
    extra=_n("We will explain why further assessment is required before you decide whether to proceed."))
s4 = _step(4, "Initial transfer of care medication appointment",
    '<p><b>Meet with your prescribing clinician — Adults 18+</b></p>'
    '<p>If your diagnostic review is accepted, you will be invited to attend a comprehensive medication appointment with an appropriate prescribing clinician.</p>'
    + _feebox("Recommended Rosora fee", "£295")
    + '<p style="margin-top:14px">During this appointment, your clinician will review:</p>'
    + _ul(["Your ADHD diagnosis", "Current ADHD symptoms", "Functional difficulties", "Previous ADHD treatment", "Current or previous medication",
           "Medication response and side effects", "Medical history", "Mental health history", "Current medication and potential interactions",
           "Relevant cardiovascular history", "Blood pressure and pulse", "Height and weight where appropriate", "Your treatment preferences", "Your treatment goals"], True)
    + '<p style="margin-top:12px">Your clinician will discuss the available treatment options with you and determine whether ADHD medication is clinically appropriate. Where medication is suitable, an individual treatment plan will be agreed.</p>'
    + '<div style="margin-top:14px">__CTA_BOOK_APPT__</div>',
    fee="£295",
    extra=_n("Medication is not automatically prescribed simply because a previous ADHD diagnosis has been accepted."))
s5 = _step(5, "Medication titration &amp; follow-up",
    '<p>If you are starting ADHD medication, restarting treatment or require a medication adjustment, you may enter the Rosora titration pathway.</p>'
    '<p>Titration is the process of carefully reviewing treatment over time to identify an appropriate medication and dose while monitoring effectiveness and tolerability.</p>'
    + _feebox("Medication follow-up review — recommended Rosora fee", "£150", "per review")
    + '<p style="margin-top:14px">Reviews will normally consider:</p>'
    + _ul(["ADHD symptom response", "Day-to-day functioning", "Medication effectiveness", "Side effects", "Sleep", "Appetite", "Emotional wellbeing",
           "Blood pressure and pulse", "Weight where clinically appropriate", "Treatment adherence", "Any changes in physical or mental health"], True)
    + '<p style="margin-top:12px">Medication may be adjusted where clinically appropriate.</p>',
    fee="£150",
    extra=_n("The number and frequency of appointments will depend on your individual treatment response and clinical needs. Some people require several titration reviews before treatment becomes stable."))
s6 = _step(6, "Stable medication &amp; ongoing care",
    '<p>Once your medication and dose are considered stable, we will discuss your longer-term treatment arrangements. This may include:</p>'
    + _ul(["Continuing private prescribing through Rosora", "Scheduled medication monitoring", "Specialist medication reviews", "Annual medication review",
           "Communication with your GP", "Consideration of shared care where appropriate"]))

transfer_body = (transfer_body
    .replace("__CTA_START__", _cta("Start Your Transfer of Care"))
    .replace("__CTA_FINAL__", _cta("Start My Transfer of Care"))
    .replace("__STEPS__", s1 + s2 + s3 + s4 + s5 + s6)
    .replace("__CTA_BOOK_REVIEW__", _cta("Book Document Review", "contact.html"))
    .replace("__CTA_BOOK_APPT__", _cta("Book Transfer of Care Appointment", "contact.html"))
    .replace("__STABLE_LIST__", _ul(["Your diagnosis", "Current treatment", "Medication response", "Side effects", "Current physical-health monitoring", "Whether your current treatment remains clinically appropriate"]))
    .replace("__ESSENTIAL__", _ul(["Full ADHD diagnostic report", "Current medication list", "Details of current or previous ADHD medication", "Relevant medical history"]))
    .replace("__AVAILABLE__", _ul(["Recent GP summary", "Previous prescribing letters", "Medication review letters", "Previous rating scales", "Relevant mental-health reports",
                                   "Recent blood pressure and pulse", "Height and weight where appropriate", "Relevant investigation results"]))
    .replace("__NOTACCEPTED__", _ul(["The diagnostic report is incomplete", "Important developmental information is missing", "Functional impairment is not adequately documented",
                                     "Diagnostic criteria are unclear", "Differential diagnoses have not been sufficiently considered",
                                     "There are significant changes in your clinical presentation", "The information provided creates uncertainty about the diagnosis",
                                     "Additional clinical information is required for safe treatment"]))
    .replace("__SAFETY__", "".join(_li_check(t) for t in ["Blood pressure", "Pulse", "Height and weight where appropriate", "Cardiovascular history", "Current medication", "Relevant medical conditions"]))
    .replace("__COSTS__", _ul(["Medication", "Strength", "Formulation", "Brand", "Availability", "Pharmacy charges", "Delivery arrangements"], True)))

page("Transfer Your ADHD Medication Care", "Already diagnosed with ADHD? Find out how Rosora can review your existing diagnosis and take over your medication treatment, titration and monitoring.", "medication-transfer.html", transfer_body)


medication_assessment_body = breadcrumb("Medication", "medication.html", "ADHD Medication Assessment") + page_hero(
    "Medication",
    "ADHD Medication Assessment",
    "Following an ADHD diagnosis, a medication assessment considers whether medication may be an "
    "appropriate part of your treatment plan.",
) + bullet_section(
    "What the medication assessment covers",
    [
        "Review of your diagnosis and current difficulties",
        "Relevant health information, including any physical health considerations",
        "Discussion of the options available, including medication and non-medication approaches",
        "A shared decision about whether to proceed with medication",
    ],
) + content_block(
    "What happens next",
    [
        "If medication is agreed as an appropriate next step, your prescriber will discuss options "
        "with you, and — where appropriate — issue a prescription to be dispensed through your "
        "nominated pharmacy, followed by a titration and monitoring period.",
    ],
    alt=True,
)

page("ADHD Medication Assessment", "What happens during an ADHD medication assessment at Rosora.", "medication-assessment.html", medication_assessment_body)


medication_titration_body = breadcrumb("Medication", "medication.html", "Titration & Monitoring") + page_hero(
    "Medication",
    "Titration &amp; Monitoring",
    "Finding the right dose takes time. Titration is the process of adjusting your medication "
    "gradually, with regular review, to find what works best for you.",
) + content_block(
    "What to expect during titration",
    [
        "Your prescriber will start at an appropriate dose and review your response at agreed "
        "intervals, adjusting gradually based on how you're responding and any side effects.",
        "Once a stable, effective dose is reached, monitoring continues on an ongoing basis to make "
        "sure the medication continues to work well for you over time.",
    ],
)

page("Titration & Monitoring", "How ADHD medication titration and ongoing monitoring works.", "medication-titration.html", medication_titration_body)


medication_faqs_body = breadcrumb("Medication", "medication.html", "Medication FAQs") + page_hero(
    "Medication",
    "Medication FAQs",
    "Common questions about ADHD medication, answered plainly.",
) + faq_section(
    "Medication FAQs",
    [
        ("Does Rosora prescribe and dispense medication directly?", "No. Rosora does not hold or dispense medication directly — prescriptions are dispensed through your nominated pharmacy."),
        ("Are shared-care arrangements available with my GP?", "Shared-care arrangements are not currently available through Rosora. We'll update this page if that changes."),
        ("Is medication compulsory after diagnosis?", "No. Medication is one option among several, and the decision is always a shared one between you and your prescriber."),
        ("How often will my medication be reviewed?", "Review frequency depends on your individual titration and monitoring plan, agreed with your prescriber."),
    ],
)

page("Medication FAQs", "Answers to common questions about ADHD medication at Rosora.", "medication-faqs.html", medication_faqs_body)


# ===========================================================================
# WORKPLACE SUPPORT
# ===========================================================================
workplace_body = page_hero(
    "Workplace Support",
    "Workplace Support",
    "Practical, evidence-based support to help you thrive at work — from formal needs assessments "
    "to coaching and guidance for employers.",
) + cards_grid(
    "Our Workplace Services",
    [
        ("🗂️", "Workplace Needs Assessment", "A structured assessment identifying the adjustments and support that could help you at work.", "workplace-needs-assessment.html", "Learn more"),
        ("🏛️", "Access to Work", "Guidance through the UK Government's Access to Work scheme.", "access-to-work.html", "Learn more"),
        ("🎯", "Workplace Coaching", "Ongoing coaching support to apply strategies and adjustments in practice.", "workplace-coaching.html", "Learn more"),
        ("🤝", "Employer Support", "Guidance for employers on supporting neurodivergent staff effectively.", "employer-support.html", "Learn more"),
    ],
    cols=4,
)

page("Workplace Support", "Workplace Needs Assessments, Access to Work guidance, coaching and employer support at Rosora.", "workplace.html", workplace_body)


workplace_needs_body = breadcrumb("Workplace Support", "workplace.html", "Workplace Needs Assessment") + page_hero(
    "Workplace Support",
    "Workplace Needs Assessment",
    "A Workplace Needs Assessment identifies the practical adjustments and support that could help "
    "you perform at your best.",
) + content_block(
    "Who it's for",
    [
        "A Workplace Needs Assessment is for anyone whose ADHD, Autism, or other neurodivergent "
        "profile is affecting them at work — whether you have a formal diagnosis or are exploring "
        "support in parallel with an assessment.",
    ],
) + bullet_section(
    "Areas we may explore",
    [
        "Organisation and planning",
        "Executive functioning",
        "Communication",
        "Workload management",
        "Concentration",
        "Sensory environment",
        "Time management",
        "Assistive technology",
        "Your strengths, and reasonable adjustments that could help",
    ],
    alt=True,
) + pathway(
    "The Journey",
    ["Enquiry", "Consultation", "Needs Assessment", "Recommendations", "Written Report", "Follow-Up if Required"],
) + """<section><div class="container" style="text-align:center;">
<a class="btn btn-primary" href="contact.html">Make a Workplace Enquiry</a>
</div></section>"""

page("Workplace Needs Assessment", "What a Workplace Needs Assessment at Rosora involves, and who it's for.", "workplace-needs-assessment.html", workplace_needs_body)




workplace_coaching_body = breadcrumb("Workplace Support", "workplace.html", "Workplace Coaching") + page_hero(
    "Workplace Support",
    "Workplace Coaching",
    "One-to-one coaching to help you put practical strategies and workplace adjustments into "
    "everyday practice.",
) + content_block(
    "How workplace coaching helps",
    [
        "Workplace coaching takes the recommendations from a needs assessment — or your own "
        "self-identified goals — and works through them practically, session by session, so that "
        "changes actually stick in day-to-day working life.",
    ],
)

page("Workplace Coaching", "One-to-one workplace coaching at Rosora to help put adjustments into practice.", "workplace-coaching.html", workplace_coaching_body)


employer_support_body = breadcrumb("Workplace Support", "workplace.html", "Employer Support") + page_hero(
    "Workplace Support",
    "Employer Support",
    "Practical guidance for employers who want to support neurodivergent staff effectively.",
) + content_block(
    "How we support employers",
    [
        "We work with HR teams and line managers to explain reasonable adjustments in practical "
        "terms, help implement recommendations from a Workplace Needs Assessment, and build "
        "confidence in supporting neurodivergent employees well.",
    ],
)

page("Employer Support", "Guidance for employers on supporting neurodivergent staff, from Rosora.", "employer-support.html", employer_support_body)


# ===========================================================================
# COACHING
# ===========================================================================
coaching_body = page_hero(
    "Coaching",
    "Coaching &amp; Post-Diagnostic Support",
    "Practical, ongoing support to help you apply insight and strategies in everyday life — clearly "
    "separate from diagnostic assessment.",
) + """<section><div class="container-narrow">""" + note(
    "Coaching is a support service, not part of the diagnostic assessment process. Coaching records "
    "are kept separate from any clinical assessment record."
) + "</div></section>" + cards_grid(
    "Our Coaching Services",
    [
        ("🌱", "ADHD, Autism &amp; AuDHD Coaching", "Tailored coaching support for adults navigating ADHD, Autism, or both together. Read about our ADHD coaching.", "adhd-coaching.html", "Learn more"),
        ("🧭", "Executive Function &amp; Wellbeing Coaching", "Practical strategies for organisation, planning and day-to-day wellbeing.", "contact.html", "Enquire"),
        ("💼", "Career &amp; Workplace Coaching", "Support to navigate career decisions and workplace challenges with confidence.", "contact.html", "Enquire"),
        ("❤️", "Relationship Coaching", "Support for relationships affected by ADHD, Autism, or AuDHD-related communication differences.", "contact.html", "Enquire"),
    ],
    cols=4,
    alt=True,
)

page("Coaching", "ADHD, Autism and AuDHD coaching, executive function coaching, career coaching and relationship coaching at Rosora.", "coaching.html", coaching_body)


# ===========================================================================
# FEES
# ===========================================================================
fees_body = page_hero(
    "Fees",
    "Clear, Transparent Fees",
    "We believe in transparent pricing. Every fee below reflects the full assessment or service — "
    "no hidden costs.",
) + """
<section>
  <div class="container grid grid-3">
    <div class="card price-card">
      <span class="eyebrow">Assessment</span>
      <h3>ADHD Assessment</h3>
      <div class="amount">From £795 <span>/ assessment</span></div>
      <ul>
        <li>Pre-assessment information gathering</li>
        <li>Full clinical assessment session</li>
        <li>QbTest/QbCheck where clinically indicated</li>
        <li>Outcome, feedback &amp; written report</li>
      </ul>
      <a class="btn btn-outline btn-block" href="assessment-adhd.html">Learn more</a>
    </div>
    <div class="card price-card">
      <span class="eyebrow">Assessment</span>
      <h3>Autism Assessment</h3>
      <div class="amount">From £995 <span>/ assessment</span></div>
      <ul>
        <li>Pre-assessment information gathering</li>
        <li>Full clinical assessment session(s)</li>
        <li>Informant &amp; supporting evidence review</li>
        <li>Outcome, feedback &amp; written report</li>
      </ul>
      <a class="btn btn-outline btn-block" href="assessment-autism.html">Learn more</a>
    </div>
    <div class="card price-card">
      <span class="eyebrow">Assessment</span>
      <h3>Combined ADHD + Autism</h3>
      <div class="amount">From £1,495 <span>/ assessment</span></div>
      <ul>
        <li>One coordinated intake — no duplication</li>
        <li>Both ADHD and Autism clinical components</li>
        <li>Single formulation &amp; report</li>
        <li>One feedback session for both</li>
      </ul>
      <a class="btn btn-outline btn-block" href="assessment-combined.html">Learn more</a>
    </div>
  </div>
</section>
<section class="section-alt">
  <div class="container grid grid-3">
    <div class="card price-card">
      <span class="eyebrow">Medication</span>
      <h3>Medication Assessment</h3>
      <div class="amount">From £295 <span>/ session</span></div>
      <ul><li>Prescriber review</li><li>Treatment planning</li></ul>
      <a class="btn btn-outline btn-block" href="medication.html">Learn more</a>
    </div>
    <div class="card price-card">
      <span class="eyebrow">Workplace</span>
      <h3>Workplace Needs Assessment</h3>
      <div class="amount">From £495 <span>/ assessment</span></div>
      <ul><li>Consultation &amp; assessment</li><li>Written recommendations report</li></ul>
      <a class="btn btn-outline btn-block" href="workplace-needs-assessment.html">Learn more</a>
    </div>
    <div class="card price-card">
      <span class="eyebrow">Coaching</span>
      <h3>Coaching Sessions</h3>
      <div class="amount">From £95 <span>/ session</span></div>
      <ul><li>One-to-one, tailored sessions</li><li>Flexible packages available</li></ul>
      <a class="btn btn-outline btn-block" href="coaching.html">Learn more</a>
    </div>
  </div>
  <div class="container">
    <p class="price-note" style="margin-top:24px;">Fees shown are indicative starting prices for a local preview build — final pricing, editable by Rosora, will be confirmed and published at launch.</p>
  </div>
</section>
"""

page("Fees", "Clear, transparent fees for ADHD, Autism and Combined assessments, medication support, workplace services and coaching at Rosora.", "fees.html", fees_body)


# ===========================================================================
# RESOURCES & BLOG
# ===========================================================================
resource_categories = [
    "ADHD", "Autism", "AuDHD", "Children &amp; Young People", "Parents &amp; Families",
    "Women &amp; Girls", "Masking / Camouflaging", "Workplace", "Access to Work",
    "Medication", "Coaching", "After Diagnosis", "Preparing for Assessment",
]

resources_body = page_hero(
    "Resources &amp; Blog",
    "Resource Centre",
    "Considered, plain-language articles on ADHD, Autism and life after diagnosis — written to "
    "inform, not overwhelm.",
) + """
<section>
  <div class="container">
    <h2>Browse by Topic</h2>
    <div>""" + "".join('<span class="tag-pill">{}</span>'.format(c) for c in resource_categories) + """</div>
  </div>
</section>
""" + cards_grid(
    "Latest Articles",
    [
        ("📘", "Understanding Adult ADHD", "A plain-language guide to how ADHD can present in adulthood.", "blog.html", "Read"),
        ("🧭", "Preparing for Your Assessment", "What to expect at each stage of your assessment.", "blog.html", "Read"),
        ("👩", "ADHD and Autism in Women &amp; Girls", "Why presentation can look different, and why it's often missed for longer.", "blog.html", "Read"),
    ],
    cols=3,
    alt=True,
) + """<section><div class="container" style="text-align:center;">
<a class="btn btn-outline" href="blog.html">View All Blog Articles</a>
<a class="btn btn-outline" href="faqs.html">View All FAQs</a>
</div></section>"""

page("Resources & Blog", "Articles, guides and FAQs on ADHD, Autism, AuDHD, workplace support and life after diagnosis.", "resources.html", resources_body)


blog_body = breadcrumb("Resources &amp; Blog", "resources.html", "Blog") + page_hero(
    "Blog",
    "Rosora Blog",
    "Considered articles from our clinical and coaching team.",
) + """
<section>
  <div class="container grid grid-3">
    <a class="card blog-card" href="blog-post-private-adhd-assessment-costs.html" style="text-decoration:none;">
      <div class="blog-thumb">💷</div>
      <span class="blog-meta">ADHD · Costs &amp; fees · 5 min read</span>
      <h3>Private ADHD Assessment Costs: What You Need to Know</h3>
      <p>Why it pays to look beyond the advertised price, and what a comprehensive assessment fee should cover.</p>
    </a>
    <a class="card blog-card" href="blog-post-understanding-adult-adhd.html" style="text-decoration:none;">
      <div class="blog-thumb">📘</div>
      <span class="blog-meta">ADHD · 6 min read</span>
      <h3>Understanding Adult ADHD</h3>
      <p>How ADHD can present in adulthood, and what to consider if you recognise yourself in these patterns.</p>
    </a>
    <a class="card blog-card" href="blog-post-preparing-for-assessment.html" style="text-decoration:none;">
      <div class="blog-thumb">🧭</div>
      <span class="blog-meta">Preparing for Assessment · 5 min read</span>
      <h3>Preparing for Your Assessment</h3>
      <p>Practical guidance on what to expect and how to prepare so you feel ready on the day.</p>
    </a>
    <div class="card blog-card">
      <div class="blog-thumb">👩</div>
      <span class="blog-meta">Women &amp; Girls · 7 min read</span>
      <h3>ADHD and Autism in Women &amp; Girls</h3>
      <p>Why presentation can look different, and why diagnosis often comes later in life.</p>
    </div>
    <div class="card blog-card">
      <div class="blog-thumb">👨‍👩‍👧</div>
      <span class="blog-meta">Parents &amp; Families · 6 min read</span>
      <h3>Supporting Your Child Through Assessment</h3>
      <p>How to help your child feel comfortable and prepared throughout the assessment process.</p>
    </div>
    <div class="card blog-card">
      <div class="blog-thumb">🏢</div>
      <span class="blog-meta">Workplace · 4 min read</span>
      <h3>Requesting Workplace Adjustments</h3>
      <p>A practical guide to starting the conversation with your employer.</p>
    </div>
    <div class="card blog-card">
      <div class="blog-thumb">🌿</div>
      <span class="blog-meta">After Diagnosis · 5 min read</span>
      <h3>Life After an ADHD or Autism Diagnosis</h3>
      <p>What tends to help in the weeks and months following diagnosis.</p>
    </div>
  </div>
</section>
"""

page("Blog", "Articles on ADHD, Autism, AuDHD, workplace support, medication and life after diagnosis from Rosora.", "blog.html", blog_body)


def blog_post(slug, title, category, read_time, paragraphs):
    body = breadcrumb("Resources &amp; Blog", "resources.html", title) + """
    <article class="container-narrow" style="padding:48px 0 72px;">
      <span class="eyebrow">{category}</span>
      <h1>{title}</h1>
      <p class="lede">{read_time}</p>
      {content}
      <hr class="divider">
      <p><a class="btn btn-outline" href="blog.html">← Back to Blog</a></p>
    </article>
    """.format(
        category=category, title=title, read_time=read_time,
        content="".join("<p>{}</p>".format(p) for p in paragraphs),
    )
    page(title, title + " — Rosora Blog", slug, body)


blog_post(
    "blog-post-understanding-adult-adhd.html",
    "Understanding Adult ADHD",
    "ADHD",
    "6 minute read",
    [
        "For a long time, ADHD was thought of mainly as something that affects children — and "
        "specifically, boys who struggled to sit still in the classroom. We now understand this was "
        "always too narrow a picture. ADHD is a lifelong neurodevelopmental condition, and many "
        "adults are only now recognising patterns that have been present since childhood.",
        "In adulthood, ADHD doesn't always look like hyperactivity. It might show up as difficulty "
        "with organisation and time management, a tendency to start projects with enthusiasm but "
        "struggle to finish them, restlessness that's more internal than physical, or a pattern of "
        "intense focus on some things and real difficulty with others.",
        "If these patterns sound familiar — and have been present since childhood, even if they "
        "weren't recognised at the time — an assessment can help bring clarity. Our ADHD Assessment "
        "page explains what the process involves, from initial information gathering through to a "
        "clinical assessment and a written outcome.",
    ],
)

blog_post(
    "blog-post-preparing-for-assessment.html",
    "Preparing for Your Assessment",
    "Preparing for Assessment",
    "5 minute read",
    [
        "It's completely normal to feel a mix of relief and nerves ahead of an assessment. Knowing "
        "what to expect can make a real difference.",
        "Before your assessment, it can help to jot down examples of the difficulties you've "
        "experienced — specific situations rather than general impressions — as these are often "
        "easier to discuss on the day. If you're able to involve someone who's known you for a long "
        "time as an informant, their perspective can add real value.",
        "On the day itself, there's no need to prepare a script. Our clinicians will guide the "
        "conversation, and you're welcome to let us know in advance about any reasonable adjustments "
        "that would help — extra processing time, breaks, or anything else that makes the process "
        "more comfortable for you.",
    ],
)


faqs_body = breadcrumb("Resources &amp; Blog", "resources.html", "FAQs") + page_hero(
    "FAQs",
    "Frequently Asked Questions",
    "Answers to the questions we're asked most often.",
) + faq_section(
    "General",
    [
        ("How do I get started?", "Use Start Your Journey to tell us a little about what's brought you here. We'll review your information and be in touch to discuss next steps."),
        ("Can I refer myself?", "Yes — self-referral is welcome, alongside referrals from a GP or another professional."),
        ("What's the difference between a screening tool and a full assessment?", "A screening tool can suggest whether further assessment may be worthwhile, but only a full clinical assessment by a qualified professional can lead to a diagnosis."),
        ("Will I get a written report?", "Yes — every assessment concludes with a feedback session and a written report you can share with your GP or other professionals."),
    ],
) + faq_section(
    "Assessment & Diagnosis",
    [
        ("Do you assess adults and children?", "Yes — see our Adult Assessments and Children & Young People pages for how the process differs."),
        ("What if I need more time or support during the assessment?", "Let us know about any reasonable adjustments you need — see our Patient Preparation resources for examples."),
        ("What happens if the assessment doesn't lead to a diagnosis?", "We'll always give you clear, honest feedback. If more information is needed, we may recommend a Further Information Required step rather than a rushed decision."),
    ],
    alt=True,
)

page("FAQs", "Answers to frequently asked questions about assessment, medication, workplace support and coaching at Rosora.", "faqs.html", faqs_body)


# ===========================================================================
# ABOUT
# ===========================================================================
about_body = page_hero(
    "About",
    "About Rosora",
    "Rosora was founded to make the path from questions to clarity feel a little less daunting — "
    "with clear information, individualised assessment, and a team that explains every step.",
) + content_block(
    "Our Story",
    [
        "Rosora exists because too many people wait too long for answers — often after being told "
        "their difficulties don't quite fit the picture, or after years of self-doubt. We built a "
        "practice around clear communication, individualised clinical assessment, and genuine "
        "ongoing support, not just a diagnosis and a goodbye.",
    ],
) + cards_grid(
    "Learn more about us",
    [
        ("🧭", "Our Approach", "How we think about assessment, and what makes it individualised.", "our-approach.html", "Read more"),
        ("👥", "Meet the Team", "The clinicians and coaches behind Rosora.", "meet-the-team.html", "Meet the team"),
        ("🛡️", "Clinical Standards &amp; Governance", "How we maintain clinical quality and safety.", "clinical-governance.html", "Read more"),
    ],
    cols=3,
    alt=True,
)

page("About", "About Rosora Autism and ADHD Assessment Practice — our story, our approach, and our clinical standards.", "about.html", about_body)


our_approach_body = breadcrumb("About", "about.html", "Our Approach") + page_hero(
    "About",
    "Our Approach",
    "We consider each referral individually — not through a single, fixed checklist.",
) + bullet_section(
    "What individualised assessment means at Rosora",
    [
        "Your developmental history and current functioning are considered as a whole, not reduced to a single score",
        "Assessment tools support clinical judgement — they never replace it",
        "We gather informant and supporting information only where it genuinely adds value",
        "We use 'Further Information Required' rather than rushing to a decision when evidence is incomplete",
        "Every outcome is explained clearly, in a feedback session and in writing",
    ],
)

page("Our Approach", "How Rosora approaches ADHD and Autism assessment — individualised, considered, and clearly explained.", "our-approach.html", our_approach_body)


meet_team_body = breadcrumb("About", "about.html", "Meet the Team") + page_hero(
    "About",
    "Meet the Team",
    "Our clinicians and coaches bring together clinical rigour and genuine warmth.",
) + """
<section>
  <div class="container grid grid-3">
    <div class="card team-card">
      <div class="team-photo">RR</div>
      <h3>Rose Robinson</h3>
      <p style="color:var(--color-accent-dark);font-weight:700;font-size:0.85rem;">Founder</p>
      <p>Leads Rosora's clinical direction and day-to-day practice.</p>
    </div>
    <div class="card team-card">
      <div class="team-photo">Dr</div>
      <h3>Consultant Psychiatrist</h3>
      <p style="color:var(--color-accent-dark);font-weight:700;font-size:0.85rem;">GMC-Registered</p>
      <p>Leads diagnostic assessments and medication reviews.</p>
    </div>
    <div class="card team-card">
      <div class="team-photo">C</div>
      <h3>Neurodiversity Coach</h3>
      <p style="color:var(--color-accent-dark);font-weight:700;font-size:0.85rem;">Coaching Team</p>
      <p>Supports clients with practical, ongoing coaching after diagnosis.</p>
    </div>
  </div>
  <p class="price-note" style="margin-top:24px;text-align:center;">Team profiles shown are placeholders for this local preview — Rosora can add real profiles and photos from the website admin area.</p>
</section>
"""

page("Meet the Team", "Meet the clinicians and coaches behind Rosora Autism and ADHD Assessment Practice.", "meet-the-team.html", meet_team_body)


clinical_gov_body = breadcrumb("About", "about.html", "Clinical Standards & Governance") + page_hero(
    "About",
    "Clinical Standards &amp; Governance",
    "Rosora is committed to safe, high-quality clinical care, underpinned by clear governance.",
) + bullet_section(
    "Our commitments",
    [
        "Assessments are led by appropriately qualified, GMC-registered clinicians",
        "The software and systems we use support the assessment process — they do not make diagnostic decisions",
        "We maintain a documented approach to clinical safety, including escalation where further information is required",
        "Patient data is handled in line with UK GDPR, with data minimisation built into our systems",
        "We welcome feedback and operate a clear complaints process — see our Complaints page",
    ],
)

page("Clinical Standards & Governance", "Rosora's approach to clinical governance, safety and regulatory standards.", "clinical-governance.html", clinical_gov_body)


# ===========================================================================
# CONTACT
# ===========================================================================
contact_body = page_hero(
    "Contact",
    "Get in Touch",
    "Have a question before starting your journey? We're happy to help.",
    cta_label="Start Your Journey",
) + """
<section>
  <div class="container two-col">
    <div>
      <h2>Contact Details</h2>
      <p><strong>Phone:</strong> 0121 000 0000<br>
      <strong>Email:</strong> hello@rosora.co.uk<br>
      <strong>Address:</strong> 262 West Bromwich Road, Walsall, WS5 4NN</p>
      <p class="price-note">Placeholder contact details for this local preview — Rosora to confirm final details before launch.</p>
      <h3 style="margin-top:32px;">Prefer to start your journey directly?</h3>
      <a class="btn btn-primary" href="start-your-journey.html">Start Your Journey</a>
    </div>
    <div class="card">
      <form id="contact-form">
        <div class="form-field"><label for="c-name">Full name</label><input id="c-name" name="name" type="text" required></div>
        <div class="form-field"><label for="c-email">Email address</label><input id="c-email" name="email" type="email" required></div>
        <div class="form-field"><label for="c-message">How can we help?</label><textarea id="c-message" name="message" rows="4" required></textarea></div>
        <button class="btn btn-primary btn-block" type="submit">Send Message</button>
      </form>
      <div class="form-success" id="contact-success">
        <div class="icon">✓</div>
        <h3>Thank you</h3>
        <p>Your message has been received. A member of the Rosora team will be in touch soon.</p>
      </div>
    </div>
  </div>
</section>
"""

page("Contact", "Get in touch with Rosora Autism and ADHD Assessment Practice.", "contact.html", contact_body)


# ===========================================================================
# START YOUR JOURNEY
# ===========================================================================
journey_body = page_hero(
    "Start Your Journey",
    "Start Your Journey",
    "Tell us a little about what's brought you here. We'll review your information and be in touch "
    "to discuss the most appropriate next step — you don't need to book anything yet.",
    cta_label="",
) + """
<section>
  <div class="container-narrow">
    <div class="card">
      <form id="start-journey-form">
        <div class="form-field">
          <label>What service are you enquiring about?</label>
          <div class="radio-cards">
            <label class="radio-card"><input type="radio" name="service" value="adhd" checked> ADHD</label>
            <label class="radio-card"><input type="radio" name="service" value="autism"> Autism</label>
            <label class="radio-card"><input type="radio" name="service" value="combined"> Combined</label>
            <label class="radio-card"><input type="radio" name="service" value="medication"> Medication</label>
            <label class="radio-card"><input type="radio" name="service" value="workplace"> Workplace</label>
            <label class="radio-card"><input type="radio" name="service" value="access-to-work"> Access to Work</label>
            <label class="radio-card"><input type="radio" name="service" value="coaching"> Coaching</label>
            <label class="radio-card"><input type="radio" name="service" value="not-sure"> Not Sure</label>
          </div>
        </div>
        <div class="form-field">
          <label>Who is this enquiry for?</label>
          <div class="radio-cards">
            <label class="radio-card"><input type="radio" name="for" value="self" checked> Myself</label>
            <label class="radio-card"><input type="radio" name="for" value="child"> My Child / a Young Person</label>
            <label class="radio-card"><input type="radio" name="for" value="someone"> Someone I Support</label>
            <label class="radio-card"><input type="radio" name="for" value="professional"> Professional Referral</label>
          </div>
        </div>
        <div class="form-field"><label for="j-name">Full name</label><input id="j-name" type="text" required></div>
        <div class="form-field"><label for="j-email">Email address</label><input id="j-email" type="email" required></div>
        <div class="form-field"><label for="j-phone">Phone number</label><input id="j-phone" type="tel"></div>
        <div class="form-field">
          <label for="j-notes">Anything you'd like us to know? (optional)</label>
          <textarea id="j-notes" rows="3"></textarea>
          <p class="hint">Please only share what feels comfortable — we'll ask for more detail if needed once we're in touch.</p>
        </div>
        <button class="btn btn-primary btn-block" type="submit">Submit</button>
      </form>
      <div class="form-success" id="journey-success">
        <div class="icon">✓</div>
        <h3>Thank you.</h3>
        <p>Your information has been received and will now be reviewed by Rosora. We will contact
           you to discuss the next stage and arrange your assessment appointment.</p>
      </div>
    </div>
  </div>
</section>
"""

page("Start Your Journey", "Start your enquiry with Rosora — tell us a little about what's brought you here and we'll be in touch.", "start-your-journey.html", journey_body)


# ===========================================================================
# PATIENT LOGIN
# ===========================================================================
patient_login_body = page_hero(
    "Patient Login",
    "Patient Login",
    "Rosora's secure patient system — including your appointments, forms, documents and messages "
    "— is hosted securely through our patient management platform, Semble.",
    cta_label="",
) + """
<section>
  <div class="container-narrow" style="text-align:center;">
    <div class="card">
      <div class="card-icon" style="margin:0 auto 18px;">🔒</div>
      <h2>Log in to your secure patient account</h2>
      <p>You'll be taken to Rosora's secure Semble-hosted patient portal to log in.</p>
      <a class="btn btn-primary" href="https://www.semble.io/" target="_blank" rel="noopener">Go to Patient Login →</a>
      <p class="price-note" style="margin-top:18px;">Placeholder link for this local preview — to be replaced with Rosora's live Semble patient login URL.</p>
    </div>
  </div>
</section>
"""

page("Patient Login", "Log in to your secure Rosora patient account, hosted via Semble.", "patient-login.html", patient_login_body)


# ===========================================================================
# ACCESSIBILITY STATEMENT
# ===========================================================================
accessibility_body = page_hero(
    "Accessibility",
    "Accessibility Statement",
    "We want everyone to be able to use this website comfortably, regardless of ability. We're "
    "working towards WCAG 2.2 AA and welcome feedback.",
    cta_label="",
) + content_block(
    "What we've built in",
    [
        "Every page on this site includes an accessibility menu (the ♿ icon in the top right) "
        "offering adjustable text size, a high-contrast mode, wider text spacing, reduced motion, "
        "and highlighted links — your preferences are remembered on this device.",
        "The site is built with keyboard navigation, visible focus indicators, accessible form "
        "labelling and error messages, and a screen-reader-friendly structure in mind, and is "
        "designed to work across mobile, tablet and desktop.",
    ],
) + bullet_section(
    "Our target standard",
    [
        "We are working towards the Web Content Accessibility Guidelines (WCAG) 2.2 AA standard",
        "We test using both automated tools and manual checks, including keyboard-only navigation",
        "If you find something that isn't accessible, please tell us — see Contact",
    ],
    alt=True,
)

page("Accessibility Statement", "Rosora's accessibility statement and the accessibility features built into this website.", "accessibility.html", accessibility_body)


# ===========================================================================
# LEGAL / GOVERNANCE (short template pages)
# ===========================================================================
def legal_page(slug, title, intro, sections):
    body = page_hero("Legal", title, intro, cta_label="")
    for h, p in sections:
        body += content_block(h, [p])
    body += """<section><div class="container-narrow">""" + note(
        "This is placeholder text for a local preview build and does not constitute legal advice. "
        "Rosora should replace this with reviewed, final wording before launch."
    ) + "</div></section>"
    page(title, title + " — Rosora Autism & ADHD Assessment Practice.", slug, body)


legal_page(
    "privacy-policy.html", "Privacy Policy",
    "How Rosora collects, uses and protects your personal information.",
    [("Data we collect", "We collect the information you provide through our enquiry and contact forms, such as your name, contact details and the reason for your enquiry."),
     ("How we use it", "We use this information to respond to your enquiry and, where you proceed with us, as part of your care journey. Clinical data collected as part of an assessment is held within our secure patient system, Semble."),
     ("Your rights", "Under UK GDPR, you have the right to access, correct or request deletion of your personal data. Contact us to exercise these rights.")],
)

legal_page(
    "cookies.html", "Cookie Policy",
    "How this website uses cookies.",
    [("Essential cookies", "Used to remember your accessibility preferences and keep the site working correctly."),
     ("Analytics cookies", "May be used, with your consent, to understand how visitors use the site so we can improve it.")],
)

legal_page(
    "terms.html", "Terms &amp; Conditions",
    "The terms on which you may use this website.",
    [("Use of this website", "This website provides general information about Rosora's services. It is not a substitute for professional clinical advice."),
     ("No diagnosis online", "Nothing on this website constitutes a diagnosis. A diagnosis can only be made following a full clinical assessment.")],
)

legal_page(
    "cancellation-refunds.html", "Cancellation &amp; Refunds Policy",
    "Our approach to appointment cancellations and refunds.",
    [("Cancelling an appointment", "Please contact us as soon as possible if you need to cancel or rearrange an appointment."),
     ("Refunds", "Refund eligibility depends on the notice given and the service booked — see your booking confirmation for specific terms.")],
)

legal_page(
    "complaints.html", "Complaints Procedure",
    "How to raise a concern or complaint with Rosora.",
    [("How to complain", "If you're unhappy with any part of your experience, please contact us directly so we can look into it."),
     ("What happens next", "We aim to acknowledge complaints promptly and respond with the outcome of our review within a reasonable timeframe.")],
)

legal_page(
    "safeguarding.html", "Safeguarding",
    "Rosora's commitment to safeguarding children and vulnerable adults.",
    [("Our commitment", "Rosora takes safeguarding seriously and follows appropriate safeguarding procedures for children and vulnerable adults."),
     ("Raising a concern", "If you have a safeguarding concern, please contact us directly and urgently.")],
)

legal_page(
    "duty-of-candour.html", "Duty of Candour",
    "Our commitment to openness and honesty when things go wrong.",
    [("What this means", "If something goes wrong with your care, we are committed to telling you, apologising, and explaining what will be done in response.")],
)

legal_page(
    "regulatory-status.html", "Regulatory Status",
    "Information about Rosora's regulatory registration.",
    [("Our registration", "Details of Rosora's regulatory registration (e.g. CQC) and clinicians' professional registration numbers (e.g. GMC) will be published here.")],
)



# ===========================================================================
# ADHD TREATMENT & MEDICATION OPTIONS
# ===========================================================================
def _chips(items, cls="tr-chip"):
    return "".join('<li class="%s">%s</li>' % (cls, i) for i in items)

def _checks(items):
    return "".join(_check_item(t, d) if isinstance(t, str) and d is not None else "" for t, d in items)

def _check_plain(text):
    return ('<div class="tx-check"><div class="ic">%s</div><div><b style="font-weight:500">%s</b></div></div>' % (_CHECK, text))

before_items = [
    "Your current ADHD symptoms and how they affect everyday life",
    "Mental health and neurodevelopmental history",
    "Current medication and relevant medical history",
    "Cardiovascular history",
    "Blood pressure and pulse",
    "Height and weight, where appropriate",
    "Potential medication interactions",
    "Risk of substance misuse or medication diversion",
    "Your personal preferences and treatment goals",
]
review_items = [
    "Changes in ADHD symptoms", "Day-to-day functioning", "Side effects", "Sleep and appetite",
    "Blood pressure and pulse", "Weight and other relevant physical health measures",
    "Emotional and mental wellbeing",
]
support_items = [
    ("ADHD psychoeducation", "Developing a better understanding of ADHD and how it affects you."),
    ("Neurodiversity coaching", "Developing practical strategies that work with your individual strengths and needs."),
    ("Executive-function support", "Organisation, planning, prioritising and time management."),
    ("Goal setting", "Turning larger goals into realistic, manageable steps."),
    ("Emotional regulation", "Developing strategies for managing strong emotions and overwhelm."),
    ("Problem-solving strategies", ""),
    ("Sleep and routine support", ""),
    ("Wellbeing and lifestyle strategies", ""),
    ("Confidence and self-esteem", ""),
    ("Workplace or educational strategies", ""),
    ("Reasonable adjustments", ""),
    ("Accountability and maintaining progress", ""),
]
support_cards = "".join(
    '<div class="tr-support c%d"><h3>%s</h3>%s</div>' % ((i % 4) + 1, t, ("<p>%s</p>" % d) if d else "")
    for i, (t, d) in enumerate(support_items)
)

treatment_body = """
<section class="tx-hero">
  <div class="container">
    <div class="hp-eyebrow">Treatment</div>
    <h1>ADHD Treatment &amp; Medication Options</h1>
    <p class="lede">Receiving an ADHD diagnosis can help you better understand your experiences and consider what support may be most helpful for you.</p>
    <p class="lede" style="margin-top:-14px">At Rosora Autism &amp; ADHD Assessment Practice, we personalise treatment recommendations. No single approach is right for everyone.</p>
    __CTA_HERO__
    <p class="hp-nice-note" style="margin-top:22px">Treatment decisions are made in line with relevant NICE guidance (NG87) and appropriate prescribing standards.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="tx-callouts">
      <div class="tx-callout tx-c1"><h3>Personalised, never one-size-fits-all</h3>
        <p>No single approach is right for everyone. Rosora personalises treatment recommendations.</p></div>
      <div class="tx-callout tx-c2"><h3>Discussed before it starts</h3>
        <p>Where ADHD medication is being considered, your clinician will discuss the potential benefits, possible side effects, your preferences and any relevant physical or mental health considerations before treatment is started.</p></div>
      <div class="tx-callout tx-c3"><h3>Guided by NICE</h3>
        <p>Treatment decisions are made in line with relevant NICE guidance (NG87) and appropriate prescribing standards.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container tr-two">
    <div>
      <div class="hp-eyebrow">Medication</div>
      <h2>ADHD Medication</h2>
      <p class="tr-lead">Medication can be an effective treatment option for some people with ADHD. It does not cure ADHD, but for some people it can help reduce core ADHD symptoms and improve day-to-day functioning.</p>
      <p style="color:var(--rosora-navy)">NICE recommends different medication pathways for children, young people and adults. Medication is therefore selected individually rather than using a one-size-fits-all approach.</p>
    </div>
    <div class="tr-med-card">
      <p class="tr-med-intro">Depending on age, individual circumstances, previous treatment response and clinical suitability, medicines used in the treatment of ADHD may include:</p>
      <ul class="tr-chips">
        __MEDS__
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="tr-panel tr-panel-lav">
      <div class="tr-panel-head">
        <div class="hp-eyebrow">Safety first</div>
        <h2>Before starting ADHD medication</h2>
        <p style="color:var(--rosora-navy)">Before prescribing medication, an appropriate clinical assessment is required. This may include consideration of:</p>
      </div>
      <div class="tr-check-cols">__BEFORE__</div>
      <div class="tr-panel-foot">
        <p>Your clinician may request additional physical health information or investigations where clinically indicated.</p>
        <p>Your clinician will explain the proposed treatment and give you an opportunity to discuss any questions or concerns before you decide whether medication is right for you.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container tr-two">
    <div>
      <div class="hp-eyebrow">Ongoing care</div>
      <h2>Medication titration and monitoring</h2>
      <p class="tr-lead">ADHD medication normally requires a period of titration and clinical monitoring.</p>
      <p style="color:var(--rosora-navy)">This means we review treatment carefully to identify an appropriate dose while monitoring effectiveness, tolerability, and any side effects.</p>
      <p class="tx-note" style="border-left:3px solid var(--rosora-lavender-deep);padding-left:14px;color:#3a4466;font-size:.92rem">Medication will only be continued where it remains clinically appropriate.</p>
    </div>
    <div>
      <p class="tr-med-intro" style="margin-bottom:12px"><b>Reviews may consider:</b></p>
      <div class="tx-check-list">__REVIEWS__</div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="tr-panel tr-panel-peach">
      <div class="hp-section-head" style="margin-bottom:30px">
        <div style="max-width:720px">
          <div class="hp-eyebrow" style="color:#8a3a2f">Support</div>
          <h2>Non-medication support</h2>
          <p class="tr-lead" style="margin-bottom:10px">Medication is not the only option for managing ADHD.</p>
          <p style="color:var(--rosora-navy);margin:0">Some people choose not to take medication, while others find that a combination of medication and non-medication strategies works best. Depending on individual needs, support may include:</p>
        </div>
      </div>
      <div class="tr-support-grid">__SUPPORT__</div>
      <p class="tr-closing">Rosora takes a person-centred approach. Recommendations are based on your individual needs rather than assuming that every person with ADHD requires the same treatment.</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="tr-combined">
      <div>
        <div class="hp-eyebrow">Together</div>
        <h2>A combined approach</h2>
        <p class="tr-lead">For many people, ADHD support involves more than one intervention.</p>
        <p style="color:var(--rosora-navy)">A personalised treatment plan might therefore combine appropriate medication with psychoeducation, practical strategies, environmental adjustments and neurodiversity-informed coaching.</p>
        <p style="color:var(--rosora-navy);margin:0">Our aim is to help you understand the available options so you can make treatment decisions collaboratively and safely.</p>
      </div>
      <div class="tr-plus">
        <span class="tr-plus-n">Appropriate medication</span><span class="tr-plus-s">+</span>
        <span class="tr-plus-n">Psychoeducation</span><span class="tr-plus-s">+</span>
        <span class="tr-plus-n">Practical strategies</span><span class="tr-plus-s">+</span>
        <span class="tr-plus-n">Environmental adjustments</span><span class="tr-plus-s">+</span>
        <span class="tr-plus-n">Neurodiversity-informed coaching</span>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="tx-final" style="text-align:left;padding:56px">
      <div class="hp-eyebrow" style="color:#CFF8FE">NHS care</div>
      <h2 style="margin:0 0 14px;max-width:none">NHS care and shared-care agreements</h2>
      <p style="margin:0 0 30px;max-width:760px;color:#b9c6c5">Some people who receive a private ADHD diagnosis may wish to discuss ongoing prescribing with their NHS GP. Where appropriate, Rosora can provide relevant clinical documentation for you and your GP following assessment and treatment.</p>
      <div class="tr-nhs-grid">
        <div class="tr-nhs"><h3>Not automatic</h3><p>A private ADHD diagnosis does not automatically guarantee that an NHS GP will take over prescribing or enter into a shared-care agreement.</p></div>
        <div class="tr-nhs"><h3>The GP decides</h3><p>Shared care is subject to the GP's clinical decision, local NHS policies and the requirements of the relevant NHS commissioning arrangements.</p></div>
        <div class="tr-nhs"><h3>Talk to your GP first</h3><p>We recommend discussing this with your GP before beginning private medication treatment if transferring prescribing to NHS primary care is important to you.</p></div>
        <div class="tr-nhs"><h3>If your GP says no</h3><p>Ongoing prescribing and medication monitoring may need to remain with the appropriate private specialist service, with the associated private costs explained to you in advance.</p></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container-narrow" style="text-align:center">
    <div class="hp-eyebrow" style="justify-content:center">Your choice</div>
    <h2>Making the right decision for you</h2>
    <p class="tr-lead">Starting ADHD medication is an individual decision.</p>
    <p style="color:var(--rosora-navy)">Our role is to provide clear clinical information, discuss appropriate options and support informed decision-making. You will never be expected to choose medication simply because you have received an ADHD diagnosis.</p>
    <p style="color:var(--rosora-navy)">For some people, medication forms an important part of treatment. For others, non-medication strategies or a combination of approaches may be more appropriate. Your treatment should be based on your needs, preferences and clinical circumstances.</p>
    <div style="margin-top:28px">__CTA_FINAL__</div>
    <p class="hp-nice-note" style="margin-top:30px">Rosora's ADHD assessment and treatment pathways are informed by NICE NG87: Attention deficit hyperactivity disorder &ndash; diagnosis and management.</p>
  </div>
</section>
"""

meds = _chips(["Methylphenidate", "Lisdexamfetamine", "Dexamfetamine", "Atomoxetine",
               "Guanfacine<small>where clinically appropriate for children and young people</small>"])
treatment_body = (treatment_body
    .replace("__CTA_HERO__", _cta("Start Your Journey"))
    .replace("__CTA_FINAL__", _cta("Start Your Journey"))
    .replace("__MEDS__", meds)
    .replace("__BEFORE__", "".join(_check_plain(t) for t in before_items))
    .replace("__REVIEWS__", "".join(_check_plain(t) for t in review_items))
    .replace("__SUPPORT__", support_cards))

page("ADHD Treatment & Medication Options", "Personalised ADHD treatment at Rosora: medication options, titration and monitoring, non-medication support and NHS shared-care, informed by NICE NG87.", "adhd-treatment.html", treatment_body)


# ===========================================================================
# ADHD COACHING (sits under Treatment)
# ===========================================================================
def _chip_list(items):
    return "".join('<li>%s</li>' % i for i in items)

def _bul(items):
    return '<ul class="co-bullets">' + "".join("<li>%s</li>" % i for i in items) + "</ul>"

approach = [
    ("Understanding Your ADHD", "<p>Develop a clearer understanding of your individual ADHD profile, including your strengths, challenges, patterns, triggers and support needs.</p>"),
    ("Executive Function Strategies", "<p>Develop practical approaches to:</p>" + _bul(["Planning and prioritising", "Starting and completing tasks", "Organisation", "Working memory", "Time management", "Maintaining attention", "Managing competing demands"])),
    ("Breaking Through Procrastination", "<p>Explore what drives avoidance or difficulty getting started, and develop realistic strategies to build momentum.</p><p>Instead of relying solely on willpower, we look at ways to make tasks more achievable, visible and rewarding.</p>"),
    ("Emotional Regulation", "<p>Learn to recognise emotional patterns, identify triggers and develop strategies for responding to frustration, overwhelm, rejection, stress or impulsive reactions more effectively.</p>"),
    ("Goal Setting and Accountability", "<p>Turn ideas and intentions into manageable actions.</p><p>Together, we can break larger goals into realistic steps, review progress, and adapt strategies when something isn't working.</p>"),
    ("Building Confidence", "<p>ADHD can sometimes affect how people see themselves, particularly after years of struggling with expectations that did not reflect how they think and function.</p><p>Coaching can help you recognise strengths, challenge unhelpful patterns, and build confidence in your ability to manage everyday life.</p>"),
    ("Creating Sustainable Routines", "<p>Rather than expecting you to follow rigid systems, we help you develop routines and structures that fit your lifestyle, responsibilities, and ADHD needs.</p>"),
]
approach_cards = "".join('<div class="co-card t%d"><span class="co-num">%02d</span><h3>%s</h3>%s</div>' % ((i % 4) + 1, i + 1, t, d) for i, (t, d) in enumerate(approach))

help_items = ["Procrastination and getting started", "Organisation and planning", "Time management and time awareness",
    "Maintaining focus and managing distractions", "Completing tasks and projects", "Managing competing priorities",
    "Motivation and consistency", "Emotional regulation", "Impulsivity", "Decision-making", "Sleep and daily routines",
    "Managing paperwork and administration", "Financial organisation", "Setting healthy boundaries", "Confidence and self-esteem",
    "Communication and relationships", "Workplace challenges", "Career development", "Study and education",
    "Managing overwhelm", "Preventing burnout", "Building healthier routines", "Creating better work-life balance"]

work_items = ["Workload management", "Prioritising tasks", "Meeting deadlines", "Managing distractions", "Preparing for meetings",
    "Communication", "Workplace confidence", "Career planning", "Reasonable adjustments",
    "Managing transitions or changes at work", "Preventing overwhelm and burnout"]

journey = [("Understand", "Explore your ADHD experiences, strengths, challenges and recurring patterns."),
    ("Prioritise", "Identify the areas that would make the biggest difference to your daily life."),
    ("Plan", "Create realistic goals and practical strategies."),
    ("Experiment", "Try different approaches and discover what works best for you."),
    ("Review", "Reflect on progress and adjust strategies when needed."),
    ("Build Independence", "Develop tools, confidence, and self-awareness you can keep using beyond coaching.")]
journey_cards = "".join('<li class="co-step"><span>%d</span><div><h3>%s</h3><p>%s</p></div></li>' % (i + 1, t, d) for i, (t, d) in enumerate(journey))

coaching_page = """
<section class="tx-hero">
  <div class="container">
    <div class="hp-eyebrow">Treatment</div>
    <h1>ADHD Coaching That Works With You</h1>
    <p class="lede">ADHD coaching at Rosora is practical, personalised, and focused on making everyday life feel more manageable.</p>
    __CTA__
  </div>
</section>

<section>
  <div class="container tr-two">
    <div>
      <p class="tr-lead">Rather than trying to change who you are, coaching helps you understand how your ADHD affects you, identify what gets in the way, recognise your strengths and develop strategies that work for your life.</p>
      <p style="color:var(--rosora-navy)">The aim is to help you build greater clarity, confidence and consistency while developing strategies you can continue using long after coaching sessions have ended.</p>
    </div>
    <div class="tr-med-card">
      <p class="tr-med-intro">Together, we can explore areas such as:</p>
      <ul class="co-chips">__AREAS__</ul>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="tr-panel tr-panel-lav">
      <div class="co-two">
        <div>
          <div class="hp-eyebrow">Personal to you</div>
          <h2>Coaching designed around your ADHD</h2>
          <p class="tr-lead">ADHD can affect people very differently.</p>
          <p style="color:var(--rosora-navy)">You may know exactly what you need to do but struggle to get started. You may lose track of time, become overwhelmed by competing priorities, act impulsively or find it difficult to maintain routines.</p>
          <p style="color:var(--rosora-navy);margin:0">For others, ADHD may affect confidence, emotional wellbeing, relationships, work or study.</p>
        </div>
        <div class="co-startbox">
          <h3>Rosora coaching begins with your priorities.</h3>
          <p>We work collaboratively to understand what is happening, what you would like to change and what practical strategies are most likely to work for you.</p>
          <p class="co-strong">There is no one-size-fits-all coaching programme.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div style="max-width:760px;margin-bottom:34px">
      <div class="hp-eyebrow">Our approach</div>
      <h2>The Rosora coaching approach</h2>
      <p class="tr-lead" style="margin:0">Our ADHD coaching combines neurodiversity-informed coaching with practical strategies for everyday functioning. Your coaching may include:</p>
    </div>
    <div class="co-grid">__APPROACH__</div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div style="max-width:760px;margin-bottom:30px">
      <div class="hp-eyebrow">Support</div>
      <h2>What can ADHD coaching help with?</h2>
      <p style="color:var(--rosora-navy);margin:0">People come to Rosora with different priorities. Coaching may support you with:</p>
    </div>
    <ul class="co-helpgrid">__HELP__</ul>
  </div>
</section>

<section>
  <div class="container tr-two">
    <div>
      <div class="hp-eyebrow">Work &amp; career</div>
      <h2>ADHD coaching for work and career</h2>
      <p class="tr-lead">ADHD can bring valuable strengths to the workplace, including creativity, energy, problem-solving, innovation and the ability to think differently.</p>
      <p style="color:var(--rosora-navy)">However, difficulties with organisation, deadlines, prioritisation, meetings, workload or maintaining attention can sometimes create additional pressure.</p>
      <p class="tx-note" style="border-left:3px solid var(--rosora-lavender-deep);padding-left:14px;color:#3a4466;font-size:.92rem">Where appropriate, coaching may also complement support provided through <a href="access-to-work.html">Access to Work</a>.</p>
    </div>
    <div>
      <p class="tr-med-intro" style="margin-bottom:12px"><b>Rosora coaching can help you develop strategies around:</b></p>
      <div class="tx-check-list">__WORK__</div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="tr-panel tr-panel-peach">
      <div class="co-two">
        <div>
          <div class="hp-eyebrow" style="color:#8a3a2f">Relationships</div>
          <h2>ADHD and relationships</h2>
          <p class="tr-lead" style="margin:0">ADHD can also influence communication and relationships.</p>
        </div>
        <div>
          <p style="color:var(--rosora-navy)">Differences in attention, emotional regulation, impulsivity, memory, and organisation can sometimes lead to misunderstandings between partners, family members, friends, or colleagues.</p>
          <p style="color:var(--rosora-navy);margin:0">Coaching can help you understand these patterns and develop practical approaches to communication, boundaries, shared responsibilities and relationship wellbeing.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="tx-final" style="text-align:left;padding:56px">
      <div class="hp-eyebrow" style="color:#CFF8FE">A strengths-based approach</div>
      <h2 style="margin:0 0 16px;max-width:none">Progress, not perfection</h2>
      <p style="margin:0 0 12px;max-width:820px;color:#cfdad9">At Rosora, ADHD coaching is not about correcting your personality or expecting you to become someone different.</p>
      <p style="margin:0 0 12px;max-width:820px;color:#cfdad9">It is about understanding how your brain works, recognising what already works well and developing strategies for the areas where you would like more support.</p>
      <p class="co-final-line">We focus on progress, not perfection. The goal is to help you create systems that work with you, not against you.</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div style="max-width:720px;margin-bottom:30px">
      <div class="hp-eyebrow">The process</div>
      <h2>Your coaching journey</h2>
      <p style="color:var(--rosora-navy);margin:0">Your coaching begins by identifying what matters most to you. Together, we can:</p>
    </div>
    <ol class="co-steps">__JOURNEY__</ol>
  </div>
</section>

<section>
  <div class="container-narrow" style="text-align:center">
    <div class="hp-eyebrow" style="justify-content:center">Start where you are</div>
    <h2>Coaching that is personal to you</h2>
    <p class="tr-lead">You do not need to arrive with everything figured out.</p>
    <p style="color:var(--rosora-navy)">You may have one specific challenge you want to work on, or you may simply know that everyday life feels harder than it needs to. We start from where you are and build from there.</p>
    <div style="margin:28px 0 30px">__CTA__</div>
    <p class="tr-lead" style="font-size:1.35rem;margin:0">Understand your ADHD. Build practical strategies. Create change that works for your life.</p>
  </div>
</section>
"""
areas = _chip_list(["Organisation", "Procrastination", "Time management", "Motivation", "Emotional regulation", "Confidence", "Relationships", "Achieving personal or professional goals"])
coaching_page = (coaching_page
    .replace("__CTA__", _cta("Enquire Now", "contact.html"))
    .replace("__AREAS__", areas)
    .replace("__APPROACH__", approach_cards)
    .replace("__HELP__", _chip_list(help_items))
    .replace("__WORK__", "".join(_check_plain(t) for t in work_items))
    .replace("__JOURNEY__", journey_cards))
page("ADHD Coaching", "ADHD coaching at Rosora is practical, personalised and strengths-based: executive function, procrastination, emotional regulation, work, relationships and sustainable routines.", "adhd-coaching.html", coaching_page)


# ===========================================================================
# FREE SCREENING CALL + SCREENER + BOOKING
# ===========================================================================
_ARR2 = '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M3 11L11 3M11 3H4.5M11 3V9.5" stroke="#0C1429" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
_CHK2 = '<svg width="18" height="18" viewBox="0 0 18 18" fill="none" aria-hidden="true"><path d="M4 9.5l3.2 3.2L14 5.8" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def _btn(label, href):
    return '<a class="btn-arrow" href="%s">%s<span class="arr">%s</span></a>' % (href, label, _ARR2)

def _chk(text):
    return '<div class="tx-check"><div class="ic">%s</div><div><b style="font-weight:500">%s</b></div></div>' % (_CHK2, text)

screening_body = """
<section class="tx-hero">
  <div class="container">
    <div class="hp-eyebrow">Free screening call</div>
    <h1>Why we recommend a free screening call</h1>
    <p class="lede">A free Rosora Screening Call can help you understand whether a full Autism, ADHD or combined assessment is the right next step.</p>
    <p class="lede" style="margin-top:-14px;font-weight:600">The aim is to give you clarity before you commit to an assessment.</p>
    __BOOK__
    <p class="hp-nice-note" style="margin-top:22px">Free. No pressure.</p>
  </div>
</section>

__SCREENERS__

<section>
  <div class="container tr-two">
    <div>
      <div class="hp-eyebrow">What a Rosora screening call can help you decide</div>
      <h2>Understand whether assessment is the right next step</h2>
      <p class="tr-lead">The screening call gives you the opportunity to discuss your main concerns, current difficulties and what has led you to consider an Autism or ADHD assessment.</p>
      <p style="color:var(--rosora-navy);margin:0">We can help you understand whether a formal neurodevelopmental assessment may be appropriate, or whether another pathway may be more suitable.</p>
    </div>
    <div class="tr-med-card">
      <div class="hp-eyebrow">Choose the right pathway</div>
      <p class="tr-med-intro">Sometimes it is not immediately clear whether your difficulties are more consistent with ADHD, Autism, or a combination of both. Your screening call can help guide you towards the most appropriate pathway:</p>
      <ul class="tr-chips">
        <li class="tr-chip"><a href="assessment-adhd.html" style="color:inherit;text-decoration:none">ADHD Assessment</a></li>
        <li class="tr-chip"><a href="assessment-autism.html" style="color:inherit;text-decoration:none">Autism Assessment</a></li>
        <li class="tr-chip"><a href="assessment-combined.html" style="color:inherit;text-decoration:none">Combined Autism + ADHD Assessment</a></li>
      </ul>
      <p class="tr-med-intro" style="margin:14px 0 0">This can help you avoid booking an assessment pathway that may not be the best fit for your needs.</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="tr-panel tr-panel-lav">
      <div class="tr-panel-head">
        <div class="hp-eyebrow">Clarify your next steps</div>
        <h2>Ask what matters to you</h2>
        <p style="color:var(--rosora-navy)">You can use the screening call to ask questions about:</p>
      </div>
      <div class="tr-check-cols">__ASK__</div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="sc-free">
      <div>
        <div class="hp-eyebrow" style="color:#CFF8FE">Free screening call</div>
        <h2>There is no charge for the Rosora screening call</h2>
      </div>
      <div>
        <p>The purpose is to help you understand your options and decide on the most appropriate next step before committing to a full assessment.</p>
        <span class="sc-free-price">£0</span>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container-narrow" style="text-align:center">
    <div class="hp-eyebrow" style="justify-content:center">Start with the right pathway</div>
    <h2>You do not need to know exactly which assessment you need</h2>
    <p style="color:var(--rosora-navy)">You do not need to know exactly which assessment you need before contacting Rosora. We can help you understand the available options and guide you towards the pathway that best fits your needs.</p>
    <p class="tr-lead" style="font-size:1.5rem;margin:22px 0 28px">Clear guidance. No pressure. The right next step for you.</p>
    __BOOK__
  </div>
</section>
"""
ask = "".join(_chk(t) for t in ["What the assessment involves", "Which assessment pathway may be most appropriate", "What forms or questionnaires may be required",
    "Whether informant information will be helpful", "What documents you may need to provide", "What happens after assessment",
    "Medication options where relevant", "Post-diagnostic support and coaching"])
screening_body = (screening_body.replace("__BOOK__", _btn("Book Your Free Screening Call", "book-screening-call.html"))
    .replace("__SCREENERS__", screener_cards("For adults")).replace("__ASK__", ask))
page("Free Screening Call", "A free Rosora screening call helps you decide whether a full Autism, ADHD or combined assessment is the right next step. No charge, no pressure.", "free-screening-call.html", screening_body)


# ---------------- Screener ----------------
screener_body = """
<section class="tx-hero" style="padding-bottom:28px">
  <div class="container">
    <div class="hp-eyebrow">Free screener</div>
    <h1 id="sc-title">Start your free screener</h1>
    <p class="lede" id="sc-lede">Choose a screener below. It takes a few minutes, and a member of the Rosora team will call you to offer a free consultation.</p>
  </div>
</section>

<section style="padding-top:20px">
  <div class="container-narrow">
    <div class="sc-switch" role="tablist" aria-label="Choose a screener">
      <a href="screener.html?type=adhd" data-type="adhd" role="tab">ADHD</a>
      <a href="screener.html?type=autism" data-type="autism" role="tab">Autism</a>
      <a href="screener.html?type=audhd" data-type="audhd" role="tab">AuDHD</a>
    </div>

    <form id="sc-form" class="sc-form" novalidate>
      <div class="sc-progress" aria-hidden="true"><span id="sc-bar"></span></div>
      <p class="sc-progress-label" id="sc-count" aria-live="polite">0 of 0 answered</p>

      <div id="sc-step1">
        <fieldset class="sc-questions" id="sc-questions"><legend class="sc-legend">Thinking about the last 6 months&hellip;</legend></fieldset>
        <div class="sc-preview-note"><b>Preview questions.</b> These are placeholder questions for the local build. They are replaced with Rosora's clinically approved screening instrument before launch. A screener does not give a diagnosis and no score is shown.</div>
        <div class="sc-actions"><button type="button" class="btn-arrow sc-next" id="sc-to2" disabled>Continue<span class="arr">__ARROW__</span></button></div>
      </div>

      <div id="sc-step2" hidden>
        <h2 style="font-size:1.8rem;margin-bottom:6px">Where should we send your results?</h2>
        <p style="color:var(--rosora-navy)">Your responses will be sent to your email and to the Rosora team, who will call you to offer a free consultation.</p>
        <div class="form-field"><label for="sc-name">Full name</label><input id="sc-name" name="name" type="text" autocomplete="name" required></div>
        <div class="form-field"><label for="sc-email">Email address</label><input id="sc-email" name="email" type="email" autocomplete="email" required></div>
        <div class="form-field"><label for="sc-phone">Phone number</label><input id="sc-phone" name="phone" type="tel" autocomplete="tel" required><p class="hint">So we can call you for your free consultation.</p></div>
        <label class="sc-consent"><input type="checkbox" id="sc-consent" required> I agree to Rosora using these details to contact me about my screener, as described in the <a href="privacy-policy.html">Privacy Policy</a>.</label>
        <p class="sc-error" id="sc-error" role="alert" hidden></p>
        <div class="sc-actions">
          <button type="button" class="sc-back" id="sc-back">&larr; Back</button>
          <button type="submit" class="btn-arrow">Send my results<span class="arr">__ARROW__</span></button>
        </div>
      </div>
    </form>

    <div id="sc-done" class="sc-done" hidden tabindex="-1">
      <div class="icon">&#10003;</div>
      <h2>Thank you &mdash; your results are on their way</h2>
      <p>We have sent your responses to your email address and to the Rosora team. A member of our team will call you to offer a free consultation and talk through what comes next.</p>
      <p class="small-note">This screener is not a diagnosis. Only a full clinical assessment can lead to a diagnosis.</p>
      __BOOKBTN__
      <p style="margin-top:18px"><a href="free-screening-call.html">Read about the free screening call</a></p>
    </div>
  </div>
</section>

<script>
(function () {
  var Q = {
    adhd: { title: "Start your free ADHD screener", lede: "A few quick questions about attention, focus and organisation.", items: [
      "How often do you find it hard to get started on tasks, even when you know they matter?",
      "How often do you lose track of time or miss deadlines?",
      "How often do you find it hard to stay focused on things that are not interesting to you?",
      "How often do you feel restless or find it hard to sit still?",
      "How often do you act or speak before thinking it through?",
      "How often do you misplace things you need for everyday life?" ] },
    autism: { title: "Start your free Autism screener", lede: "A few quick questions about communication, sensory experience and routine.", items: [
      "How often do you find social situations tiring or hard to read?",
      "How often do changes to plans or routine feel distressing?",
      "How often are you sensitive to noise, light, textures or smells?",
      "How often do you prefer to focus deeply on particular interests?",
      "How often do you rehearse conversations or copy others to fit in?",
      "How often do you find it hard to know what others feel or expect?" ] },
    audhd: { title: "Start your free AuDHD screener", lede: "A short mix of questions covering both ADHD and Autism traits.", items: [
      "How often do you find it hard to get started on tasks, even when you know they matter?",
      "How often do you find it hard to stay focused on things that are not interesting to you?",
      "How often do you act or speak before thinking it through?",
      "How often do you find social situations tiring or hard to read?",
      "How often do changes to plans or routine feel distressing?",
      "How often are you sensitive to noise, light, textures or smells?" ] }
  };
  var OPTS = ["Never", "Rarely", "Sometimes", "Often", "Very often"];
  var type = (new URLSearchParams(location.search).get("type") || "").toLowerCase();
  var form = document.getElementById("sc-form");
  document.querySelectorAll(".sc-switch a").forEach(function (a) { if (a.dataset.type === type) a.classList.add("active"); });
  if (!Q[type]) { form.hidden = true; return; }
  var cfg = Q[type];
  document.getElementById("sc-title").textContent = cfg.title;
  document.getElementById("sc-lede").textContent = cfg.lede + " It takes a few minutes, and a member of the Rosora team will call you to offer a free consultation.";
  document.title = cfg.title + " | Rosora Autism & ADHD Assessment Practice";
  var box = document.getElementById("sc-questions");
  cfg.items.forEach(function (text, i) {
    var q = document.createElement("div"); q.className = "sc-q";
    var html = '<p class="sc-q-text"><span>' + (i + 1) + '</span>' + text + '</p><div class="sc-opts" role="radiogroup" aria-label="Question ' + (i + 1) + '">';
    OPTS.forEach(function (o, k) { html += '<label><input type="radio" name="q' + i + '" value="' + k + '"><span>' + o + '</span></label>'; });
    q.innerHTML = html + "</div>"; box.appendChild(q);
  });
  var total = cfg.items.length, bar = document.getElementById("sc-bar"), count = document.getElementById("sc-count"), next = document.getElementById("sc-to2");
  function update() {
    var n = 0; for (var i = 0; i < total; i++) if (form.querySelector('input[name="q' + i + '"]:checked')) n++;
    bar.style.width = (n / total * 100) + "%"; count.textContent = n + " of " + total + " answered"; next.disabled = n < total;
  }
  form.addEventListener("change", update); update();
  next.addEventListener("click", function () { document.getElementById("sc-step1").hidden = true; document.getElementById("sc-step2").hidden = false; document.getElementById("sc-name").focus(); window.scrollTo({ top: form.offsetTop - 120 }); });
  document.getElementById("sc-back").addEventListener("click", function () { document.getElementById("sc-step2").hidden = true; document.getElementById("sc-step1").hidden = false; });
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var err = document.getElementById("sc-error"), name = form.name.value.trim(), email = form.email.value.trim(), phone = form.phone.value.trim();
    var msg = !name ? "Please enter your name." : !/^\S+@\S+\.\S+$/.test(email) ? "Please enter a valid email address." : !phone ? "Please enter a phone number so we can call you." : !document.getElementById("sc-consent").checked ? "Please tick the box to agree to be contacted." : "";
    if (msg) { err.textContent = msg; err.hidden = false; return; }
    err.hidden = true; form.hidden = true;
    var done = document.getElementById("sc-done"); done.hidden = false; done.focus();
  });
})();
</script>
"""
screener_body = screener_body.replace("__ARROW__", _ARR2).replace("__BOOKBTN__", _btn("Book Your Free Screening Call", "book-screening-call.html"))
page("Free Screener", "Take a free ADHD, Autism or AuDHD screener. Your responses go to your email and to the Rosora team, who will call you for a free consultation.", "screener.html", screener_body)


# ---------------- Booking ----------------
book_body = """
<section class="tx-hero" style="padding-bottom:28px">
  <div class="container">
    <div class="hp-eyebrow">Free screening call</div>
    <h1>Book your free screening call</h1>
    <p class="lede">Tell us when suits you. A member of the Rosora team will call you for a short, free conversation &mdash; no pressure, no commitment.</p>
  </div>
</section>

<section style="padding-top:20px">
  <div class="container-narrow">
    <form id="bk-form" class="sc-form" novalidate>
      <div class="bk-steps" aria-hidden="true"><span class="on">1 &middot; About you</span><span>2 &middot; When suits you</span></div>

      <div id="bk-1">
        <div class="form-field"><label>Who is the call for?</label>
          <div class="radio-cards">
            <label class="radio-card"><input type="radio" name="for" value="me" checked> Me</label>
            <label class="radio-card"><input type="radio" name="for" value="child"> My child / a young person</label>
          </div></div>
        <div class="form-field"><label>Which pathway are you thinking about?</label>
          <div class="radio-cards">
            <label class="radio-card"><input type="radio" name="path" value="adhd"> ADHD</label>
            <label class="radio-card"><input type="radio" name="path" value="autism"> Autism</label>
            <label class="radio-card"><input type="radio" name="path" value="audhd"> AuDHD / both</label>
            <label class="radio-card"><input type="radio" name="path" value="notsure" checked> Not sure yet</label>
          </div></div>
        <div class="form-field"><label for="bk-name">Full name</label><input id="bk-name" name="name" type="text" autocomplete="name" required></div>
        <div class="form-field"><label for="bk-email">Email address</label><input id="bk-email" name="email" type="email" autocomplete="email" required></div>
        <div class="form-field"><label for="bk-phone">Phone number</label><input id="bk-phone" name="phone" type="tel" autocomplete="tel" required></div>
        <p class="sc-error" id="bk-err1" role="alert" hidden></p>
        <div class="sc-actions"><button type="button" class="btn-arrow" id="bk-next">Next<span class="arr">__ARROW__</span></button></div>
      </div>

      <div id="bk-2" hidden>
        <div class="form-field"><label>Preferred days</label>
          <div class="bk-chips" id="bk-days">
            <label><input type="checkbox" name="day" value="Mon"><span>Mon</span></label><label><input type="checkbox" name="day" value="Tue"><span>Tue</span></label>
            <label><input type="checkbox" name="day" value="Wed"><span>Wed</span></label><label><input type="checkbox" name="day" value="Thu"><span>Thu</span></label>
            <label><input type="checkbox" name="day" value="Fri"><span>Fri</span></label><label><input type="checkbox" name="day" value="Sat"><span>Sat</span></label>
          </div></div>
        <div class="form-field"><label>Preferred time</label>
          <div class="radio-cards">
            <label class="radio-card"><input type="radio" name="time" value="Morning (9&ndash;12)" checked> Morning &middot; 9&ndash;12</label>
            <label class="radio-card"><input type="radio" name="time" value="Afternoon (12&ndash;4)"> Afternoon &middot; 12&ndash;4</label>
            <label class="radio-card"><input type="radio" name="time" value="Evening (4&ndash;7)"> Evening &middot; 4&ndash;7</label>
            <label class="radio-card"><input type="radio" name="time" value="Any time"> Any time</label>
          </div></div>
        <div class="form-field"><label for="bk-notes">Anything you would like us to know? (optional)</label><textarea id="bk-notes" name="notes" rows="3"></textarea>
          <p class="hint">Only share what feels comfortable &mdash; you can tell us more on the call.</p></div>
        <label class="sc-consent"><input type="checkbox" id="bk-consent" required> I agree to Rosora contacting me about this call, as described in the <a href="privacy-policy.html">Privacy Policy</a>.</label>
        <p class="sc-error" id="bk-err2" role="alert" hidden></p>
        <div class="sc-actions"><button type="button" class="sc-back" id="bk-back">&larr; Back</button><button type="submit" class="btn-arrow">Request my free call<span class="arr">__ARROW__</span></button></div>
      </div>
    </form>

    <div id="bk-done" class="sc-done" hidden tabindex="-1">
      <div class="icon">&#10003;</div>
      <h2>Thank you &mdash; your call request is in</h2>
      <p id="bk-summary">We will confirm your free screening call by email and phone.</p>
      <p class="small-note">The call is free and there is no obligation to book an assessment.</p>
      <p style="margin-top:14px"><a href="free-screening-call.html">Back to the free screening call page</a></p>
    </div>
  </div>
</section>

<script>
(function () {
  var f = document.getElementById("bk-form"), s1 = document.getElementById("bk-1"), s2 = document.getElementById("bk-2");
  var tabs = document.querySelectorAll(".bk-steps span");
  function show(n) { s1.hidden = n !== 1; s2.hidden = n !== 2; tabs[0].classList.toggle("on", n === 1); tabs[1].classList.toggle("on", n === 2); }
  document.getElementById("bk-next").addEventListener("click", function () {
    var e = document.getElementById("bk-err1"), n = f.name.value.trim(), m = f.email.value.trim(), p = f.phone.value.trim();
    var msg = !n ? "Please enter your name." : !/^\S+@\S+\.\S+$/.test(m) ? "Please enter a valid email address." : !p ? "Please enter a phone number." : "";
    if (msg) { e.textContent = msg; e.hidden = false; return; } e.hidden = true; show(2);
  });
  document.getElementById("bk-back").addEventListener("click", function () { show(1); });
  f.addEventListener("submit", function (ev) {
    ev.preventDefault();
    var e = document.getElementById("bk-err2");
    if (!document.getElementById("bk-consent").checked) { e.textContent = "Please tick the box to agree to be contacted."; e.hidden = false; return; }
    e.hidden = true;
    var days = Array.prototype.map.call(f.querySelectorAll('input[name="day"]:checked'), function (x) { return x.value; });
    var t = f.querySelector('input[name="time"]:checked').value;
    document.getElementById("bk-summary").textContent = "We will call you on " + f.phone.value.trim() + (days.length ? " (" + days.join(", ") + ", " + t + ")" : " (" + t + ")") + " and confirm by email to " + f.email.value.trim() + ".";
    f.hidden = true; var d = document.getElementById("bk-done"); d.hidden = false; d.focus();
  });
})();
</script>
"""
book_body = book_body.replace("__ARROW__", _ARR2)
page("Book a Free Screening Call", "Book your free Rosora screening call in two quick steps. No charge, no pressure.", "book-screening-call.html", book_body)


# ===========================================================================
# ACCESS TO WORK SUPPORT (full page — replaces the short version)
# ===========================================================================
_A = '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M3 11L11 3M11 3H4.5M11 3V9.5" stroke="#0C1429" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
_C = '<svg width="18" height="18" viewBox="0 0 18 18" fill="none" aria-hidden="true"><path d="M4 9.5l3.2 3.2L14 5.8" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def _aw_btn(label, href="contact.html"):
    return '<a class="btn-arrow" href="%s">%s<span class="arr">%s</span></a>' % (href, label, _A)
def _aw_chk(t): return '<div class="tx-check"><div class="ic">%s</div><div><b style="font-weight:500">%s</b></div></div>' % (_C, t)
def _aw_ul(items, cols=False): return '<ul class="co-bullets%s">%s</ul>' % (" tx-bul2" if cols else "", "".join("<li>%s</li>" % i for i in items))
def _aw_chips(items): return '<ul class="co-chips">%s</ul>' % "".join("<li>%s</li>" % i for i in items)
def _aw_grid(items): return '<ul class="co-helpgrid">%s</ul>' % "".join("<li>%s</li>" % i for i in items)
def _aw_cards(items, tint=True):
    return "".join('<div class="co-card t%d"><span class="co-num">%02d</span><h3>%s</h3>%s</div>' % ((i % 4) + 1, i + 1, t, d) for i, (t, d) in enumerate(items))
def _aw_support(items): return "".join('<div class="tr-support c%d"><h3>%s</h3><p>%s</p></div>' % ((i % 4) + 1, t, d) for i, (t, d) in enumerate(items))

aw_conditions = ["ADHD", "Autism", "Dyslexia", "Dyspraxia", "Mental health conditions", "Long-term physical health conditions", "Sensory or physical disabilities", "Other conditions that affect your ability to work"]
aw_affects = ["Planning and prioritising", "Starting tasks", "Completing tasks", "Time awareness", "Meeting deadlines", "Working memory", "Organisation",
    "Managing emails and administration", "Maintaining attention", "Managing distractions", "Switching between tasks", "Emotional regulation", "Communication",
    "Confidence", "Coping with changes or uncertainty", "Managing workload", "Establishing sustainable routines", "Preventing overwhelm or burnout"]
aw_help = [("Specialist workplace support", "<p>Support may be available to help you develop strategies for managing difficulties related to your condition within the workplace.</p>"),
    ("Assistive technology", "<p>Access to Work may recommend specialist software or equipment where this is considered necessary for your role.</p><p>This could include technology that supports organisation, communication, reading, writing or other aspects of workplace functioning.</p>"),
    ("Support workers", "<p>Some individuals may qualify for specialist support, such as a job coach or another type of support worker.</p>"),
    ("Travel support", "<p>Where a disability or health condition means you cannot use your usual form of transport to travel to work, Access to Work may consider additional travel support.</p>"),
    ("Workplace adaptations", "<p>Support may also include certain adaptations or specialist equipment where these are appropriate and are not considered the employer's responsibility as a reasonable adjustment.</p>")]
aw_coach = [("Organisation and planning", "Develop practical systems for managing workload, appointments, tasks, projects and competing priorities."),
    ("Time management", "Build strategies for time awareness, estimating how long tasks will take, meeting deadlines and creating realistic schedules."),
    ("Task initiation", "Understand what makes it difficult to begin certain tasks and develop approaches that help you move from intention into action."),
    ("Prioritisation", "Learn how to distinguish between urgent, important and lower-priority tasks when everything feels equally demanding."),
    ("Focus and distraction", "Develop strategies for protecting attention, reducing unnecessary interruptions and creating working conditions that support concentration."),
    ("Executive functioning", "Explore practical ways to support planning, working memory, organisation, task switching and follow-through."),
    ("Managing procrastination", "Identify patterns behind procrastination and build realistic strategies that reduce avoidance and make tasks easier to approach."),
    ("Emotional regulation", "Develop greater awareness of emotional triggers and practical approaches to managing frustration, overwhelm, workplace pressure and difficult interactions."),
    ("Communication", "Explore ways to communicate your needs clearly, prepare for meetings, manage workplace conversations and reduce misunderstandings."),
    ("Workplace confidence", "Build confidence in recognising your strengths, expressing your needs and making decisions about how you work."),
    ("Reasonable adjustments", "Coaching can help you identify which aspects of your working environment create barriers and consider adjustments that you may wish to discuss with your employer."),
    ("Managing change", "Develop strategies for handling changes to workload, responsibilities, routines, management structures or working environments."),
    ("Preventing overwhelm and burnout", "Recognise early warning signs and develop sustainable ways of managing workload, boundaries, energy and recovery.")]
aw_plan = [("Understand", "Identify your strengths, workplace challenges and the situations where you experience the greatest difficulty."),
    ("Prioritise", "Decide which areas would make the most meaningful difference to your working life."),
    ("Plan", "Develop realistic goals and practical strategies that fit your role."),
    ("Put strategies into practice", "Experiment with tools, systems and approaches in your real working environment."),
    ("Review and adapt", "Review what is helping, what needs changing and how you can continue using the strategies independently.")]
aw_plan_html = "".join('<li class="co-step"><span>%d</span><div><h3>%s</h3><p>%s</p></div></li>' % (i + 1, t, d) for i, (t, d) in enumerate(aw_plan))

def _aw_step(n, title, body, extra=""):
    return '<li class="tx-step"><div class="tx-step-top"><span class="tx-step-tag">Step %d</span></div><h3>%s</h3>%s%s</li>' % (n, title, body, extra)
aw_steps = (
  _aw_step(1, "Identify your workplace needs",
    "<p>Think about the parts of your job that are more difficult because of your condition. Try to identify specific examples.</p>"
    '<div class="aw-quote"><div><span>Instead of</span><p>&ldquo;I struggle with organisation.&rdquo;</p></div>'
    '<div class="yes"><span>You might explain</span><p>&ldquo;I find it difficult to prioritise several competing tasks, which can result in missed deadlines unless I have a clear system for organising and reviewing my workload.&rdquo;</p></div></div>',
    '<p class="tx-note">Specific examples can make it easier to explain the support you need.</p>')
  + _aw_step(2, "Apply to Access to Work",
    '<p>Applications can be made through the official <a href="https://www.gov.uk/access-to-work" target="_blank" rel="noopener">GOV.UK Access to Work service</a>. You may be asked for information about:</p>'
    + _aw_ul(["Your condition or disability", "How it affects your work", "Your job", "Your workplace", "The type of support you believe may help", "Your employer or workplace contact", "Your employment or self-employment details"], True))
  + _aw_step(3, "Discuss your needs", "<p>An Access to Work adviser may contact you to discuss your circumstances and the difficulties you experience at work. Some applicants may also require a workplace assessment.</p>")
  + _aw_step(4, "Receive your decision", "<p>Access to Work will decide what support has been approved and provide details of the award.</p>")
  + _aw_step(5, "Arrange approved support", "<p>Once you have received your award, you can arrange the support in accordance with the terms of your Access to Work agreement.</p>"))

aw_body = """
<section class="tx-hero">
  <div class="container">
    <div class="hp-eyebrow">Access to Work Support</div>
    <h1>Practical workplace support for neurodivergent people</h1>
    <p class="lede">Work can be rewarding, but the way a workplace is organised does not always match the way a neurodivergent person thinks, processes information, communicates or manages attention.</p>
    __ENQUIRE__
  </div>
</section>

<section>
  <div class="container">
    <div class="tx-callouts">
      <div class="tx-callout tx-c1"><h3>Support to start and stay in work</h3><p>If ADHD, Autism, Dyslexia or another health condition affects you at work, Access to Work may be able to provide practical support to help you start work, stay in work and perform your role more effectively.</p></div>
      <div class="tx-callout tx-c2"><h3>Personalised coaching</h3><p>At Rosora, we provide personalised neurodiversity coaching designed to help you understand your working style, develop practical strategies and build greater confidence and independence at work.</p></div>
      <div class="tx-callout tx-c3"><h3>Through your award</h3><p>Where your Access to Work award includes appropriate coaching or specialist support, Rosora may be able to support you with your agreed workplace goals.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container tr-two">
    <div>
      <div class="hp-eyebrow">The programme</div>
      <h2>What is Access to Work?</h2>
      <p class="tr-lead">Access to Work is a UK government programme administered by the Department for Work and Pensions (DWP).</p>
      <p style="color:var(--rosora-navy)">It can provide practical and financial support where a disability, neurodevelopmental difference or health condition creates additional barriers at work.</p>
    </div>
    <div class="tx-check-list">
      __WHAT__
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="tr-panel tr-panel-lav">
      <div class="co-two">
        <div>
          <div class="hp-eyebrow">Eligibility</div>
          <h2>Can I apply if I have ADHD or Autism?</h2>
          <p class="tr-lead">Yes.</p>
          <p style="color:var(--rosora-navy)">Access to Work can support people with a range of conditions and disabilities, including:</p>
          __CONDITIONS__
          <p style="color:var(--rosora-navy);margin:14px 0 0">You usually need to be aged 16 or over and be in paid employment, self-employment, or about to start or return to paid work.</p>
        </div>
        <div class="co-startbox">
          <h3>You do not need a formal diagnosis to apply</h3>
          <p>You do not necessarily need a formal diagnosis to make an Access to Work application.</p>
          <p>The important issue is how your condition or difficulties affect you in your job and what support you need to reduce those barriers.</p>
          <p class="co-strong">A diagnostic or clinical report may sometimes be useful supporting information, but Access to Work determines what information is required for each application.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div style="max-width:780px;margin-bottom:28px">
      <div class="hp-eyebrow">Everyone&rsquo;s experience is different</div>
      <h2>How neurodivergence can affect work</h2>
      <p style="color:var(--rosora-navy);margin:0">For some people, ADHD or another neurodevelopmental difference may affect:</p>
    </div>
    __AFFECTS__
    <div class="tx-two" style="margin-top:26px">
      <p class="tr-lead" style="margin:0">You may be highly capable in your role while still finding particular aspects of the working environment disproportionately difficult.</p>
      <p style="color:var(--rosora-navy);margin:0">The purpose of workplace support is not to change who you are. It is to identify the barriers you experience and develop practical ways of helping you work more effectively.</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div style="max-width:760px;margin-bottom:30px">
      <div class="hp-eyebrow">The support</div>
      <h2>What can Access to Work help with?</h2>
      <p style="color:var(--rosora-navy);margin:0">The support awarded is individually assessed by Access to Work. Depending on your needs and circumstances, support may include areas such as:</p>
    </div>
    <div class="co-grid">__HELP__</div>
    <p class="tx-note" style="margin-top:22px;max-width:620px">Your Access to Work adviser will determine what support can be approved.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="tx-final" style="text-align:left;padding:56px">
      <div class="hp-eyebrow" style="color:#CFF8FE">Coaching through Rosora</div>
      <h2 style="margin:0 0 16px;max-width:none">Neurodiversity coaching through Rosora</h2>
      <p style="margin:0 0 12px;max-width:820px;color:#cfdad9">If coaching or specialist strategy support forms part of your Access to Work award, Rosora can work with you to translate your workplace challenges into practical, achievable strategies.</p>
      <p style="margin:0 0 12px;max-width:820px;color:#cfdad9">Our approach is collaborative, strengths-based and neurodiversity-informed. We focus on helping you understand how you work best rather than expecting you to fit into one standard way of working.</p>
      <p class="co-final-line">Your coaching programme is built around your individual workplace needs and agreed goals.</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div style="max-width:760px;margin-bottom:30px">
      <div class="hp-eyebrow">Workplace coaching</div>
      <h2>What can Rosora workplace coaching help with?</h2>
      <p style="color:var(--rosora-navy);margin:0">Depending on your needs, your coaching sessions may focus on:</p>
    </div>
    <div class="tr-support-grid">__COACH__</div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div style="max-width:720px;margin-bottom:30px">
      <div class="hp-eyebrow">The process</div>
      <h2>Your Rosora workplace coaching plan</h2>
      <p style="color:var(--rosora-navy);margin:0">Your coaching begins with understanding what is currently happening at work and what you would like to improve. Together, we may work through five stages:</p>
    </div>
    <ol class="co-steps">__PLAN__</ol>
    <p class="tr-lead" style="margin:26px 0 0;font-size:1.25rem">The aim is to build sustainable skills rather than create dependence on coaching.</p>
  </div>
</section>

<section>
  <div class="container">
    <div style="max-width:780px;margin-bottom:30px">
      <div class="hp-eyebrow">Know the difference</div>
      <h2>Access to Work and reasonable adjustments are different</h2>
      <p style="color:var(--rosora-navy);margin:0">Access to Work and reasonable adjustments are related, but they are not the same thing.</p>
    </div>
    <div class="tx-two">
      <div class="tx-info-card">
        <h3>Reasonable adjustments</h3>
        <p>Under the Equality Act 2010, employers may have a legal duty to make reasonable adjustments where a disabled employee would otherwise experience a substantial disadvantage. Examples might include:</p>
        __ADJ__
        <p style="margin:14px 0 0">What is considered reasonable depends on the individual circumstances.</p>
      </div>
      <div>
        <div class="tx-info-card" style="margin-bottom:20px">
          <h3>Access to Work</h3>
          <p style="margin:0">Access to Work is a government programme that may provide funding for additional specialist support beyond adjustments that an employer would reasonably be expected to provide. Access to Work will decide what support is eligible for funding.</p>
        </div>
        <div class="tx-info-card" style="background:var(--rosora-teal-tint);border-color:transparent">
          <h3>NICE guidance and workplace support</h3>
          <p>NICE guidance for ADHD recognises the importance of considering how ADHD affects employment and recommends appropriate environmental modifications to reduce the impact of symptoms.</p>
          <p style="margin:0">Environmental modifications can include changes that reduce distractions, improve structure and make information or tasks easier to manage. Rosora&rsquo;s coaching approach complements this principle by helping individuals identify practical strategies and workplace changes that reflect their individual needs.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="tx-steps-panel">
      <div class="tx-steps-grid">
        <div class="tx-steps-side">
          <div class="hp-eyebrow">How to apply</div>
          <h2>How to apply for Access to Work</h2>
          <p style="color:var(--rosora-navy);margin-bottom:26px">You normally apply directly to Access to Work yourself. The process generally involves:</p>
          <a class="btn-arrow" href="https://www.gov.uk/access-to-work" target="_blank" rel="noopener">Go to GOV.UK<span class="arr">__ARROW__</span></a>
        </div>
        <ol class="tx-steps">__STEPS__</ol>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container tr-two">
    <div>
      <div class="hp-eyebrow">Get ready</div>
      <h2>Preparing for your Access to Work conversation</h2>
      <p style="color:var(--rosora-navy)">It can help to think about your needs before speaking with an Access to Work adviser. Consider:</p>
      <p class="tr-lead" style="margin:0">Focus on your functional needs, rather than feeling that you need to prove how severe your diagnosis is.</p>
    </div>
    <div class="tx-check-list">__PREP__</div>
  </div>
</section>

<section class="section-alt">
  <div class="container tr-two">
    <div>
      <div class="hp-eyebrow">Working for yourself</div>
      <h2>Access to Work if you are self-employed</h2>
      <p style="color:var(--rosora-navy)">Self-employed people may also be eligible for Access to Work, subject to the programme&rsquo;s eligibility requirements. Support may be particularly useful where neurodivergence affects areas such as:</p>
      <p class="tx-note" style="border-left:3px solid var(--rosora-lavender-deep);padding-left:14px;color:#3a4466;font-size:.92rem;margin:0">Check the current eligibility requirements directly with Access to Work before applying.</p>
    </div>
    <div class="tx-info-card">__SELF__</div>
  </div>
</section>

<section>
  <div class="container tx-two">
    <div class="tx-info-card">
      <h3>Do I need to tell my employer?</h3>
      <p>You do not have to disclose every aspect of your medical history to your employer.</p>
      <p>However, where workplace support needs to be arranged, Access to Work may need to involve your employer or workplace contact, with the appropriate permissions.</p>
      <p style="margin:0">If you are unsure about disclosure, Rosora coaching can help you think through how you would like to communicate your needs professionally and confidently.</p>
    </div>
    <div class="tx-info-card">
      <h3>What Access to Work does not replace</h3>
      <p>Access to Work is workplace support. It does not replace:</p>
      __NOTREPLACE__
      <p style="margin:14px 0 0">If you are looking for an Autism or ADHD assessment, this should be considered separately from an Access to Work application. See our <a href="assessment-adults.html">adult assessments</a>.</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="tr-panel tr-panel-peach">
      <div class="hp-section-head" style="margin-bottom:26px">
        <div style="max-width:760px">
          <div class="hp-eyebrow" style="color:#8a3a2f">How Rosora can support you</div>
          <h2>Coaching focused on everyday working life</h2>
          <p style="color:var(--rosora-navy);margin:0">Rosora provides neurodiversity-informed coaching focused on the practical challenges that can arise in everyday working life. We can help you:</p>
        </div>
      </div>
      __SUPPORT__
      <p class="tr-closing">Our aim is not to tell you how you should work. It is to help you discover what helps you work at your best.</p>
    </div>
  </div>
</section>

<section>
  <div class="container tr-two">
    <div class="tr-med-card">
      <div class="hp-eyebrow">Already have an award?</div>
      <h2 style="font-size:1.9rem">Already have an Access to Work award?</h2>
      <p class="tr-med-intro">If your Access to Work award includes coaching or relevant specialist support, you can contact Rosora to discuss your award and the goals you would like to work on.</p>
      <p class="tr-med-intro">We can review the type of support approved and determine whether Rosora&rsquo;s coaching service is appropriate for your needs.</p>
      <p class="co-strong" style="color:var(--rosora-teal-deepest)">Have your Access to Work award letter available when you contact us.</p>
    </div>
    <div style="text-align:center;align-self:center">
      <div class="hp-eyebrow" style="justify-content:center">Start with your strengths</div>
      <h2>Start with your strengths. Build strategies that work.</h2>
      <p style="color:var(--rosora-navy)">You do not need to force yourself into a working style that does not suit you. With the right understanding, practical strategies and workplace support, it is possible to create a more sustainable way of working.</p>
      <p class="tr-lead" style="font-size:1.3rem">Understand how you work. Build practical strategies. Work with greater clarity and confidence.</p>
      <div style="margin-top:20px">__ENQUIRE__</div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="aw-review">
      <div class="aw-avatar" aria-hidden="true">RR</div>
      <div>
        <div class="hp-eyebrow">Clinically reviewed by</div>
        <h3>Rose Robinson, Registered Mental Health Nurse (NMC)</h3>
        <p class="aw-role">Neurodevelopmental Assessor &nbsp;|&nbsp; Clinical Reviewer &nbsp;|&nbsp; Founder of Rosora</p>
        <p>Rose Robinson is an NMC-registered Mental Health Nurse with extensive clinical experience supporting children, young people and adults with mental health and neurodevelopmental needs.</p>
        <p>She has specialist training and experience in ADHD and Autism assessment, including using recognised assessment tools and structured clinical approaches. Her work is informed by current NICE guidance, evidence-based practice and recognised diagnostic standards.</p>
        <p>At Rosora Autism &amp; ADHD Assessment Practice, Rose contributes to clinical assessment, formulation, quality assurance, and the review of patient information to help ensure services remain person-centred, clinically robust, and evidence-informed.</p>
        <p style="margin:0">Her approach combines professional clinical experience with a strong understanding of neurodiversity, ensuring that individuals are supported with respect, clarity and compassion throughout their assessment journey.</p>
      </div>
    </div>
  </div>
</section>
"""
aw_body = (aw_body
    .replace("__ENQUIRE__", _aw_btn("Enquire About Access to Work Coaching"))
    .replace("__ARROW__", _A)
    .replace("__WHAT__", "".join(_aw_chk(t) for t in ["The support available depends on your individual circumstances, your job and the difficulties you experience in carrying out your role.",
        "Access to Work is separate from the reasonable adjustments that an employer may have a legal responsibility to provide."]))
    .replace("__CONDITIONS__", _aw_chips(aw_conditions))
    .replace("__AFFECTS__", _aw_grid(aw_affects))
    .replace("__HELP__", _aw_cards(aw_help))
    .replace("__COACH__", _aw_support(aw_coach))
    .replace("__PLAN__", aw_plan_html)
    .replace("__ADJ__", _aw_ul(["Providing written as well as verbal instructions", "Reducing unnecessary distractions", "Providing a quieter place to work", "Adjusting working arrangements", "Allowing appropriate breaks", "Changing how information is presented", "Providing additional structure or check-ins"]))
    .replace("__STEPS__", aw_steps)
    .replace("__PREP__", "".join(_aw_chk(t) for t in ["Which parts of your job are most difficult?", "What happens when those difficulties occur?", "How often do they happen?",
        "How do they affect your productivity or wellbeing?", "What have you already tried?", "What helps?", "What does not help?",
        "Are there particular environments or situations where things become harder?", "Would structured specialist support help you develop sustainable strategies?"]))
    .replace("__SELF__", _aw_ul(["Managing workload", "Business administration", "Planning", "Scheduling", "Prioritisation", "Invoicing and paperwork", "Client communication", "Maintaining routines", "Separating work and personal time", "Managing multiple projects"], True))
    .replace("__NOTREPLACE__", _aw_ul(["A clinical ADHD or Autism assessment", "Medical treatment", "ADHD medication", "Psychological therapy", "Your employer's responsibility to consider reasonable adjustments"]))
    .replace("__SUPPORT__", _aw_grid(["Understand your working style", "Identify strengths and barriers", "Build executive-function strategies", "Improve organisation and planning",
        "Develop sustainable routines", "Manage competing priorities", "Work on procrastination and task initiation", "Strengthen workplace communication", "Develop confidence",
        "Explore reasonable adjustments", "Improve work-life balance", "Reduce overwhelm", "Build strategies you can continue using independently"])))
page("Access to Work Support", "Practical workplace support for neurodivergent people: what Access to Work is, who can apply, how to apply, and how Rosora workplace coaching can help.", "access-to-work.html", aw_body)


# ===========================================================================
# BLOG ARTICLE — Private ADHD Assessment Costs
# ===========================================================================
_AA = '<svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M3 11L11 3M11 3H4.5M11 3V9.5" stroke="#0C1429" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
_CC = '<svg width="18" height="18" viewBox="0 0 18 18" fill="none" aria-hidden="true"><path d="M4 9.5l3.2 3.2L14 5.8" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def _art_btn(label, href, light=False):
    return '<a class="btn-arrow%s" href="%s">%s<span class="arr">%s</span></a>' % (" btn-arrow-light" if light else "", href, label, _AA)
def _art_checks(items): return '<div class="tx-check-list art-list">%s</div>' % "".join('<div class="tx-check"><div class="ic">%s</div><div><b style="font-weight:500">%s</b></div></div>' % (_CC, t) for t in items)

art_include = ["Pre-assessment questionnaires", "A detailed clinical and developmental history", "Exploration of ADHD symptoms in childhood and adulthood",
    "Assessment of how symptoms affect everyday functioning", "Relevant information from a family member, partner, school or other informant where appropriate",
    "Mental and physical health history", "Consideration of other possible or co-existing conditions", "A structured ADHD diagnostic interview",
    "Clinical formulation and diagnostic decision", "Feedback about the outcome", "A comprehensive written report"]
art_cover = ["What is included within your assessment", "Whether your diagnostic report is included", "Whether further information may be required",
    "Any separate medication or treatment costs", "Follow-up options after your assessment"]
art_choose = ["The qualifications and experience of the clinician", "The depth of the assessment", "Whether childhood and current symptoms are considered",
    "Whether functional impairment is assessed", "Whether other conditions are considered", "Whether informant information is used where appropriate",
    "Whether a written report is included", "What support is available following the assessment"]

article = """
<div class="container"><p class="breadcrumb"><a href="index.html">Home</a> / <a href="blog.html">Blog</a> / <b>Private ADHD Assessment Costs: What You Need to Know</b></p></div>
<article class="art">
  <header class="art-head">
    <div class="hp-tag-row" style="justify-content:center"><span class="hp-tag-pill">ADHD</span><span class="hp-tag-pill">Costs &amp; fees</span><span class="hp-tag-pill">Choosing an assessment</span></div>
    <h1>Private ADHD Assessment Costs: What You Need to Know</h1>
    <p class="art-by">By the Rosora team &nbsp;&bull;&nbsp; 5 min read</p>
  </header>
  <div class="container"><div class="art-hero"><img src="__HERO__" alt="A clinician talking with a client during an assessment" loading="eager"></div></div>

  <div class="art-body">
    <p class="art-lead">When choosing a private ADHD assessment, it is important to look beyond the advertised price. Assessment fees can vary depending on the clinician involved, the assessment process, the information collected and what is included after your appointment.</p>

    <h2>What should an ADHD assessment include?</h2>
    <p>A comprehensive ADHD assessment should consider more than symptoms alone. At Rosora, the assessment process may include:</p>
    __INCLUDE__

    <h2>What does the assessment fee cover?</h2>
    <p>Before booking, you should know exactly what is included in the price. Rosora aims to provide clear information about:</p>
    __COVER__
    <div class="art-callout"><p>Assessment and medication treatment are separate clinical services and any additional charges will be explained clearly.</p></div>

    <h2>Does paying for an assessment guarantee an ADHD diagnosis?</h2>
    <p class="art-no">No.</p>
    <p>Paying for an assessment gives you access to a professional diagnostic assessment. It does not guarantee a diagnosis.</p>
    <p>The purpose of the assessment is to determine whether the clinical evidence supports ADHD after considering your developmental history, symptoms, functional difficulties and other possible explanations.</p>
    <p><b>Possible outcomes may include:</b></p>
    <div class="art-outcomes">
      <div class="o1"><span>1</span>ADHD diagnostic criteria are met</div>
      <div class="o2"><span>2</span>ADHD diagnostic criteria are not met</div>
      <div class="o3"><span>3</span>Further information is required before a decision can be reached</div>
    </div>
    <p>Whatever the outcome, we will explain the findings and recommended next steps.</p>

    <h2>Choosing an ADHD assessment</h2>
    <p>When comparing providers, consider:</p>
    __CHOOSE__
    <p>At Rosora Autism and ADHD Assessment Practice, our aim is to provide a clear, thorough and person-centred assessment pathway with transparent information about what you are paying for.</p>
  </div>

  <div class="container"><div class="art-cta">
    <div class="hp-eyebrow" style="justify-content:center;color:#CFF8FE">Next step</div>
    <h2>Ready to take the next step?</h2>
    <p>Explore our ADHD Assessment pathway or complete our initial ADHD screening before deciding whether a full assessment is right for you.</p>
    <div class="art-cta-btns">__BTN1__ __BTN2__</div>
  </div></div>

  <div class="container art-more">
    <h2>You might also like</h2>
    <div class="grid grid-3">
      <a class="hp-blog-card" href="blog-post-understanding-adult-adhd.html"><div class="hp-blog-thumb"><img src="__R1__" alt="" loading="lazy"></div><div class="hp-tag-row"><span class="hp-tag-pill">ADHD</span></div><h3>Understanding Adult ADHD</h3></a>
      <a class="hp-blog-card" href="blog-post-preparing-for-assessment.html"><div class="hp-blog-thumb"><img src="__R2__" alt="" loading="lazy"></div><div class="hp-tag-row"><span class="hp-tag-pill">Preparing for Assessment</span></div><h3>Preparing for Your Assessment</h3></a>
      <a class="hp-blog-card" href="fees.html"><div class="hp-blog-thumb"><img src="__R3__" alt="" loading="lazy"></div><div class="hp-tag-row"><span class="hp-tag-pill">Fees</span></div><h3>Our transparent fees</h3></a>
    </div>
  </div>
</article>
"""
article = (article.replace("__HERO__", img("rosora-article-costs", 1200, 560))
    .replace("__INCLUDE__", _art_checks(art_include)).replace("__COVER__", _art_checks(art_cover)).replace("__CHOOSE__", _art_checks(art_choose))
    .replace("__BTN1__", _art_btn("Explore ADHD Assessment", "assessment-adhd.html"))
    .replace("__BTN2__", _art_btn("Start Your Free ADHD Screener", "screener.html?type=adhd", True))
    .replace("__R1__", img("rosora-blog-1", 500, 340)).replace("__R2__", img("rosora-blog-2", 500, 340)).replace("__R3__", img("rosora-blog-3", 500, 340)))
page("Private ADHD Assessment Costs: What You Need to Know", "Why it pays to look beyond the advertised price of a private ADHD assessment: what a comprehensive assessment includes, what the fee should cover, and how to choose.", "blog-post-private-adhd-assessment-costs.html", article)

# ---------------------------------------------------------------------------
# Make medication-transfer.html fully self-contained (CSS + JS inlined)
# ---------------------------------------------------------------------------
def inline_assets(slug):
    path = os.path.join(ROOT, slug)
    html = open(path, encoding="utf-8").read()
    css = open(os.path.join(ROOT, "css", "style.css"), encoding="utf-8").read()
    js = open(os.path.join(ROOT, "js", "main.js"), encoding="utf-8").read().replace("</script>", "<\\/script>")
    html = html.replace('<link rel="stylesheet" href="css/style.css">', "<style>\n" + css + "\n</style>")
    html = html.replace('<script src="js/main.js"></script>', "<script>\n" + js + "\n</script>")
    open(path, "w", encoding="utf-8").write(html)

inline_assets("medication-transfer.html")

print("All pages generated.")
