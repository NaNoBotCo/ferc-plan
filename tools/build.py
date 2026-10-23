#!/usr/bin/env python3
"""Builds the FERC plan minisite: docs/index.html (English), docs/de/ (German),
and docs/board/ + docs/de/board/ (one printable page for the board).

Words live in WORDS below. Edit there, then run: python3 tools/build.py
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
URL = "https://nanobotco.github.io/ferc-plan/"
MAP = "https://hongdam.net/for/eveline/#map"

WORDS = {
    "en": {
        "lang": "en",
        "voice": "en-GB",
        "title": "FERC · Giving season plan",
        "desc": "A five-step plan for FERC: donors in every country, a newsletter list with room to grow, the website and school map, more people seeing FERC, and lighter sponsor reports.",
        "skip": "Skip to the plan",
        "other": ("Deutsch", "de/"),
        "aa": "Text size",
        "theme": "Light or dark",
        "read": "Read aloud",
        "stop": "Stop",
        "kick": "For Eveline Willi and Heinz · Monday 26 October 2026, 7 pm",
        "h1": "More gifts for FERC by 29 November",
        "lede": "A plan in five steps. You approve; we do the work. Steps 1, 2 and 4 fit before your talk on 28 November and the fundraiser on 29 November. The website and the reports wait for January, when you have more time.",
        "board_btn": "One page for the board",
        "road": "A hill road in Chiang Mai province",
        "told_h": "You told us",
        "told": [
            "First: banking and donations. Then: recognition and social media.",
            "In six months: many more donations, and many more clicks.",
            "You are busy until the new year.",
            "The board decides. It meets on 31 October.",
            "The website stays on WordPress. You and Heinz keep it up to date.",
            "English first. Thai, perhaps.",
            "Schools and students: through CMSEO only.",
        ],
        "plan_h": "The plan",
        "we": "We do",
        "you": "You do",
        "when": "When",
        "cost": "Cost to FERC",
        "steps": [
            {
                "h": "Every donor can give, in their own country",
                "p": "We take the Myriad exit off your desk. fercthailand.org gets one clear “How to give” box per country, with a note on tax receipts.",
                "table": [
                    ("Thailand", "Bank transfer, as today. A Thai tax deduction for a gift to a foundation now goes through the Revenue Department’s e-Donation system; we check with the treasurer whether FERC is registered, and help register if not."),
                    ("Switzerland", "Bank transfer with a Swiss tax receipt, as today. Clearer on the website."),
                    ("USA", "CAF America, a US charity, passes gifts on to FERC; the donor gets a US tax receipt. FERC’s Every.org page runs through Myriad USA, so it may stop when FERC leaves Myriad."),
                    ("Australia", "A partner that already has Australian tax status, such as Global Development Group. This takes longer than November; until then, direct transfer."),
                    ("UK, Netherlands, others", "Direct transfer to FERC’s Thai account, for example with Wise. No tax receipt in the donor’s country."),
                ],
                "we": "Compare the routes with their costs and set-up time. Prepare the papers for leaving Myriad and for the new routes. Write a short email to US and Australian donors. Build the “How to give” page.",
                "you": "The treasurer’s answer on e-Donation. Your signature on the applications.",
                "when": "November, before the 28th",
                "cost": "CAF America takes a fee from each gift; we ask them for a quote.",
            },
            {
                "h": "A newsletter list with room to grow",
                "p": "MailPoet’s free plan stops at 500 contacts. Brevo’s free plan has no contact limit and sends 300 emails a day. A 500-person newsletter goes to the first 300 on day one; the next day, one click in Brevo sends the rest. The free plan shows a small Brevo logo.",
                "we": "Move the list to Brevo, unsubscribes included. Make a FERC newsletter template and a signup form on fercthailand.org. Write a one-page guide.",
                "you": "Approve, then send newsletters yourself.",
                "when": "November",
                "cost": "Free",
            },
            {
                "h": "fercthailand.org, refreshed inside WordPress, with the school map",
                "p": "Yes, everything stays on WordPress. You and Heinz edit it as you do now.",
                "list": [
                    "A “Sponsor a student” button on every page",
                    "The “How to give” page from step 1",
                    "Student stories, from students who ticked yes in the consent box",
                    "The school map: 34 schools, each with name, district and photo",
                    "Faster on phones",
                    "Thai as a second language, if you want it",
                    "A short guide, and one hour together to hand it over",
                ],
                "map": "See the map",
                "we": "Build it inside your WordPress, with our own login.",
                "you": "Tell us the hosting company, theme and plugins. Give us a login of our own.",
                "when": "January",
                "cost": "Hosting, as today",
            },
            {
                "h": "More people see FERC",
                "list": [
                    "Two posts a week on Facebook and LinkedIn, November and December, around the talk, the fundraiser and Christmas",
                    "A short video from the school map: “34 schools, one province”",
                    "Google Ad Grants: up to US$10,000 a month in free Google search ads for charities that qualify. We check whether FERC does, and apply.",
                    "A count of website visits and donation clicks, for the board",
                ],
                "we": "Draft every post and the video. Apply for Ad Grants.",
                "you": "Approve each post.",
                "when": "November and December",
                "cost": "Free",
            },
            {
                "h": "From January: sponsor reports in less time",
                "p": "Today Heinz collects about 100 student reports twice a year, you turn them into sponsor reports, and the master list and the treasurer’s list are kept apart.",
                "list": [
                    "One shared list in place of two, with a column for each student’s consent",
                    "A student’s report typed in once; the sponsor’s report comes out ready to send",
                    "One view of which reports are in, which are missing, which are sent",
                ],
                "p2": "It holds details of minors, so it is private to the FERC team, and works through CMSEO and the schools as now.",
                "when": "From January, if the board wants it",
                "cost": "To be agreed with the board",
            },
        ],
        "dao": "Doi Chiang Dao in the clouds",
        "time_h": "When",
        "time": [
            ("31 Oct", "Board meeting"),
            ("November", "Steps 1, 2 and 4 begin"),
            ("28 Nov", "Your Expat Club talk"),
            ("29 Nov", "Fundraiser"),
            ("December", "Posts, newsletter, Christmas"),
            ("January", "Steps 3 and 5"),
        ],
        "priv_h": "Students’ privacy",
        "priv": [
            "On the website: only what a student ticked yes to in the consent box.",
            "Students’ email, LINE and phone numbers stay off the website.",
            "Contact with schools and students goes through CMSEO, as today.",
        ],
        "q_h": "Questions for Monday",
        "q": [
            "What did you think of the school map?",
            "Leaving Myriad: which part is hardest, the legal side, the bank, or telling donors?",
            "May we ask the treasurer about e-Donation and online payment?",
            "Which hosting company, theme and plugins does the website use?",
            "Does FERC already use Google for Nonprofits or Canva for Nonprofits?",
            "Is there a budget for paid tools, or free tools only?",
        ],
        "who_h": "Who we are",
        "who": "NaN, Marcus (Myat Kaung Thant) and Michael, Chiang Mai.",
        "write": "Write to NaN",
        "fee_h": "Our work",
        "fee": [
            "Steps 1 to 4: no charge to FERC.",
            "Step 5: a price agreed with the board in January.",
            "Introductions: when someone you introduce becomes our client, 20% of their first year’s fees goes to FERC as a gift for students.",
        ],
        "src_h": "Sources",
        "photos": "Photos",
        "board_title": "FERC · Plan for the board, 31 October 2026",
        "board_lede": "Five steps. The volunteers approve; our team does the work.",
        "board_ask": "For the board: steps 1, 2 and 4 in November, before the talk and the fundraiser. Steps 3 and 5 in January.",
        "board_cols": ("Step", "When", "Cost to FERC"),
        "board_short": [
            "Every donor can give in their own country: Thailand (e-Donation), Switzerland, USA (CAF America), Australia (a partner), others (direct transfer)",
            "Newsletter list moved from MailPoet to Brevo (free, no contact limit)",
            "fercthailand.org refreshed inside WordPress, with the school map",
            "More people see FERC: posts, a short video, Google Ad Grants",
            "Sponsor reports in less time: one shared list, reports made from it",
        ],
        "print": "Print",
        "back": "Back to the plan",
    },
    "de": {
        "lang": "de-CH",
        "voice": "de-CH",
        "title": "FERC · Plan für die Spendenzeit",
        "desc": "Ein Plan in fünf Schritten für FERC: Spenden aus jedem Land, eine Newsletter-Liste mit Platz zum Wachsen, die Website mit der Schulkarte, mehr Sichtbarkeit und leichtere Berichte an die Paten.",
        "skip": "Zum Plan springen",
        "other": ("English", "../"),
        "aa": "Schriftgrösse",
        "theme": "Hell oder dunkel",
        "read": "Vorlesen",
        "stop": "Stopp",
        "kick": "Für Eveline Willi und Heinz · Montag, 26. Oktober 2026, 19 Uhr",
        "h1": "Mehr Spenden für FERC bis zum 29. November",
        "lede": "Ein Plan in fünf Schritten. Sie geben das Okay; wir machen die Arbeit. Die Schritte 1, 2 und 4 passen vor Ihren Vortrag am 28. November und den Spendenanlass am 29. November. Die Website und die Berichte warten bis Januar, wenn Sie mehr Zeit haben.",
        "board_btn": "Eine Seite für den Vorstand",
        "road": "Eine Bergstrasse in der Provinz Chiang Mai",
        "told_h": "Was Sie uns gesagt haben",
        "told": [
            "Zuerst: Bank und Spenden. Danach: Bekanntheit und soziale Medien.",
            "In sechs Monaten: viel mehr Spenden und viel mehr Klicks.",
            "Bis zum neuen Jahr haben Sie wenig Zeit.",
            "Der Vorstand entscheidet. Er trifft sich am 31. Oktober.",
            "Die Website bleibt auf WordPress. Sie und Heinz halten sie aktuell.",
            "Zuerst Englisch. Vielleicht Thai.",
            "Schulen und Schüler: nur über das CMSEO.",
        ],
        "plan_h": "Der Plan",
        "we": "Wir machen",
        "you": "Sie machen",
        "when": "Wann",
        "cost": "Kosten für FERC",
        "steps": [
            {
                "h": "Jeder Spender kann spenden, aus seinem eigenen Land",
                "p": "Wir nehmen Ihnen den Ausstieg bei Myriad ab. Auf fercthailand.org gibt es pro Land ein klares Feld «So können Sie spenden», mit einem Hinweis zur Steuerbescheinigung.",
                "table": [
                    ("Thailand", "Banküberweisung wie heute. Ein thailändischer Steuerabzug für eine Spende an eine Stiftung läuft jetzt über das e-Donation-System der Steuerbehörde; wir klären mit dem Kassier, ob FERC eingetragen ist, und helfen beim Eintrag, falls nicht."),
                    ("Schweiz", "Banküberweisung mit Schweizer Steuerbescheinigung, wie heute. Klarer auf der Website."),
                    ("USA", "CAF America, eine amerikanische Stiftung, leitet Spenden an FERC weiter; der Spender erhält eine US-Steuerbescheinigung. Die Every.org-Seite von FERC läuft über Myriad USA und hört deshalb vielleicht auf, wenn FERC Myriad verlässt."),
                    ("Australien", "Ein Partner mit australischem Steuerstatus, zum Beispiel Global Development Group. Das dauert länger als bis November; bis dahin direkte Überweisung."),
                    ("Grossbritannien, Niederlande, andere", "Direkte Überweisung auf das thailändische Konto von FERC, zum Beispiel mit Wise. Keine Steuerbescheinigung im Land des Spenders."),
                ],
                "we": "Die Wege mit Kosten und Dauer vergleichen. Die Unterlagen für den Ausstieg bei Myriad und für die neuen Wege vorbereiten. Eine kurze E-Mail an die Spender in den USA und in Australien schreiben. Die Seite «So können Sie spenden» bauen.",
                "you": "Die Antwort des Kassiers zu e-Donation. Ihre Unterschrift auf den Anträgen.",
                "when": "November, vor dem 28.",
                "cost": "CAF America nimmt eine Gebühr pro Spende; wir fragen nach einem Angebot.",
            },
            {
                "h": "Eine Newsletter-Liste mit Platz zum Wachsen",
                "p": "Der Gratis-Plan von MailPoet endet bei 500 Kontakten. Der Gratis-Plan von Brevo hat keine Kontaktgrenze und verschickt 300 E-Mails pro Tag. Ein Newsletter an 500 Personen geht am ersten Tag an 300; am nächsten Tag schickt ein Klick in Brevo den Rest. Im Gratis-Plan steht ein kleines Brevo-Logo.",
                "we": "Die Liste zu Brevo umziehen, mit allen Abmeldungen. Eine FERC-Vorlage und ein Anmeldeformular auf fercthailand.org machen. Eine Anleitung auf einer Seite schreiben.",
                "you": "Das Okay geben, dann Newsletter selbst verschicken.",
                "when": "November",
                "cost": "Gratis",
            },
            {
                "h": "fercthailand.org, erneuert in WordPress, mit der Schulkarte",
                "p": "Ja, alles bleibt auf WordPress. Sie und Heinz bearbeiten die Seite wie bisher.",
                "list": [
                    "Ein Knopf «Patenschaft übernehmen» auf jeder Seite",
                    "Die Seite «So können Sie spenden» aus Schritt 1",
                    "Geschichten von Schülern, die im Einwilligungsfeld Ja angekreuzt haben",
                    "Die Schulkarte: 34 Schulen, jede mit Name, Bezirk und Foto",
                    "Schneller auf dem Handy",
                    "Thai als zweite Sprache, wenn Sie das möchten",
                    "Eine kurze Anleitung und eine Stunde zusammen für die Übergabe",
                ],
                "map": "Die Karte ansehen",
                "we": "Alles in Ihrem WordPress bauen, mit einem eigenen Login.",
                "you": "Uns Hosting-Firma, Theme und Plugins nennen. Uns ein eigenes Login geben.",
                "when": "Januar",
                "cost": "Hosting wie heute",
            },
            {
                "h": "Mehr Menschen sehen FERC",
                "list": [
                    "Zwei Beiträge pro Woche auf Facebook und LinkedIn, im November und Dezember, rund um den Vortrag, den Spendenanlass und Weihnachten",
                    "Ein kurzes Video aus der Schulkarte: «34 Schulen, eine Provinz»",
                    "Google Ad Grants: bis zu 10’000 US-Dollar pro Monat an Gratis-Werbung in der Google-Suche für berechtigte gemeinnützige Organisationen. Wir prüfen, ob FERC berechtigt ist, und stellen den Antrag.",
                    "Eine Zählung der Website-Besuche und Spenden-Klicks, für den Vorstand",
                ],
                "we": "Jeden Beitrag und das Video entwerfen. Ad Grants beantragen.",
                "you": "Jeden Beitrag freigeben.",
                "when": "November und Dezember",
                "cost": "Gratis",
            },
            {
                "h": "Ab Januar: Berichte an die Paten in weniger Zeit",
                "p": "Heute sammelt Heinz zweimal im Jahr rund 100 Schülerberichte, Sie machen daraus die Berichte für die Paten, und die Hauptliste und die Liste des Kassiers werden getrennt geführt.",
                "list": [
                    "Eine gemeinsame Liste statt zwei, mit einer Spalte für die Einwilligung jedes Schülers",
                    "Der Bericht eines Schülers wird einmal eingetippt; der Bericht für den Paten kommt versandbereit heraus",
                    "Eine Übersicht: welche Berichte da sind, welche fehlen, welche verschickt sind",
                ],
                "p2": "Die Liste enthält Angaben über Minderjährige; sie ist deshalb nur für das FERC-Team zugänglich und läuft wie heute über das CMSEO und die Schulen.",
                "when": "Ab Januar, wenn der Vorstand es möchte",
                "cost": "Mit dem Vorstand zu besprechen",
            },
        ],
        "dao": "Doi Chiang Dao in den Wolken",
        "time_h": "Wann",
        "time": [
            ("31. Okt.", "Vorstandssitzung"),
            ("November", "Schritte 1, 2 und 4 beginnen"),
            ("28. Nov.", "Ihr Vortrag im Expat Club"),
            ("29. Nov.", "Spendenanlass"),
            ("Dezember", "Beiträge, Newsletter, Weihnachten"),
            ("Januar", "Schritte 3 und 5"),
        ],
        "priv_h": "Schutz der Schüler",
        "priv": [
            "Auf der Website: nur, wozu ein Schüler im Einwilligungsfeld Ja angekreuzt hat.",
            "E-Mail, LINE und Telefonnummern der Schüler stehen nicht auf der Website.",
            "Kontakt mit Schulen und Schülern läuft über das CMSEO, wie heute.",
        ],
        "q_h": "Fragen für Montag",
        "q": [
            "Wie hat Ihnen die Schulkarte gefallen?",
            "Ausstieg bei Myriad: Was ist am schwierigsten, das Rechtliche, die Bank oder die Information an die Spender?",
            "Dürfen wir den Kassier nach e-Donation und Online-Zahlung fragen?",
            "Welche Hosting-Firma, welches Theme und welche Plugins nutzt die Website?",
            "Nutzt FERC schon Google for Nonprofits oder Canva for Nonprofits?",
            "Gibt es ein Budget für bezahlte Werkzeuge, oder nur gratis?",
        ],
        "who_h": "Wer wir sind",
        "who": "NaN, Marcus (Myat Kaung Thant) und Michael, Chiang Mai.",
        "write": "NaN schreiben",
        "fee_h": "Unsere Arbeit",
        "fee": [
            "Schritte 1 bis 4: ohne Kosten für FERC.",
            "Schritt 5: ein Preis, den wir im Januar mit dem Vorstand vereinbaren.",
            "Empfehlungen: Wenn jemand, den Sie uns vorstellen, unser Kunde wird, gehen 20 % seiner Gebühren im ersten Jahr als Spende für die Schüler an FERC.",
        ],
        "src_h": "Quellen",
        "photos": "Fotos",
        "board_title": "FERC · Plan für den Vorstand, 31. Oktober 2026",
        "board_lede": "Fünf Schritte. Die Freiwilligen geben das Okay; unser Team macht die Arbeit.",
        "board_ask": "Für den Vorstand: Schritte 1, 2 und 4 im November, vor dem Vortrag und dem Spendenanlass. Schritte 3 und 5 im Januar.",
        "board_cols": ("Schritt", "Wann", "Kosten für FERC"),
        "board_short": [
            "Jeder Spender kann aus seinem Land spenden: Thailand (e-Donation), Schweiz, USA (CAF America), Australien (ein Partner), andere (direkte Überweisung)",
            "Newsletter-Liste von MailPoet zu Brevo (gratis, ohne Kontaktgrenze)",
            "fercthailand.org erneuert in WordPress, mit der Schulkarte",
            "Mehr Menschen sehen FERC: Beiträge, ein kurzes Video, Google Ad Grants",
            "Berichte an die Paten in weniger Zeit: eine gemeinsame Liste, Berichte daraus",
        ],
        "print": "Drucken",
        "back": "Zurück zum Plan",
    },
}

SOURCES = [
    ("CAF America: Friends Funds", "https://cafamerica.org/friends-funds/"),
    ("DFAT: Overseas Aid Gift Deduction Scheme", "https://www.dfat.gov.au/development/who-we-work-with/ngos/oagds"),
    ("Global Development Group (Australia)", "https://globaldevelopmentgroup.org/au/help/"),
    ("THE STANDARD: donations to foundations through e-Donation from 1 January 2026", "https://thestandard.co/donation-tax-deduction-e-donation-2026/"),
    ("Revenue Department: e-Donation", "https://www.rd.go.th/region/04/saraburi/85/6565.html"),
    ("Brevo pricing", "https://www.brevo.com/pricing/"),
    ("Google for Nonprofits: Ad Grants", "https://www.google.com/grants/"),
    ("Myriad USA (formerly King Baudouin Foundation United States)", "https://myriadusa.org/"),
]

PHOTOS = [
    ("road", "Takeaway", "https://commons.wikimedia.org/wiki/File:Chiang_mai_province_road_1263.jpg", "CC BY 3.0", "https://creativecommons.org/licenses/by/3.0"),
    ("dao", "Takeaway", "https://commons.wikimedia.org/wiki/File:Doi_Chiang_Dao_in_the_clouds.jpg", "CC BY-SA 3.0", "https://creativecommons.org/licenses/by-sa/3.0"),
]

e = html.escape


def head(w, rel, title, path):
    other_label, other_href = w["other"]
    return f"""<!doctype html>
<html lang="{w['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<meta name="google" content="notranslate">
<title>{e(title)}</title>
<meta name="description" content="{e(w['desc'])}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(w['desc'])}">
<meta property="og:type" content="website">
<meta property="og:url" content="{URL}{path}">
<meta property="og:image" content="{URL}img/card.jpg">
<meta property="og:image:alt" content="{e(w['road'])}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&display=swap">
<link rel="stylesheet" href="{rel}style.css">
<script>try{{var s=JSON.parse(localStorage.getItem('ferc')||'{{}}');if(s.big)document.documentElement.classList.add('big');if(s.theme)document.documentElement.dataset.theme=s.theme}}catch(_){{}}</script>
</head>
<body data-voice="{w['voice']}" data-read="{e(w['read'])}" data-stop="{e(w['stop'])}">
<a class="skip" href="#plan">{e(w['skip'])}</a>
<div class="bar">
  <a class="btn" href="{other_href}" lang="{'de' if w['lang']=='en' else 'en'}">{e(other_label)}</a>
  <button class="btn" type="button" id="aa" aria-pressed="false">A<span class="a2">A</span> <span class="lbl">{e(w['aa'])}</span></button>
  <button class="btn" type="button" id="theme"><span aria-hidden="true">◐</span> <span class="lbl">{e(w['theme'])}</span></button>
</div>
"""


def readbtn(w):
    return f'<button class="read" type="button" aria-label="{e(w["read"])}"><span aria-hidden="true">🔊</span> {e(w["read"])}</button>'


def foot(w, rel):
    src = "".join(f'<li><a href="{u}">{e(t)}</a></li>' for t, u in SOURCES)
    ph = " · ".join(
        f'{e(w[k])} · {e(a)} · <a href="{u}">Wikimedia Commons</a> · <a href="{lu}">{e(l)}</a>'
        for k, a, u, l, lu in PHOTOS
    )
    fee = "".join(f"<li>{e(x)}</li>" for x in w["fee"])
    return f"""<section class="sec" aria-labelledby="fee-h"><div class="wrap">
  <div class="hrow"><h2 id="fee-h">{e(w['fee_h'])}</h2>{readbtn(w)}</div>
  <ul class="told">{fee}</ul>
</div></section>
<section class="sec" aria-labelledby="who-h"><div class="wrap">
  <h2 id="who-h">{e(w['who_h'])}</h2>
  <p>{e(w['who'])}</p>
  <p><a class="cta" href="mailto:nan@motdang.net?subject=FERC">{e(w['write'])}: nan@motdang.net</a></p>
</div></section>
<footer class="wrap foot">
  <h2>{e(w['src_h'])}</h2>
  <ul>{src}</ul>
  <p class="small">{e(w['photos'])}: {ph}</p>
</footer>
<script src="{rel}app.js"></script>
</body>
</html>
"""


def step_html(w, i, s):
    out = [f'<li class="step" id="step{i}"><div class="num" aria-hidden="true">{i}</div><div class="body">']
    out.append(f'<h3>{e(s["h"])}</h3>')
    if "p" in s:
        out.append(f"<p>{e(s['p'])}</p>")
    if "table" in s:
        rows = "".join(f'<tr><th scope="row">{e(a)}</th><td>{e(b)}</td></tr>' for a, b in s["table"])
        out.append(f'<table class="routes"><tbody>{rows}</tbody></table>')
    if "list" in s:
        out.append("<ul>" + "".join(f"<li>{e(x)}</li>" for x in s["list"]) + "</ul>")
    if "map" in s:
        out.append(f'<p><a class="cta" href="{MAP}">{e(s["map"])} →</a></p>')
    if "p2" in s:
        out.append(f"<p>{e(s['p2'])}</p>")
    dl = []
    for k in ("we", "you", "when", "cost"):
        if k in s:
            dl.append(f"<div><dt>{e(w[k])}</dt><dd>{e(s[k])}</dd></div>")
    out.append(f'<dl class="facts">{"".join(dl)}</dl>')
    out.append("</div></li>")
    return "".join(out)


def page(w, rel, path):
    told = "".join(f"<li>{e(x)}</li>" for x in w["told"])
    steps = "".join(step_html(w, i + 1, s) for i, s in enumerate(w["steps"]))
    time = "".join(f'<li><span class="d">{e(a)}</span> <span>{e(b)}</span></li>' for a, b in w["time"])
    priv = "".join(f"<li>{e(x)}</li>" for x in w["priv"])
    q = "".join(f"<li>{e(x)}</li>" for x in w["q"])
    return head(w, rel, w["title"], path) + f"""
<header class="band" style="background-image:url({rel}img/road.jpg)">
  <div class="in">
    <p class="kick">{e(w['kick'])}</p>
    <h1>{e(w['h1'])}</h1>
    <p class="lede">{e(w['lede'])}</p>
    <p class="row"><a class="cta light" href="board/">{e(w['board_btn'])} →</a></p>
  </div>
  <p class="cred">{e(w['road'])}</p>
</header>
<main>
<section class="sec" aria-labelledby="told-h"><div class="wrap">
  <div class="hrow"><h2 id="told-h">{e(w['told_h'])}</h2>{readbtn(w)}</div>
  <ul class="told">{told}</ul>
</div></section>
<section class="sec" id="plan" aria-labelledby="plan-h"><div class="wrap">
  <div class="hrow"><h2 id="plan-h">{e(w['plan_h'])}</h2>{readbtn(w)}</div>
  <ol class="steps">{steps}</ol>
</div></section>
<div class="band short" style="background-image:url({rel}img/dao.jpg);background-position:center 40%" role="img" aria-label="{e(w['dao'])}"><p class="cred">{e(w['dao'])}</p></div>
<section class="sec" aria-labelledby="time-h"><div class="wrap">
  <div class="hrow"><h2 id="time-h">{e(w['time_h'])}</h2>{readbtn(w)}</div>
  <ol class="time">{time}</ol>
</div></section>
<section class="sec" aria-labelledby="priv-h"><div class="wrap">
  <div class="hrow"><h2 id="priv-h">{e(w['priv_h'])}</h2>{readbtn(w)}</div>
  <ul class="told">{priv}</ul>
</div></section>
<section class="sec alt" aria-labelledby="q-h"><div class="wrap">
  <div class="hrow"><h2 id="q-h">{e(w['q_h'])}</h2>{readbtn(w)}</div>
  <ol class="qs">{q}</ol>
</div></section>
</main>
""" + foot(w, rel)


def board(w, rel, path):
    c1, c2, c3 = w["board_cols"]
    rows = "".join(
        f'<tr><th scope="row"><span class="n">{i+1}</span> {e(t)}</th><td>{e(s["when"])}</td><td>{e(s["cost"])}</td></tr>'
        for i, (t, s) in enumerate(zip(w["board_short"], w["steps"]))
    )
    priv = "".join(f"<li>{e(x)}</li>" for x in w["priv"])
    return head(w, rel, w["board_title"], path) + f"""
<main class="wrap boardpage" id="plan">
  <p class="noprint"><a href="../">← {e(w['back'])}</a> · <button class="btn" type="button" onclick="window.print()">{e(w['print'])}</button></p>
  <h1>{e(w['board_title'])}</h1>
  <p class="lede">{e(w['board_lede'])}</p>
  <table class="board"><thead><tr><th scope="col">{e(c1)}</th><th scope="col">{e(c2)}</th><th scope="col">{e(c3)}</th></tr></thead><tbody>{rows}</tbody></table>
  <p class="ask">{e(w['board_ask'])}</p>
  <h2>{e(w['fee_h'])}</h2>
  <ul>{"".join(f"<li>{e(x)}</li>" for x in w["fee"])}</ul>
  <h2>{e(w['priv_h'])}</h2>
  <ul>{priv}</ul>
  <p class="small">{e(w['who'])} nan@motdang.net · {URL}</p>
</main>
<script src="{rel}app.js"></script>
</body>
</html>
"""


def write(p, s):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")


write(DOCS / "index.html", page(WORDS["en"], "", ""))
write(DOCS / "de/index.html", page(WORDS["de"], "../", "de/"))
board_en = WORDS["en"] | {"other": ("Deutsch", "../de/board/")}
board_de = WORDS["de"] | {"other": ("English", "../../board/")}
write(DOCS / "board/index.html", board(board_en, "../", "board/"))
write(DOCS / "de/board/index.html", board(board_de, "../../", "de/board/"))
print("built", *sorted(str(p.relative_to(ROOT)) for p in DOCS.rglob("*.html")))
