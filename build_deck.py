#!/usr/bin/env python3
"""Factorial Client Day deck. 16:9 PDF."""

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import simpleSplit

OUT = "/Users/victor.gutierrez/Documents/Client Day/Factorial-Client-Day.pdf"
W, H = 960, 540
ML = 50

RED = HexColor("#E10600")
RED_ON_DARK = HexColor("#FF6A5C")
INK = HexColor("#161616")
MUTED = HexColor("#5C5854")
BODY = HexColor("#3F3C39")
SAND = HexColor("#F6F3EE")
DARK = HexColor("#141414")
LINE = HexColor("#ECE7E1")
CREAM = HexColor("#F7F4EF")
FOOT = HexColor("#8A847C")
PALE = HexColor("#E6E2DC")


def bg(c, color):
    c.setFillColor(color)
    c.rect(0, 0, W, H, stroke=0, fill=1)


def footer(c, num=None, dark=False):
    c.setFillColor(RED)
    c.rect(ML, 28, 7, 7, stroke=0, fill=1)
    c.setFillColor(HexColor("#C8C4BE") if dark else INK)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(ML + 14, 28, "factorial")
    if num is not None:
        c.setFillColor(HexColor("#9A958E") if dark else FOOT)
        c.setFont("Helvetica", 10)
        c.drawRightString(W - ML, 28, f"{num:02d}")


def eyebrow(c, text, x, y, color=RED):
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x, y, text.upper())


def wrapped(c, text, x, y, font, size, color, max_w, leading):
    c.setFillColor(color)
    c.setFont(font, size)
    lines = simpleSplit(text, font, size, max_w)
    for i, line in enumerate(lines):
        c.drawString(x, y - i * leading, line)
    return len(lines)


def title_slide(c):
    bg(c, DARK)
    c.setFillColor(RED)
    c.rect(ML, 318, 52, 4, stroke=0, fill=1)
    eyebrow(c, "Client Day", ML, 286, RED_ON_DARK)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 68)
    c.drawString(ML, 210, "Factorial")
    c.setFillColor(HexColor("#D4D0CA"))
    c.setFont("Helvetica", 20)
    c.drawString(ML, 168, "For the people who use it, and the people who might.")
    footer(c, 1, dark=True)
    c.showPage()


def agenda(c):
    bg(c, white)
    eyebrow(c, "Today", ML, 486)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 32)
    c.drawString(ML, 448, "How this hour goes")
    items = [
        "What is new",
        "What clients already use",
        "KennScott",
        "Kahoot",
        "Questions from both sides of the room",
    ]
    y = 390
    for i, item in enumerate(items, 1):
        c.setStrokeColor(LINE)
        c.setLineWidth(1)
        c.line(ML, y + 26, W - ML, y + 26)
        c.setFillColor(RED)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(ML, y, f"{i:02d}")
        c.setFillColor(INK)
        c.setFont("Helvetica", 22)
        c.drawString(ML + 48, y - 2, item)
        y -= 62
    footer(c, 2)
    c.showPage()


def features(c, num):
    bg(c, white)
    eyebrow(c, "What clients use", ML, 492)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(ML, 456, "What clients already use")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 15)
    c.drawString(ML, 426, "The same set KennScott is running.")
    cards = [
        ("01", "Time", "Leave and attendance, day to day"),
        ("02", "Documents", "Contracts and certifications, signed online"),
        ("03", "Records", "Profiles and attendance in one place"),
        ("04", "Learning", "Training on the record, including offshore safety"),
        ("05", "Reminders", "Birthdays and anniversaries for offshore staff"),
    ]
    gap = 14
    cw = (W - ML * 2 - gap * 2) / 3
    ch = 148
    top = 398
    row2 = 2 * cw + gap
    x2 = ML + ((W - ML * 2) - row2) / 2
    spots = [
        (ML, top - ch),
        (ML + cw + gap, top - ch),
        (ML + 2 * (cw + gap), top - ch),
        (x2, top - ch - gap - ch),
        (x2 + cw + gap, top - ch - gap - ch),
    ]
    for (n, name, desc), (x, y) in zip(cards, spots):
        c.setFillColor(SAND)
        c.roundRect(x, y, cw, ch, 8, stroke=0, fill=1)
        c.setFillColor(RED)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(x + 18, y + ch - 32, n)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 22)
        c.drawString(x + 18, y + 58, name)
        wrapped(c, desc, x + 18, y + 34, "Helvetica", 13, BODY, cw - 36, 16)
    footer(c, num)
    c.showPage()


def difference(c, num):
    bg(c, white)
    eyebrow(c, "The difference", ML, 492)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 32)
    c.drawString(ML, 452, "What separates Factorial")
    gap = 16
    pw = (W - ML * 2 - gap) / 2
    ph = 330
    y = 68
    # dark
    c.setFillColor(DARK)
    c.roundRect(ML, y, pw, ph, 10, stroke=0, fill=1)
    eyebrow(c, "In the market", ML + 28, y + ph - 44, RED_ON_DARK)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 36)
    c.drawString(ML + 28, y + ph - 100, "Agentic AI")
    wrapped(
        c,
        "The only agentic AI among HRIS.",
        ML + 28,
        y + 56,
        "Helvetica",
        18,
        PALE,
        pw - 56,
        24,
    )
    # sand
    x2 = ML + pw + gap
    c.setFillColor(SAND)
    c.roundRect(x2, y, pw, ph, 10, stroke=0, fill=1)
    eyebrow(c, "In Trinidad", x2 + 28, y + ph - 44, RED)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 36)
    c.drawString(x2 + 28, y + ph - 100, "Local support")
    wrapped(
        c,
        "The only HRIS with local support in Trinidad.",
        x2 + 28,
        y + 56,
        "Helvetica",
        18,
        BODY,
        pw - 56,
        24,
    )
    footer(c, num)
    c.showPage()


def bullets(c, kicker, heading, items, num, callout=None, lede=None):
    bg(c, white)
    eyebrow(c, kicker, ML, 492)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 30)
    lines = simpleSplit(heading, "Helvetica-Bold", 30, 820)
    y = 450
    for line in lines:
        c.drawString(ML, y, line)
        y -= 36
    if lede:
        y -= 4
        n = wrapped(c, lede, ML, y, "Helvetica", 16, MUTED, 840, 20)
        y -= n * 20 + 8
    y -= 6
    for item in items:
        c.setFillColor(RED)
        c.circle(ML + 4, y + 4, 4, stroke=0, fill=1)
        used = wrapped(c, item, ML + 24, y, "Helvetica", 18, INK, 820, 24)
        y -= max(used, 1) * 24 + 16
    if callout:
        c.setFillColor(DARK)
        c.roundRect(ML, 64, W - ML * 2, 52, 8, stroke=0, fill=1)
        c.setFillColor(white)
        c.setFont("Helvetica", 16)
        c.drawString(ML + 20, 84, callout)
    footer(c, num)
    c.showPage()


def film(c, num):
    bg(c, DARK)
    c.setFillColor(RED)
    c.circle(ML + 28, 390, 28, stroke=0, fill=1)
    path = c.beginPath()
    path.moveTo(ML + 22, 376)
    path.lineTo(ML + 22, 404)
    path.lineTo(ML + 46, 390)
    path.close()
    c.setFillColor(white)
    c.drawPath(path, stroke=0, fill=1)
    eyebrow(c, "KennScott", ML, 320, RED_ON_DARK)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 56)
    c.drawString(ML, 250, "Play the film")
    c.setFillColor(HexColor("#D4D0CA"))
    c.setFont("Helvetica", 22)
    c.drawString(ML, 204, "Hold questions until it ends.")
    footer(c, num, dark=True)
    c.showPage()


def whats_new(c, num):
    bg(c, white)
    eyebrow(c, "What is new", ML, 492)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 30)
    c.drawString(ML, 452, "Live now. Two things still this quarter.")
    left_w = 530
    gap = 16
    right_x = ML + left_w + gap
    right_w = W - ML - right_x
    cards = [
        ("Set up from a file", "Job catalog, document templates, onboarding rules, and benefits."),
        ("The week of work", "On-call shifts, cover calls, retroactive clock-in, payroll exceptions."),
        ("For managers", "Accruals, training, goals, and 1-on-1s, with the assistant."),
    ]
    top = 420
    ch = 104
    gap_y = 12
    for i, (h, p) in enumerate(cards):
        y = top - (i + 1) * ch - i * gap_y
        c.setFillColor(SAND)
        c.roundRect(ML, y, left_w, ch, 8, stroke=0, fill=1)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 18)
        c.drawString(ML + 20, y + 62, h)
        wrapped(c, p, ML + 20, y + 34, "Helvetica", 13, BODY, left_w - 40, 17)
    panel_h = 3 * ch + 2 * gap_y
    panel_y = top - panel_h
    c.setFillColor(DARK)
    c.roundRect(right_x, panel_y, right_w, panel_h, 10, stroke=0, fill=1)
    eyebrow(c, "End of Q4", right_x + 22, panel_y + panel_h - 40, RED_ON_DARK)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 26)
    c.drawString(right_x + 22, panel_y + panel_h - 84, "Not live today")
    wrapped(
        c,
        "Culture fit on the candidate profile. A preview of the onboarding a person will actually get.",
        right_x + 22,
        panel_y + 70,
        "Helvetica",
        14,
        PALE,
        right_w - 44,
        19,
    )
    footer(c, num)
    c.showPage()


def rows(c, kicker, heading, lede, items, num):
    bg(c, white)
    eyebrow(c, kicker, ML, 492)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 32)
    c.drawString(ML, 452, heading)
    y_start = 400
    if lede:
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 16)
        c.drawString(ML, 416, lede)
        y_start = 378
    n = len(items)
    bottom = 64
    usable = y_start - bottom
    rh = usable / n
    for i, (name, desc) in enumerate(items):
        top = y_start - i * rh
        c.setStrokeColor(LINE)
        c.setLineWidth(1)
        c.line(ML, top, W - ML, top)
        mid = top - rh / 2
        c.setFillColor(RED)
        c.setFont("Helvetica-Bold", 13)
        c.drawString(ML, mid - 4, f"{i+1:02d}")
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(ML + 48, mid - 4, name)
        wrapped(c, desc, ML + 210, mid + 6, "Helvetica", 14, BODY, W - ML - (ML + 210), 18)
    footer(c, num)
    c.showPage()


def quarter(c, num):
    bg(c, white)
    eyebrow(c, "End of Q4", ML, 492)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 32)
    c.drawString(ML, 452, "Still this quarter")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 16)
    c.drawString(ML, 420, "Not in the product today.")
    gap = 16
    cw = (W - ML * 2 - gap) / 2
    ch = 280
    y = 78
    cards = [
        ("01", "Culture fit", "Scored from the candidate profile, then available in the engagement module."),
        ("02", "Onboarding simulation", "Pick a role or an entity and see the task list that person will get."),
    ]
    for i, (n, name, desc) in enumerate(cards):
        x = ML + i * (cw + gap)
        c.setFillColor(SAND)
        c.roundRect(x, y, cw, ch, 10, stroke=0, fill=1)
        c.setFillColor(RED)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(x + 28, y + ch - 44, n)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 26)
        wrapped(c, name, x + 28, y + ch - 90, "Helvetica-Bold", 26, INK, cw - 56, 32)
        wrapped(c, desc, x + 28, y + 70, "Helvetica", 16, BODY, cw - 56, 22)
    footer(c, num)
    c.showPage()


def qa(c, num):
    bg(c, white)
    eyebrow(c, "Q&A", ML, 492)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 32)
    c.drawString(ML, 452, "Ask the person who uses it")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 16)
    c.drawString(ML, 420, "Non-clients ask. Clients answer from use.")
    prompts = [
        "What did you stop doing in spreadsheets?",
        "What was broken before Factorial fixed it?",
        "What features do employees use the most?",
        "What made you buy Factorial?",
    ]
    y = 384
    for p in prompts:
        c.setFillColor(SAND)
        c.roundRect(ML, y - 52, W - ML * 2, 58, 8, stroke=0, fill=1)
        c.setFillColor(INK)
        c.setFont("Helvetica", 18)
        c.drawString(ML + 20, y - 30, p)
        y -= 74
    footer(c, num)
    c.showPage()


def suggestions(c, num):
    bg(c, white)
    eyebrow(c, "Suggestions", ML, 492)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 36)
    c.drawString(ML, 448, "One card. One sentence.")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 16)
    c.drawString(ML, 414, "We will read a few out loud. The rest go to the product team.")
    gap = 16
    cw = (W - ML * 2 - gap) / 2
    ch = 270
    y = 78
    cards = [
        ("Clients", "What is still missing"),
        ("Non-clients", "What you would need to see before you moved"),
    ]
    for i, (tag, line) in enumerate(cards):
        x = ML + i * (cw + gap)
        c.setFillColor(SAND)
        c.roundRect(x, y, cw, ch, 10, stroke=0, fill=1)
        eyebrow(c, tag, x + 28, y + ch - 48)
        wrapped(c, line, x + 28, y + ch - 110, "Helvetica-Bold", 26, INK, cw - 56, 32)
    footer(c, num)
    c.showPage()


def game(c, kicker, heading, lede, pill, num):
    bg(c, DARK)
    eyebrow(c, kicker, ML, 250, RED_ON_DARK)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 56)
    c.drawString(ML, 180, heading)
    c.setFillColor(HexColor("#D4D0CA"))
    c.setFont("Helvetica", 20)
    c.drawString(ML, 140, lede)
    c.setStrokeColor(HexColor("#3A3A3A"))
    c.setLineWidth(1)
    c.setFillColor(DARK)
    width = 150
    c.roundRect(ML, 78, width, 32, 16, stroke=1, fill=0)
    c.setFillColor(white)
    c.setFont("Helvetica", 12)
    c.drawString(ML + 16, 90, pill)
    footer(c, num, dark=True)
    c.showPage()


def close(c, num):
    bg(c, white)
    eyebrow(c, "Close", ML, 360)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 42)
    c.drawString(ML, 300, "Before you leave")
    items = [
        "Take the suggestion card with you",
        "Clients, your account manager has the updates",
        "Non-clients, name the spreadsheet you still run",
    ]
    y = 240
    for item in items:
        c.setFillColor(RED)
        c.circle(ML + 4, y + 4, 4, stroke=0, fill=1)
        c.setFillColor(INK)
        c.setFont("Helvetica", 18)
        c.drawString(ML + 24, y, item)
        y -= 40
    footer(c, num)
    c.showPage()


def stop(c):
    bg(c, DARK)
    eyebrow(c, "Stop presenting", ML, 320, RED_ON_DARK)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 48)
    c.drawString(ML, 250, "Host notes follow")
    wrapped(
        c,
        "Kahoot answers, what to say, and questions you may get. Do not show these pages.",
        ML,
        200,
        "Helvetica",
        18,
        HexColor("#D4D0CA"),
        760,
        24,
    )
    footer(c, None, dark=True)
    c.showPage()


def host_banner(c):
    c.setFillColor(RED)
    c.rect(0, H - 28, W, 28, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(ML, H - 18, "HOST ONLY. DO NOT SHOW.")


def host_say(c, heading, notes):
    bg(c, CREAM)
    host_banner(c)
    eyebrow(c, "What to say", ML, 480)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 26)
    c.drawString(ML, 448, heading)
    col_w = (W - ML * 2 - 24) / 2
    for i, (h, p) in enumerate(notes):
        col = i % 2
        row = i // 2
        x = ML + col * (col_w + 24)
        y = 410 - row * 88
        c.setFillColor(RED)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(x, y, h.upper())
        wrapped(c, p, x, y - 18, "Helvetica", 11, INK, col_w, 14)
    c.showPage()


def host_qa(c, kicker, heading, pairs, extra=None, last=False):
    bg(c, CREAM)
    host_banner(c)
    eyebrow(c, kicker, ML, 484)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(ML, 454, heading)
    y = 420
    for i, (q, a) in enumerate(pairs, 1):
        c.setFillColor(RED)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(ML, y, str(i))
        c.setFillColor(INK)
        c.setFont("Helvetica", 12)
        c.drawString(ML + 24, y, q)
        c.setFillColor(BODY)
        c.setFont("Helvetica", 12)
        c.drawString(ML + 24, y - 16, a)
        y -= 46
    if extra:
        y -= 6
        wrapped(c, extra, ML, y, "Helvetica", 11, BODY, W - ML * 2, 15)
    if not last:
        c.showPage()


def main():
    c = canvas.Canvas(OUT, pagesize=(W, H))
    c.setTitle("Factorial Client Day")
    c.setAuthor("Factorial")

    title_slide(c)
    agenda(c)
    whats_new(c, 3)
    rows(
        c,
        "Live now",
        "Set up from a file",
        "Upload the document. Factorial builds the setup.",
        [
            ("Job catalog", "Roles, salary bands, and categories from one upload."),
            ("Templates", "Document templates built from employee data."),
            ("Onboarding", "Tasks fire by location, department, or team."),
            ("Benefits", "Upload the policy. The employee sees their allowance."),
        ],
        4,
    )
    rows(
        c,
        "Live now",
        "The week of work",
        None,
        [
            ("On-call shifts", "For hospitality, healthcare, and any team off a fixed rota."),
            ("Open shift", "Factorial calls people to cover it, in their language."),
            ("Clock-in", "An employee can ask to be clocked in for a start time that already happened."),
            ("Payroll", "Differences with the external provider get flagged and resolved."),
        ],
        5,
    )
    rows(
        c,
        "Live now",
        "For managers",
        None,
        [
            ("Time off", "Accrual rules, including a day on a work anniversary, set with the assistant and simulated before you save."),
            ("Training", "The assistant writes the content. You set the design."),
            ("Goals", "Created in bulk, from a file or from a request."),
            ("1-on-1s", "Prep before the meeting. A summary and suggested actions after."),
        ],
        6,
    )
    quarter(c, 7)
    features(c, 8)
    difference(c, 9)
    bullets(
        c,
        "Agentic AI",
        "One knows the company and acts inside it",
        [
            "Screens candidates, and can call them",
            "Checks expenses against your policy",
            "Drafts the ticket answer for someone to approve",
            "Builds the report from live data",
            "Stays inside each person’s permissions",
        ],
        10,
        "The only agentic AI among HRIS.",
    )
    bullets(
        c,
        "Trinidad",
        "The difference is who picks up",
        [
            "Davyn is the local partner",
            "Onboarding with someone in Trinidad",
            "An account manager who stays after go-live",
            "A typical rollout is measured in weeks",
        ],
        11,
        "The only HRIS with local support in Trinidad.",
    )
    bullets(
        c,
        "Proof",
        "KennScott Limited",
        [
            "Certification, medical, and contract expiry live in the system",
            "Profiles, contracts, and attendance in one place, signed online",
            "Reminders for people the HR team rarely sees",
            "Learning sits in Factorial, with room for offshore safety training",
            "Leave and time already run day to day",
        ],
        12,
        lede="Offshore crew. A five-person HR team, going first.",
    )
    film(c, 13)
    game(c, "Everyone plays", "Kahoot", "Power banks. Every answer was said in this room.", "Seven questions", 14)
    game(c, "Second round", "Non-clients only", "Clients sit this one out.", "Four questions", 15)
    qa(c, 16)
    suggestions(c, 17)
    close(c, 18)
    stop(c)
    host_say(
        c,
        "Updates, then the product",
        [
            ("Open", "Start with what is new. Clients, this is what you can use now. Non-clients, listen for the job you still do by hand. Two items are not live yet."),
            ("From a file", "The old way was a spreadsheet, then a template, then someone pasting names. The upload is the setup."),
            ("Open shift", "Pause here. The system calls the person who can take the shift, in their language. It does not hand the manager a list."),
            ("Payroll", "Find the break between Factorial and the payroll provider, then fix it."),
            ("Accruals", "You see the balance move before anyone’s vacation changes."),
            ("This quarter", "Do not demo culture fit or onboarding simulation as live. They are in by the end of Q4."),
            ("What clients use", "These five are what KennScott is already running: time, documents, records, learning, reminders. Ask a client which of these they open."),
            ("Two differences", "Among HRIS, the only agentic AI. In Trinidad, the only HRIS with local support. Pause on each card."),
        ],
    )
    host_say(
        c,
        "KennScott through the close",
        [
            ("One", "A normal HR tool stores the process. One runs the step. It drafts, routes, checks, and asks before it acts. Say the line: the only agentic AI among HRIS."),
            ("Trinidad", "Davyn is the local partner. Implementation and the first payroll cycle sit in Trinidad. The account manager stays after go-live. Say the line: the only HRIS with local support in Trinidad."),
            ("KennScott", "Davyn made the introduction and stayed through onboarding. They started with the HR team of five. The offshore rollout comes after. The features on the previous slides are the ones in the film."),
            ("Spelling", "KennScott Limited. Two n’s. The film slide is your cue. Do not talk over it."),
            ("Kahoot", "Play before the Q&A, while the film is still fresh. Power banks. Everyone first. Then non-clients only, so they are not scoring against people who use it every week."),
            ("Q&A", "Non-clients ask. Clients answer from use, including what was annoying. Add a product fact only when the room needs it."),
            ("Cards", "One sentence each. Clients: what is still missing. Non-clients: what they would need to see before they moved. Read a few out loud."),
            ("Close", "Suggestion card on the way out. Clients, the account manager has the updates. Non-clients, name the spreadsheet they still run."),
        ],
    )
    host_qa(
        c,
        "Kahoot",
        "Everyone. Seven questions.",
        [
            ("What separates Factorial from other HRIS?", "The only agentic AI among HRIS."),
            ("What separates Factorial in Trinidad?", "The only HRIS with local support in Trinidad."),
            ("KennScott started with which team?", "The five-person HR team, before the offshore rollout."),
            ("Name one record KennScott stopped tracking from memory.", "Certifications, medicals, or contracts."),
            ("Which module replaced a separate learning platform?", "The built-in LMS."),
            ("How do you create a job catalog now?", "Upload a document. Factorial builds the roles, bands, and categories."),
            ("Which two are not live yet?", "Culture fit and onboarding simulation. Both by the end of Q4."),
        ],
    )
    host_qa(
        c,
        "Bonus Kahoot",
        "Non-clients only. Four questions.",
        [
            ("Name three core modules.", "Any three: time, talent, documents, expenses, learning, One."),
            ("What is the Trinidad difference, in one line?", "The only HRIS with local support in Trinidad."),
            ("What should you ask a client here before a demo?", "What they stopped doing by hand."),
            ("An open shift needs cover. What does Factorial do?", "It calls people, in their language, to take it."),
        ],
        extra="If someone asks. German qualified reference letters, interim or final, export to PDF or a document. That one is live, and it is built for Germany. The payroll example in the source video is ATR Nova in Spain. The point in this room is the flag and the fix. The benefit example is a meal subsidy in Portugal. The point is that the employee sees the allowance that applies to them.",
        last=True,
    )
    c.save()
    print(OUT)


if __name__ == "__main__":
    main()
