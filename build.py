#!/usr/bin/env python3
"""Builds the Life Builders static site into ./site from the page content below."""
import os, html, pathlib

SITE = pathlib.Path(__file__).parent / "site"
GIVE_URL = "https://givebutter.com/untitled-campaign-egsgrx"  # update when the campaign slug is renamed
CONTACT_EMAIL = "preston@saintscrown.com"

NAV = [("", "Home"), ("about/", "Our Story"), ("mentorship/", "Mentorship"),
       ("story/", "Share Your Story"), ("impact/", "Impact")]


def page(path, title, description, body, active):
    depth = path.count("/")
    root = "../" * depth
    nav = "".join(
        f'<a href="{root}{href}"{" class=\"active\"" if href == active else ""}>{label}</a>'
        for href, label in NAV)
    out = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:image" content="https://lifebuilders.net/assets/img/logo.png">
<link rel="icon" type="image/png" href="{root}assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Source+Serif+4:opsz,wght@8..60,700;8..60,900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/site.css">
</head>
<body>
<header class="site-header">
  <div class="wrap header-row">
    <a class="brand" href="{root}"><img src="{root}assets/img/shield.png" alt="" width="34" height="50"><span>Life Builders</span></a>
    <input type="checkbox" id="menu" class="menu-toggle" aria-label="Open menu">
    <label for="menu" class="menu-button" aria-hidden="true"><span></span><span></span><span></span></label>
    <nav class="site-nav">{nav}<a class="btn btn-gold btn-sm" href="{root}give/">Give</a></nav>
  </div>
</header>
<main>
{body.replace("{root}", root)}
</main>
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <img class="footer-logo" src="{root}assets/img/logo-light.png" alt="Life Builders: Build the man. Strengthen the family. Change the legacy." width="220">
    </div>
    <div>
      <p class="eyebrow light">Explore</p>
      <ul class="footer-links">
        <li><a href="{root}about/">Our Story</a></li>
        <li><a href="{root}mentorship/">Mentorship</a></li>
        <li><a href="{root}story/">Share Your Story</a></li>
        <li><a href="{root}impact/">Impact</a></li>
        <li><a href="{root}give/">Give</a></li>
      </ul>
    </div>
    <div>
      <p class="eyebrow light">Contact</p>
      <p>Preston Woody, Founder and President<br><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a><br>Fort Worth, Texas</p>
    </div>
  </div>
  <div class="wrap legal">
    <p>Life Builders is a ministry of Preston Woody Foundation Corporation, a 501(c)(3) public charity. EIN 42-3136909. Contributions are tax-deductible to the extent allowed by law.</p>
    <p>&copy; 2026 Preston Woody Foundation Corporation. Build the man. Strengthen the family. Change the legacy.</p>
  </div>
</footer>
</body>
</html>
"""
    dest = SITE / path / "index.html" if path else SITE / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(out)


PATHWAY = """
<section class="section">
  <div class="wrap">
    <p class="eyebrow center">One connected pathway</p>
    <h2 class="center">From reach to generational impact</h2>
    <p class="lede center narrow">Every gift funds one connected mission, not one isolated program. A message reaches a man, truth roots him, mentorship equips him, and his family is strengthened.</p>
    <ol class="pathway">
      <li><span class="num">1</span><p class="eyebrow">Reach</p><p class="big">100,000</p><p>people reached through 16 episodes of The Standard</p></li>
      <li><span class="num">2</span><p class="eyebrow">Root</p><p class="big">Bible plan</p><p>truth becomes a daily rhythm</p></li>
      <li><span class="num">3</span><p class="eyebrow">Open access</p><p class="big">30 to 40</p><p>men sponsored through mentorship and transformational experiences</p></li>
      <li><span class="num">4</span><p class="eyebrow">Equip</p><p class="big">3 mentors</p><p>trained to guide lasting change</p></li>
      <li><span class="num">5</span><p class="eyebrow">Multiply</p><p class="big">Generations</p><p>stronger men strengthen marriages, children, churches and communities</p></li>
    </ol>
    <p class="fineprint center">First-year targets. We will report verified results as the pathway launches.</p>
  </div>
</section>
"""

GIVE_BAND = """
<section class="band navy">
  <div class="wrap band-row">
    <div>
      <p class="eyebrow light">Unrestricted donor support</p>
      <h2>Help us build the first men, families and legacies.</h2>
      <p>Your gift removes the financial barrier for men who are ready to change but can't afford the help.</p>
    </div>
    <div class="band-actions"><a class="btn btn-gold" href="{root}give/">Give now</a></div>
  </div>
</section>
"""

HOME = """
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow light">Life Builders &middot; A 501(c)(3) charitable organization</p>
      <h1>Build the man. Strengthen the family. Change the legacy.</h1>
      <p class="hero-lede">Men are drifting without mentors, purpose or a foundation in Scripture. Life Builders helps them root their lives in truth, walks beside them with a mentor, and removes the cost barrier so any man can start.</p>
      <div class="actions">
        <a class="btn btn-gold" href="{root}mentorship/">Apply for mentorship</a>
        <a class="btn btn-outline" href="{root}story/">Share your story</a>
      </div>
    </div>
    <div class="hero-mark"><img src="{root}assets/img/logo-light.png" alt="Life Builders logo" width="340"></div>
  </div>
</section>

<section class="section">
  <div class="wrap two-col">
    <div>
      <p class="eyebrow">The problem</p>
      <h2>Drifting men create broken families.</h2>
    </div>
    <div>
      <p>Men are increasingly isolated, lacking mentors, drifting without purpose, and struggling to lead themselves, their families and their communities. The result is fractured homes, fatherlessness, addiction, loneliness, and cycles that pass from one generation to the next.</p>
      <p>Many men want help. Cost keeps them from it. Life Builders exists to change that.</p>
    </div>
  </div>
</section>
""" + PATHWAY + """
<section class="section alt">
  <div class="wrap">
    <p class="eyebrow center">What we do</p>
    <h2 class="center">Three ways we build men</h2>
    <div class="cards three">
      <article class="card">
        <p class="eyebrow">The Standard Podcast</p>
        <h3>A message that gives language to the drift</h3>
        <p>The Standard with Preston Woody brings practical, faith-based teaching on life, leadership, marriage and growth to men wherever they listen.</p>
      </article>
      <article class="card">
        <p class="eyebrow">Bible Experience</p>
        <h3>Truth that becomes a daily rhythm</h3>
        <p>A reading and listening plan built to help men experience the entire Bible, ten to fifteen minutes a day, and live what they read.</p>
      </article>
      <article class="card">
        <p class="eyebrow">Mentorship</p>
        <h3>A mentor who walks beside him</h3>
        <p>Sponsored mentorship and transformational experiences for men who are ready to grow, free to the participant after an application.</p>
        <a class="text-link" href="{root}mentorship/">How mentorship works &rarr;</a>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow center">One man's journey</p>
    <h2 class="center">How one man moves from drift to generational impact</h2>
    <p class="lede center narrow">Meet Daniel: 38, husband, father of two. Present, but distracted. Responsible, but drifting. Ready for change, but unsure where to begin.</p>
    <ol class="journey">
      <li><p class="eyebrow">1 &middot; Hears</p><h3>The message</h3><p>The Standard gives language to his drift. "I don't have to stay here."</p></li>
      <li><p class="eyebrow">2 &middot; Roots</p><h3>In truth</h3><p>The Bible plan moves truth into his daily rhythm.</p></li>
      <li><p class="eyebrow">3 &middot; Responds</p><h3>Takes ownership</h3><p>He completes an assessment, then applies for mentorship.</p></li>
      <li><p class="eyebrow">4 &middot; Accesses</p><h3>A path forward</h3><p>A scholarship removes the financial barrier. A mentor walks beside him.</p></li>
      <li><p class="eyebrow">5 &middot; Transforms</p><h3>Becomes a leader</h3><p>Faith and discipline deepen. His family sees the change.</p></li>
    </ol>
    <p class="fineprint center">Daniel is an illustration of the path every man can take. Donor partnership makes every step possible.</p>
  </div>
</section>

<section class="section quote-section">
  <div class="wrap narrow">
    <blockquote>
      <p>"Transformation begins with information, but takes root when a man has another man who can call out the gold nobody else sees."</p>
      <cite>Preston Woody, Founder</cite>
    </blockquote>
    <p class="center"><a class="text-link" href="{root}about/">Read the founder's story &rarr;</a></p>
  </div>
</section>
""" + GIVE_BAND

ABOUT = """
<section class="page-hero">
  <div class="wrap narrow">
    <p class="eyebrow light">Our story</p>
    <h1>It started with a man, a Bible, and every morning before sunrise.</h1>
  </div>
</section>

<section class="section">
  <div class="wrap narrow prose">
    <p>Ten years ago I spent my final days with my grandfather, Wayne Woody. Each morning he rose before the sun, opened his Bible and read. When I asked him how he chose what to read each day, he told me he had read through the Bible more than 120 times. That shook me to my core.</p>
    <p>When he was young, he started reading it through each year, just ten to fifteen minutes first thing each morning. I committed to him that I would do the same. Ten years, a marriage, three businesses and three kids later, I have read the Bible ten times in four different versions. That daily discipline gave me the capacity to build a life dedicated to helping others do the same.</p>
    <p>In 2020 I became a coach, and I learned that transformation begins with information but takes root when a man has another man who can call out the gold nobody else sees and build a vision that outlasts life's hardest trials.</p>
    <p>My dream is to see 100,000 men experience the entire Bible at a time when most men are handing their thinking to someone, or something, else. I believe this work can create generational impact and give any man a shot at changing his legacy.</p>
    <p class="signature">Preston Woody<br><span>Founder and President</span></p>
  </div>
</section>

<section class="section alt">
  <div class="wrap two-col">
    <div>
      <p class="eyebrow">Our mission</p>
      <h2>Build men. Strengthen families. Change generations.</h2>
    </div>
    <div>
      <p>Life Builders builds men, strengthens families and changes generations through mentorship, education, leadership development and charitable support.</p>
      <p>We remove financial barriers so men can access life-changing resources and experiences regardless of their ability to pay.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow center">Where we're going</p>
    <h2 class="center">One-year and ten-year vision</h2>
    <div class="table-wrap">
      <table class="vision">
        <thead><tr><th></th><th>The Standard Podcast</th><th>Bible Experience</th><th>Mentorship</th></tr></thead>
        <tbody>
          <tr><th>Year 1</th><td>Produce 16 podcast messages</td><td>Build a Bible reading plan and pursue a YouVersion partnership</td><td>Open access to mentorship</td></tr>
          <tr><th>10 years</th><td>Reach 3 million through long-form listens</td><td>Help 100,000 men experience the whole Bible</td><td>Provide 1,000 mentorship sponsorships</td></tr>
        </tbody>
      </table>
    </div>
    <p class="fineprint center">Targets, not results. See the full numbers on the <a href="{root}impact/">Impact</a> page.</p>
  </div>
</section>

<section class="section alt">
  <div class="wrap narrow">
    <p class="eyebrow">Stewardship</p>
    <h2>Every gift is managed with integrity.</h2>
    <p>Life Builders is a ministry of Preston Woody Foundation Corporation, a recognized 501(c)(3) public charity. Financial stewardship, accountability and measurable impact are foundational commitments. Unless agreed otherwise in writing, gifts support the overall charitable mission and go where they can do the most mission-aligned good.</p>
  </div>
</section>
""" + GIVE_BAND

MENTORSHIP = """
<section class="page-hero">
  <div class="wrap narrow">
    <p class="eyebrow light">Mentorship</p>
    <h1>You weren't meant to build alone.</h1>
    <p class="hero-lede">A 90-day mentorship that pairs you with a trained mentor who walks beside you, calls out what's possible, and helps you lead yourself and your family well.</p>
    <div class="actions"><a class="btn btn-gold" href="#apply">Apply now</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="cards three">
      <article class="card"><p class="eyebrow">90 days</p><h3>Focused and finite</h3><p>A clear season with a written plan, so the growth lasts after the 90 days end.</p></article>
      <article class="card"><p class="eyebrow">Virtual</p><h3>Wherever you are</h3><p>You meet with your mentor online, so distance and schedule don't keep you out.</p></article>
      <article class="card"><p class="eyebrow">Free to you</p><h3>Sponsored by donors</h3><p>Once your application is approved, your mentorship is fully sponsored. Cost should never be the reason a man stays stuck.</p></article>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="wrap two-col">
    <div>
      <p class="eyebrow">Who it's for</p>
      <h2>Men who are ready to stop drifting.</h2>
    </div>
    <div>
      <p>Husbands, fathers and leaders who are present but distracted, responsible but drifting, and ready for change but unsure where to begin.</p>
      <p>You don't need to have it figured out. You need to be honest about where you are and willing to do the work.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow center">How it works</p>
    <h2 class="center">Four steps</h2>
    <ol class="steps">
      <li><span class="num">1</span><h3>Apply</h3><p>Tell us where you are and where you want to go. It takes about ten minutes.</p></li>
      <li><span class="num">2</span><h3>Review</h3><p>Our team reads every application and follows up personally.</p></li>
      <li><span class="num">3</span><h3>Match</h3><p>Approved men are matched with a trained mentor.</p></li>
      <li><span class="num">4</span><h3>Meet</h3><p>Your first virtual meeting sets your 90-day plan.</p></li>
    </ol>
  </div>
</section>

<section class="section alt" id="apply">
  <div class="wrap narrow">
    <p class="eyebrow center">Apply</p>
    <h2 class="center">Start your application</h2>
    <div class="form-slot" data-form="mentorship">
      <p>The application form opens here soon.</p>
      <p class="fineprint">Questions in the meantime? Email <a href="mailto:preston@saintscrown.com">preston@saintscrown.com</a>.</p>
    </div>
  </div>
</section>
""" + GIVE_BAND

STORY = """
<section class="page-hero">
  <div class="wrap narrow">
    <p class="eyebrow light">Share your story</p>
    <h1>Has The Standard helped you? Tell us.</h1>
    <p class="hero-lede">Your story shows other men what's possible and shows our partners what their generosity is doing. It takes about five minutes.</p>
    <div class="actions"><a class="btn btn-gold" href="#share">Share your story</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="cards three">
      <article class="card"><p class="eyebrow">Where you were</p><h3>Before</h3><p>What were you facing when you started listening?</p></article>
      <article class="card"><p class="eyebrow">What changed</p><h3>The turn</h3><p>Which message, idea or moment made a difference?</p></article>
      <article class="card"><p class="eyebrow">Where you are</p><h3>Now</h3><p>What's different in you, your marriage, your family or your work?</p></article>
    </div>
  </div>
</section>

<section class="section alt" id="share">
  <div class="wrap narrow">
    <p class="eyebrow center">Your story</p>
    <h2 class="center">Share it here</h2>
    <div class="form-slot" data-form="story">
      <p>The story form opens here soon.</p>
    </div>
    <p class="fineprint center">Your story stays private. We will never share it publicly without your separate permission.</p>
  </div>
</section>
"""

IMPACT = """
<section class="page-hero">
  <div class="wrap narrow">
    <p class="eyebrow light">Impact</p>
    <h1>What your generosity builds.</h1>
    <p class="hero-lede">We're launching in 2026. Here's what we've set out to do, and where we'll report what actually happens.</p>
  </div>
</section>
""" + PATHWAY + """
<section class="section alt">
  <div class="wrap">
    <p class="eyebrow center">Ten-year vision</p>
    <h2 class="center">Where the pathway leads</h2>
    <div class="cards three">
      <article class="card stat"><p class="eyebrow">The Standard Podcast</p><p class="big">3 million</p><p>reached through long-form listens</p></article>
      <article class="card stat"><p class="eyebrow">Bible Experience</p><p class="big">100,000</p><p>men who experience the whole Bible</p></article>
      <article class="card stat"><p class="eyebrow">Mentorship</p><p class="big">1,000</p><p>mentorship sponsorships provided</p></article>
    </div>
    <p class="fineprint center">Ten-year targets. Podcast reach is reported separately from verified program outcomes.</p>
  </div>
</section>

<section class="section">
  <div class="wrap narrow">
    <p class="eyebrow">Donor updates</p>
    <h2>Updates from the work</h2>
    <p>Our first update to founding partners goes out in December 2026, covering what their gifts made possible in our first season. Future updates will be posted here.</p>
  </div>
</section>
""" + GIVE_BAND

GIVE = f"""
<section class="page-hero">
  <div class="wrap narrow">
    <p class="eyebrow light">Give</p>
    <h1>Build the man. Strengthen the family. Change the legacy.</h1>
    <p class="hero-lede">Your gift removes the financial barrier for men who are ready to change. One-time, monthly and multi-year gifts are all welcome.</p>
    <div class="actions"><a class="btn btn-gold" href="{GIVE_URL}" target="_blank" rel="noopener">Give online</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow center">Monthly impact partners</p>
    <h2 class="center">Give every month</h2>
    <div class="tiers">
      <div class="tier"><p class="big">$50</p><p class="eyebrow">Open the Door</p><p>$600 a year</p></div>
      <div class="tier featured"><p class="big">$100</p><p class="eyebrow">Build a Man</p><p>$1,200 a year</p><p class="tag">Recommended start</p></div>
      <div class="tier"><p class="big">$250</p><p class="eyebrow">Strengthen a Family</p><p>$3,000 a year</p></div>
      <div class="tier"><p class="big">$500</p><p class="eyebrow">Change a Legacy</p><p>$6,000 a year</p></div>
      <div class="tier"><p class="big">$1,000</p><p class="eyebrow">Build the Future</p><p>$12,000 a year</p></div>
    </div>
    <p class="center"><a class="btn btn-navy" href="{GIVE_URL}" target="_blank" rel="noopener">Become a monthly partner</a></p>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <p class="eyebrow center">Founding partners</p>
    <h2 class="center">Major gifts</h2>
    <p class="lede center narrow">Founding partners give the launch capital that lets Life Builders serve men for years to come. Gifts can be made at once or over a monthly, quarterly, annual or multi-year schedule.</p>
    <div class="tiers four">
      <div class="tier"><p class="big">$15,000</p><p class="eyebrow">Mission Builder</p></div>
      <div class="tier"><p class="big">$25,000</p><p class="eyebrow">Impact Partner</p></div>
      <div class="tier"><p class="big">$50,000</p><p class="eyebrow">Legacy Builder</p></div>
      <div class="tier"><p class="big">$100,000</p><p class="eyebrow">Founding Vision Partner</p></div>
    </div>
    <p class="center"><a class="btn btn-navy" href="mailto:{CONTACT_EMAIL}?subject=Founding%20partner%20gift">Talk with Preston</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow center">Ways to give</p>
    <h2 class="center">Give generously. Give wisely.</h2>
    <div class="cards three">
      <article class="card"><h3>Online</h3><p>One-time or recurring gifts through our secure giving page.</p><a class="text-link" href="{GIVE_URL}" target="_blank" rel="noopener">Give online &rarr;</a></article>
      <article class="card"><h3>Check, ACH or wire</h3><p>Make checks payable to Preston Woody Foundation Corporation, memo Life Builders. Email us for the mailing address or secure bank instructions.</p></article>
      <article class="card"><h3>Stock, IRA or donor-advised fund</h3><p>Appreciated stock, an IRA charitable distribution or a DAF grant can stretch your gift. Contact us before you sell or withdraw.</p></article>
    </div>
    <p class="fineprint center">This page is general information, not tax advice. Please talk with your own tax advisor. Contributions are deductible to the extent allowed by law.</p>
  </div>
</section>
"""

page("", "Life Builders | Build the man. Strengthen the family. Change the legacy.",
     "Life Builders helps men root their lives in Scripture, find a mentor, and lead their families well, and removes the cost barrier so any man can start.", HOME, "")
page("about/", "Our Story | Life Builders", "The story behind Life Builders and its founder, Preston Woody.", ABOUT, "about/")
page("mentorship/", "Mentorship | Life Builders", "A free, sponsored 90-day virtual mentorship for men ready to stop drifting.", MENTORSHIP, "mentorship/")
page("story/", "Share Your Story | Life Builders", "Has The Standard podcast helped you? Share your story with Life Builders.", STORY, "story/")
page("impact/", "Impact | Life Builders", "What Life Builders sets out to do in year one and over ten years.", IMPACT, "impact/")
page("give/", "Give | Life Builders", "Support Life Builders with a one-time, monthly or founding partner gift.", GIVE, "give/")
# CNAME added once DNS points to GitHub Pages: (SITE / "CNAME").write_text("lifebuilders.net\n")
(SITE / ".nojekyll").write_text("")
print("built")
