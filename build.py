#!/usr/bin/env python3
"""Builds the Life Builders static site into ./site from the page content below."""
import os, html, pathlib

SITE = pathlib.Path(__file__).parent / "site"
GIVE_URL = "https://givebutter.com/lifebuilders-give"
GIVEBUTTER_LIB = '<script async src="https://widgets.givebutter.com/latest.umd.cjs?acct=dvLoMdShHQYq7qEm&p=other"></script>'
GIVEBUTTER_FORM = '<givebutter-widget id="pdVNee"></givebutter-widget>'

NAV = [("", "Home"), ("about/", "Our Story"), ("mentorship/", "Mentorship"),
       ("story/", "Share Your Story")]


def page(path, title, description, body, active, head_extra=""):
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
{head_extra}
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
        <li><a href="{root}give/">Give</a></li>
        <li><a href="{root}contact/">Contact</a></li>
      </ul>
    </div>
    <div>
      <p class="eyebrow light">Contact</p>
      <p>Fort Worth, Texas<br><a href="{root}contact/">Send us a message</a></p>
    </div>
  </div>
  <div class="wrap legal">
    <p>Life Builders is a ministry of Preston Woody Foundation Corporation, a 501(c)(3) public charity. Contributions are tax-deductible to the extent allowed by law.</p>
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
    <p class="lede center narrow">A message reaches a man. Truth roots him. A mentor equips him. His family is strengthened.</p>
    <ol class="pathway">
      <li><span class="num">1</span><p class="eyebrow">Reach</p><p class="big">The Standard</p><p>a podcast that gives men language for the drift</p></li>
      <li><span class="num">2</span><p class="eyebrow">Root</p><p class="big">Bible plan</p><p>a custom plan to help men find truth</p></li>
      <li><span class="num">3</span><p class="eyebrow">Open access</p><p class="big">Free mentorship</p><p>sponsored, so cost never keeps a man stuck</p></li>
      <li><span class="num">4</span><p class="eyebrow">Equip</p><p class="big">Trained mentors</p><p>men who walk beside you and call out the gold</p></li>
      <li><span class="num">5</span><p class="eyebrow">Multiply</p><p class="big">Generations</p><p>stronger men strengthen marriages, children, churches and communities</p></li>
    </ol>
  </div>
</section>
"""

GIVE_BAND = """
<section class="band navy">
  <div class="wrap band-row">
    <div>
      <p class="eyebrow light">Join the work</p>
      <h2>Help build the next man.</h2>
      <p>Mentorship is free for every man we serve because partners cover the cost.</p>
    </div>
    <div class="band-actions"><a class="btn btn-gold" href="{root}give/">Give</a></div>
  </div>
</section>
"""

HOME = """
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow light">For men ready to stop drifting</p>
      <h1>Build the man. Strengthen the family. Change the legacy.</h1>
      <p class="hero-lede">You weren't made to drift. Life Builders helps men root their lives in Scripture, walk with a mentor, and lead their families well. Mentorship is free for the men we serve.</p>
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
      <p class="eyebrow">Why we exist</p>
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
        <p>A trained mentor walks with you for 90 days. It's free once your application is approved.</p>
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
    <p class="fineprint center">Daniel is an illustration. Your story can follow the same path.</p>
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
    <h2 class="center">The next ten years</h2>
    <div class="cards three">
      <article class="card stat"><p class="eyebrow">The Standard Podcast</p><p class="big">3 million</p><p>people reached with the message</p></article>
      <article class="card stat"><p class="eyebrow">Bible Experience</p><p class="big">100,000</p><p>men who experience the whole Bible</p></article>
      <article class="card stat"><p class="eyebrow">Mentorship</p><p class="big">1,000</p><p>men mentored, free of cost</p></article>
    </div>
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
      <article class="card"><p class="eyebrow">Free to you</p><h3>Covered for you</h3><p>Once your application is approved, your mentorship is fully sponsored. Cost should never be the reason a man stays stuck.</p></article>
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
    <div class="form-embed"><iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdecv6O4qvhO327ga7zbDR93pkgMOqBBIhntdF6pSUaMI-jIQ/viewform?embedded=true" height="1500" title="Mentorship application" loading="lazy">Loading</iframe></div>
    <p class="fineprint center">Form not loading? <a href="https://docs.google.com/forms/d/e/1FAIpQLSdecv6O4qvhO327ga7zbDR93pkgMOqBBIhntdF6pSUaMI-jIQ/viewform" target="_blank" rel="noopener">Open it in a new tab</a>.</p>
    <p class="fineprint center">Questions first? <a href="{root}contact/">Send us a message</a>.</p>
  </div>
</section>
"""

STORY = """
<section class="page-hero">
  <div class="wrap narrow">
    <p class="eyebrow light">Share your story</p>
    <h1>Has The Standard helped you? Tell us.</h1>
    <p class="hero-lede">Your story shows other men what's possible. It takes about five minutes.</p>
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
    <div class="form-embed"><iframe src="https://docs.google.com/forms/d/e/1FAIpQLSfzvm9KSJhWinfOeMP8FQgX_MxfvhFWLHNZ4s3_8H75B9mYZw/viewform?embedded=true" height="1900" title="Share your story" loading="lazy">Loading</iframe></div>
    <p class="fineprint center">Form not loading? <a href="https://docs.google.com/forms/d/e/1FAIpQLSfzvm9KSJhWinfOeMP8FQgX_MxfvhFWLHNZ4s3_8H75B9mYZw/viewform" target="_blank" rel="noopener">Open it in a new tab</a>.</p>
    <p class="fineprint center">Your story stays private. We will never share it publicly without your separate permission.</p>
  </div>
</section>

<section class="section">
  <div class="wrap narrow">
    <p class="eyebrow">Stories</p>
    <h2>Stories from the work</h2>
    <p>As men share how God is changing their lives, we'll tell those stories here, always with their permission.</p>
  </div>
</section>
"""

GIVE = f"""
<section class="page-hero">
  <div class="wrap narrow">
    <p class="eyebrow light">Give</p>
    <h1>Build the man. Strengthen the family. Change the legacy.</h1>
    <p class="hero-lede">Your gift removes the financial barrier for men who are ready to change. One-time, monthly and multi-year gifts are all welcome.</p>
    <div class="actions"><a class="btn btn-gold" href="#give-now">Give now</a></div>
  </div>
</section>

<section class="section" id="give-now">
  <div class="wrap narrow">
    <p class="eyebrow center">Give now</p>
    <h2 class="center">Give securely, right here</h2>
    <p class="lede center">Choose one-time or monthly. Every gift is tax-deductible and receipted by email.</p>
    <div class="give-embed">{GIVEBUTTER_FORM}</div>
    <p class="fineprint center">Trouble loading the form? <a href="{GIVE_URL}" target="_blank" rel="noopener">Give on our secure GiveButter page</a>.</p>
  </div>
</section>

<section class="section alt">
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
    <p class="center"><a class="btn btn-navy" href="#give-now">Become a monthly partner</a></p>
  </div>
</section>

<section class="section">
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
    <p class="center"><a class="btn btn-navy" href="../contact/">Start a conversation</a></p>
  </div>
</section>

<section class="section alt">
  <div class="wrap">
    <p class="eyebrow center">Ways to give</p>
    <h2 class="center">Give generously. Give wisely.</h2>
    <div class="cards three">
      <article class="card"><h3>Online</h3><p>One-time or recurring gifts through our secure giving page.</p><a class="text-link" href="#give-now">Give now &rarr;</a></article>
      <article class="card"><h3>Check, ACH or wire</h3><p>Make checks payable to Preston Woody Foundation Corporation, memo Life Builders. <a href="../contact/">Send us a message</a> for the mailing address or secure bank instructions.</p></article>
      <article class="card"><h3>Stock, IRA or donor-advised fund</h3><p>Appreciated stock, an IRA charitable distribution or a DAF grant can stretch your gift. <a href="../contact/">Contact us</a> before you sell or withdraw.</p></article>
    </div>
    <p class="fineprint center">This page is general information, not tax advice. Please talk with your own tax advisor. Contributions are deductible to the extent allowed by law.</p>
  </div>
</section>
"""


CONTACT = """
<section class="page-hero">
  <div class="wrap narrow">
    <p class="eyebrow light">Contact</p>
    <h1>Let's talk.</h1>
    <p class="hero-lede">Questions about mentorship, giving or the podcast? Send us a message and someone from our team will get back to you.</p>
  </div>
</section>

<section class="section">
  <div class="wrap narrow">
    <div class="form-embed"><iframe src="https://docs.google.com/forms/d/e/1FAIpQLSdwSduOYAwvJzvgOXlVb3w8G5N3lhbIoVCTcSCq1GT1Ym7HPg/viewform?embedded=true" height="1150" title="Contact Life Builders" loading="lazy">Loading</iframe></div>
    <p class="fineprint center">Form not loading? <a href="https://docs.google.com/forms/d/e/1FAIpQLSdwSduOYAwvJzvgOXlVb3w8G5N3lhbIoVCTcSCq1GT1Ym7HPg/viewform" target="_blank" rel="noopener">Open it in a new tab</a>.</p>
  </div>
</section>
"""

page("", "Life Builders | Build the man. Strengthen the family. Change the legacy.",
     "Life Builders helps men root their lives in Scripture, find a mentor, and lead their families well, and removes the cost barrier so any man can start.", HOME, "")
page("about/", "Our Story | Life Builders", "The story behind Life Builders and its founder, Preston Woody.", ABOUT, "about/")
page("mentorship/", "Mentorship | Life Builders", "A free, sponsored 90-day virtual mentorship for men ready to stop drifting.", MENTORSHIP, "mentorship/")
page("story/", "Share Your Story | Life Builders", "Has The Standard podcast helped you? Share your story with Life Builders.", STORY, "story/")
page("contact/", "Contact | Life Builders", "Send Life Builders a message.", CONTACT, "contact/")
page("give/", "Give | Life Builders", "Support Life Builders with a one-time, monthly or founding partner gift.", GIVE, "give/", head_extra=GIVEBUTTER_LIB)
(SITE / "CNAME").write_text("lifebuilders.net\n")
(SITE / ".nojekyll").write_text("")
print("built")
