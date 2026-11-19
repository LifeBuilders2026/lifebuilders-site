"""Branded site forms that post into the existing Google Forms.

Each field name is the Google Form's entry ID, so answers land in the same
response sheet tabs as before. If a question is added, removed or reworded
in a Google Form, update its entry here (see README: "Forms").
Item types follow Google's codes: 0 short text, 1 paragraph, 2 multiple
choice, 4 checkboxes, 6 section header, 8 page break.
"""
import html

GF = "https://docs.google.com/forms/d/e/{}/formResponse"
GF_VIEW = "https://docs.google.com/forms/d/e/{}/viewform"
OTHER = "__other__"

FORMS = {
    "mentor": {
        "id": "1FAIpQLSdecv6O4qvhO327ga7zbDR93pkgMOqBBIhntdF6pSUaMI-jIQ",
        "intro": "A free, 90-day virtual mentorship for men 18 and older. It takes about 10 minutes, and our team reads every application and follows up personally.",
        "notice": "Life Builders mentorship is not counseling or therapy. If you are in crisis, call or text 988 (Suicide &amp; Crisis Lifeline).",
        "submit": "Submit application",
        "done_title": "Application received.",
        "done_text": "Thank you for applying. Our team reads every application and will follow up with you personally.",
        "items": [
            (6, 0, 0, "About you", []),
            (0, 489131209, 1, "Full name", []),
            (0, 531066950, 1, "Email", []),
            (0, 412089155, 1, "Phone", []),
            (0, 1999380734, 1, "City and state", []),
            (2, 1200677348, 1, "Age range", ["18 to 24", "25 to 34", "35 to 44", "45 to 54", "55 or older"]),
            (2, 1723257533, 0, "Marital status", ["Single", "Married", "Separated or divorced", "Widowed", "Prefer not to say"]),
            (2, 379892452, 0, "Do you have children?", ["Yes", "No"]),
            (8, 0, 0, "Where you are", []),
            (1, 1489286356, 1, "What's going on in your life right now that made you apply?", []),
            (4, 1401944993, 1, "Where do you feel most stuck? Choose any that apply.", ["Faith", "Marriage", "Fatherhood", "Work or career", "Health", "Purpose and direction", "Habits or addiction", OTHER]),
            (1, 1206632953, 1, "What do you want to be different 90 days from now?", []),
            (2, 1560178698, 0, "How would you describe your faith right now?", ["Growing and active", "A believer, but inconsistent", "Exploring", "Not sure"]),
            (8, 0, 0, "Commitment", []),
            (2, 373921141, 1, "Mentorship runs 90 days and meets virtually. Can you commit to meeting with your mentor regularly for 90 days?", ["Yes", "I have questions first"]),
            (4, 270477084, 0, "What times usually work best for you?", ["Weekday mornings", "Weekday lunch", "Weekday evenings", "Weekends"]),
            (2, 452295270, 1, "How did you hear about Life Builders?", ["The Standard podcast", "Saints Crown", "A friend or family member", "My church", "Social media", OTHER]),
            (1, 1563174404, 0, "Anything else we should know?", []),
            (4, 329665526, 1, "Agreement", ["I understand the Life Builders team will review my application, and mentorship is free once I am approved."]),
        ],
    },
    "story": {
        "id": "1FAIpQLSfzvm9KSJhWinfOeMP8FQgX_MxfvhFWLHNZ4s3_8H75B9mYZw",
        "intro": "",
        "notice": "",
        "submit": "Share my story",
        "done_title": "Thank you for sharing.",
        "done_text": "Your story matters. Our team will read it personally, and we will never share it publicly without your permission.",
        "items": [
            (0, 799675764, 1, "First name", []),
            (0, 1570047928, 1, "Email", [], "We'll only use this to follow up about your story."),
            (0, 1904109123, 0, "City and state", []),
            (2, 30362650, 0, "How long have you listened to The Standard?", ["Less than 3 months", "3 to 12 months", "More than a year"]),
            (1, 1326136451, 1, "Where were you when you started listening? What were you facing?", []),
            (1, 862953205, 1, "What message, idea or moment made a difference?", []),
            (1, 1800407841, 1, "What's different now in you, your marriage, your family or your work?", []),
            (2, 1363922213, 1, "May we share your story publicly?", ["Yes, with my first name", "Yes, but keep it anonymous", "No, keep it private"]),
            (2, 1911279626, 1, "May we contact you to follow up?", ["Yes", "No"]),
        ],
    },
    "contact": {
        "id": "1FAIpQLSdwSduOYAwvJzvgOXlVb3w8G5N3lhbIoVCTcSCq1GT1Ym7HPg",
        "intro": "",
        "notice": "",
        "submit": "Send message",
        "done_title": "Message sent.",
        "done_text": "Thanks for reaching out. Someone from our team will get back to you soon.",
        "items": [
            (0, 947988994, 1, "Name", []),
            (0, 1528375330, 1, "Email", []),
            (0, 423854929, 0, "Phone (optional)", []),
            (2, 2121202158, 1, "What's this about?", ["Mentorship", "Sharing a story", "Giving, including stock or IRA gifts", "The Standard podcast", "Volunteering or becoming a mentor", OTHER]),
            (1, 1436633745, 1, "Message", []),
        ],
    },
}


def _e(s):
    return html.escape(s, quote=True)


def _input_type(label):
    low = label.lower()
    if low.startswith("email"):
        return 'type="email" autocomplete="email" inputmode="email"'
    if low.startswith("phone"):
        return 'type="tel" autocomplete="tel" inputmode="tel"'
    if low in ("full name", "name"):
        return 'type="text" autocomplete="name"'
    if low == "first name":
        return 'type="text" autocomplete="given-name"'
    return 'type="text"'


def _field(key, item):
    kind, entry, req, label = item[0], item[1], item[2], item[3]
    choices = item[4]
    help_text = item[5] if len(item) > 5 else ""
    fid = f"{key}-{entry}"
    star = '<span class="req" aria-hidden="true">*</span>' if req else ""
    help_html = f'<span class="help">{_e(help_text)}</span>' if help_text else ""
    name = f"entry.{entry}"
    r = " required" if req else ""
    if kind == 0:
        return (f'<div class="field"><label for="{fid}">{_e(label)}{star}</label>{help_html}'
                f'<input id="{fid}" name="{name}" {_input_type(label)}{r}></div>')
    if kind == 1:
        return (f'<div class="field"><label for="{fid}">{_e(label)}{star}</label>{help_html}'
                f'<textarea id="{fid}" name="{name}" rows="5"{r}></textarea></div>')
    if kind in (2, 4):
        typ = "radio" if kind == 2 else "checkbox"
        opts = []
        for i, c in enumerate(choices):
            oid = f"{fid}-{i}"
            if c == OTHER:
                opts.append(
                    f'<label class="choice other" for="{oid}"><input id="{oid}" type="{typ}" name="{name}" value="__other_option__">'
                    f'<span>Other:</span><input type="text" class="other-text" name="{name}.other_option_response" aria-label="Other, please specify"></label>')
            else:
                opts.append(f'<label class="choice" for="{oid}"><input id="{oid}" type="{typ}" name="{name}" value="{_e(c)}"><span>{_e(c)}</span></label>')
        legend = "Please confirm" if label == "Agreement" else label
        return (f'<fieldset class="field group" data-required="{req}"><legend>{_e(legend)}{star}</legend>{help_html}'
                f'<div class="choices">{"".join(opts)}</div></fieldset>')
    return ""


def render(key):
    f = FORMS[key]
    pages = [[]]
    titles = []
    for item in f["items"]:
        if item[0] == 8:
            pages.append([])
            titles.append(item[3])
        elif item[0] == 6:
            titles.insert(0, item[3])
        else:
            pages[-1].append(item)
    multi = len(pages) > 1
    parts = [f'<div class="lb-form-wrap" id="{key}-form">']
    parts.append(f'<form class="lb-form" data-action="{GF.format(f["id"])}" data-pages="{len(pages)}" novalidate>')
    if f["intro"]:
        parts.append(f'<p class="form-intro">{f["intro"]}</p>')
    if f["notice"]:
        parts.append(f'<p class="form-notice">{f["notice"]}</p>')
    if multi:
        active = ' class="active"'
        steps = "".join(f'<li{active if i == 0 else ""}><span>{i + 1}</span>{_e(t)}</li>' for i, t in enumerate(titles))
        parts.append(f'<ol class="form-steps" aria-label="Application steps">{steps}</ol>')
    for i, items in enumerate(pages):
        hidden = "" if i == 0 else " hidden"
        parts.append(f'<div class="form-step" data-step="{i}"{hidden}>')
        if multi:
            parts.append(f'<h3 class="step-title">{_e(titles[i])}</h3>')
        parts.extend(_field(key, it) for it in items)
        nav = []
        if i > 0:
            nav.append('<button type="button" class="btn btn-ghost" data-back>Back</button>')
        if i < len(pages) - 1:
            nav.append('<button type="button" class="btn btn-gold" data-next>Next</button>')
        else:
            nav.append(f'<button type="submit" class="btn btn-gold">{_e(f["submit"])}</button>')
        parts.append(f'<div class="form-nav">{"".join(nav)}</div></div>')
    parts.append('<div class="hp" aria-hidden="true"><label>Leave this empty<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>')
    parts.append('<p class="form-error" role="alert" hidden></p>')
    parts.append('<p class="form-required-note"><span class="req">*</span> Required</p>')
    parts.append('</form>')
    parts.append(f'<div class="form-done" hidden tabindex="-1"><h3>{_e(f["done_title"])}</h3><p>{_e(f["done_text"])}</p></div>')
    parts.append(f'<p class="fineprint center">Trouble with this form? <a href="{GF_VIEW.format(f["id"])}" target="_blank" rel="noopener">Use our backup form</a>.</p>')
    parts.append('</div>')
    return "\n".join(parts)
