#!/usr/bin/env python3
"""Builds the FERC plan minisite: docs/index.html (English), docs/de/ (German),
and docs/board/ + docs/de/board/ (one printable page for the board, with boxes to tick).

Words live in WORDS below, English and German side by side. Edit there, then run:
python3 tools/build.py
"""
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
URL = "https://nanobotco.github.io/ferc-plan/"
DESK = "https://hongdam.net/for/eveline/"
MAP = DESK + "#map"
MAIL = "nan@motdang.net"

# Extras: id, price once (baht), price a month (baht). Words are in WORDS[...]["extras"].
EXTRAS = [
    ("book", 0, 3000),
    ("posts", 0, 3000),
    ("kit", 5000, 0),
    ("ads", 0, 2000),
    ("alumni", 3000, 0),
    ("usf", 5000, 0),
    ("thai", 10000, 0),
    ("wpcare", 0, 2000),
]

WORDS = {
    "en": {
        "lang": "en",
        "voice": "en-GB",
        "title": "FERC · Plan for donations",
        "desc": "A plan in five steps for FERC: ways to give from each country, a newsletter for more than 500 people, the website with the school map, more people seeing FERC, and sponsor reports with less work.",
        "skip": "Skip to the plan",
        "other": ("Deutsch", "de/"),
        "aa": "Text size",
        "theme": "Light or dark",
        "read": "Read aloud",
        "stop": "Stop",
        "kick": "For Eveline Willi and Heinz · Monday 26 October 2026, 7 pm",
        "h1": "More donations for FERC: a plan in five steps",
        "lede": [
            "Our work on steps 1 to 4 is free for FERC.",
            "FERC’s board decides on 31 October. Then we do the work, and you say yes to each part.",
        ],
        "go_choose": "Choose and send",
        "board_btn": "Page for the board",
        "road": "A hill road in Chiang Mai province",
        "who_h": "Who we are",
        "who": [
            "Hongdam is a small web company in Chiang Mai and Chiang Rai. We are six people: Thai, Burmese and American.",
            "We build websites and online tools in Thai and English, for companies, charities and clubs. We also run motdang.net, a guide to Chiang Mai.",
            "For FERC we already made a sample giving page and a map of the 34 schools.",
            "At the meeting: NaN (your contact), Marcus (Myat Kaung Thant) and Michael.",
        ],
        "desk_btn": "See the sample giving page and map",
        "write": "Write to NaN",
        "told_h": "You told us",
        "told": [
            "First: banking and donations. Then: recognition and social media.",
            "In six months: many more donations, and much more exposure and clicks on social media.",
            "You are busy until the new year.",
            "You would like the board to agree. It meets on 31 October.",
            "The website stays on WordPress. You and Heinz keep it up to date.",
            "English first. Thai, perhaps.",
            "Schools and students: through CMSEO only.",
        ],
        "time_h": "When",
        "time": [
            ("31 Oct", "FERC board meeting: yes or no"),
            ("November", "1 🌍 Ways to give · 2 ✉️ Newsletter · 4 📣 More people see FERC"),
            ("28 Nov", "Your talk at the Expat Club"),
            ("29 Nov", "Fundraiser"),
            ("December", "Posts and newsletter for Christmas"),
            ("January", "3 🖥️ Website · 5 📋 Sponsor reports start"),
            ("March", "3 🖥️ Website and 5 📋 report tool ready, with a short guide"),
        ],
        "plan_h": "The plan",
        "we": "We do",
        "you": "You do",
        "when": "When",
        "cost": "Cost to FERC",
        "steps": [
            {
                "h": "Donations from each country",
                "short": "Donations from each country",
                "p": "FERC is leaving Myriad. (Myriad USA and Myriad Australia pass US and Australian gifts on to FERC today.) We help with that paperwork. Then we add a “How to give” page to fercthailand.org: one box per country, each saying whether the donor gets a tax receipt.",
                "table": [
                    ("Thailand", "Bank transfer, as now. Since 1 January 2026, a Thai tax deduction for a gift to a foundation goes through e-Donation, the Revenue Department’s online system. We ask the treasurer whether FERC is registered. If not, we find out how FERC can register."),
                    ("Switzerland", "Bank transfer with a Swiss tax receipt, as now. The website explains it more clearly."),
                    ("USA", "CAF America, a US charity, takes the gift, gives the donor a US tax receipt, and sends the money to FERC. FERC’s page on Every.org, a US giving website, works through Myriad USA, so it may close when FERC leaves Myriad."),
                    ("Australia", "An Australian charity that can give Australian tax receipts, such as Global Development Group, takes gifts for FERC. This is not ready in November. Until then: bank transfer to FERC’s Thai account."),
                    ("UK, Netherlands, others", "Bank transfer to FERC’s Thai account, for example with Wise, a money-transfer service. No tax receipt in the donor’s country."),
                ],
                "we": "Compare the ways to give, with costs and time. Prepare the papers for leaving Myriad and for CAF America. Write a short email to US and Australian donors. Build the “How to give” page.",
                "you": "Tell the treasurer we will ask about e-Donation. Give us an administrator login for fercthailand.org. Sign the applications. Send the email to donors.",  # stylecheck: allow — a task list for the client
                "when": "November, before the 28th",
                "cost": "Our work: free. CAF America keeps a fee from each US gift. We ask them how much.",
            },
            {
                "h": "A newsletter for more than 500 people",
                "short": "Newsletter moved to Brevo",
                "p": "MailPoet, your newsletter tool, is free up to 500 contacts, and FERC has reached 500. Brevo, another newsletter service, is free for more than 500 contacts. It sends 300 emails a day. So a newsletter to 500 people goes out over two days: 300 on the first day, the other 200 the next day with one more click. Free Brevo newsletters end with a small line, “Sent with Brevo”. (MailerLite, a similar service, is now free only up to 250 contacts.)",
                "we": "Move the list to Brevo. People who unsubscribed stay unsubscribed. Make a FERC newsletter design and a sign-up form on fercthailand.org. Write a one-page guide. The first newsletter tells donors about the new ways to give from step 1.",
                "you": "Say yes to the move. Then you send each newsletter. The guide shows how.",
                "when": "November",
                "cost": "Free",
            },
            {
                "h": "Website: new look, with the school map",
                "short": "Website refresh with the school map",
                "p": "You can choose where the new website runs.",
                "ab": [
                    ("A", "Website on WordPress, as now", "Stay on WordPress", "We build the new look inside FERC’s WordPress. You and Heinz edit it as now. Most security holes in WordPress are in plugins (add-ons): in 2025, 11,334 new holes were found, 91% of them in plugins. Attackers often use a new hole within 5 hours. So a WordPress site needs updates every week: see the extra “WordPress care”.", "Our work: free. FERC pays for hosting, as now."),
                    ("B", "Website on a simpler system", "Move to a simpler website that we host", "Same address, fercthailand.org. Fewer parts to update, so less to keep safe. You change the words on the page itself, as on the practice copy of your giving page. We move the old pages and pictures across.", "Our work: free. We host it at no charge today."),
                ],
                "rec": "We recommend B. If FERC prefers A, we build in WordPress.",  # stylecheck: allow — NaN asked for this recommendation (23 Oct)
                "list": [
                    "A “Sponsor a student” button on every page",
                    "The “How to give” page from step 1",
                    "Student stories, only from students who ticked yes on the permission box",
                    "The school map: 34 schools, each with name, district and photo",
                    "Faster on phones",
                    "A short guide, and one hour with you and Heinz to show how it works",
                ],
                "map": "See the school map",
                "we": "Build the new website, A or B.",
                "you": "Choose A or B. Tell us which company hosts the website today.",
                "when": "January",
                "cost": "Our work: free. A: FERC pays for hosting, as now. B: we host it at no charge today.",
            },
            {
                "h": "More people see FERC",
                "short": "Posts, a short video, Google Ad Grants",
                "list": [
                    "Two posts a week on Facebook and LinkedIn in November and December: the talk, the fundraiser, Christmas",
                    "A short video made from the school map’s photos",
                    "Google Ad Grants: free Google search ads for charities, up to US$10,000 a month. Google asks for a fast, secure website; step 3 gives FERC one. We check whether FERC can get them, and apply.",
                    "A count of website visits and clicks on “How to give”, for the board",
                ],
                "we": "Write the posts and make the video. Apply for Ad Grants.",
                "you": "Once a month, say yes to that month’s posts. FERC posts them, or gives us access to post.",
                "when": "November and December",
                "cost": "Free",
            },
            {
                "h": "From January: sponsor reports with less work",
                "short": "Sponsor reports with less work",
                "p": "Today: Heinz collects about 100 student reports, twice a year. You turn them into reports for sponsors. FERC keeps two lists: the master list and the treasurer’s list.",
                "list": [
                    "One shared list instead of two, with a column for each student’s permission",
                    "Type a student’s report once; the sponsor’s report is made from it.",
                    "One page showing which reports are in, missing or sent",
                ],
                "p2": "The list holds details of students under 18. FERC decides who can open it. Contact with schools goes through CMSEO, as now.",
                "when": "From January, if the board wants it",
                "cost": "A price we agree with the board in January",
            },
        ],
        "dao": "Doi Chiang Dao in the clouds",
        "ex_h": "Extras FERC can add",
        "ex_p": "Each extra is optional. Prices for FERC, in Thai baht. Up to half can be paid in trade.",
        "once": "once",
        "month": "a month",
        "stop_any": "stop any month",
        "extras": {
            "book": ("Gift record for the treasurer", "Each gift is one row: way of giving, fee, baht and Swiss francs. A thank-you to each donor. A statement for the board each month. Only if the treasurer wants it."),
            "posts": ("Posts from January to June", "Two posts a week after the free months. You say yes once a month."),
            "kit": ("Talk and fundraiser kit", "Large-print slides for your talk on 28 November. “How to give” cards with a QR code for each table on 29 November. A thank-you email to guests on 30 November."),
            "ads": ("Ad Grants care", "If Google says yes: we keep the free ads working within Google’s rules, and send the board one line a month."),
            "alumni": ("Alumni survey", "Questions for FERC alumni as a short form in Thai and English, in FERC’s own Google account."),
            "usf": ("Papers for US foundations", "The English papers a US foundation asks for before it gives to a charity abroad. Only if a US foundation is among FERC’s donors."),
            "thai": ("Thai website", "Thai pages beside the English ones, checked by a Thai speaker."),
            "wpcare": ("WordPress care", "For choice A: each week we update WordPress and its plugins, check for new security holes, and keep a backup."),
        },
        "tr_h": "Pay in trade",
        "tr_p": "FERC can pay up to half of any extra in trade instead of money. For example:",
        "trades": {
            "credit": "A line at the bottom of fercthailand.org, “Website and giving page: Hongdam”, one thank-you in the newsletter, and permission to show FERC’s pages as our work.",
            "thanks": "Our name on the thank-you slide and a table card at the fundraiser on 29 November.",
            "jobs": "Our job posts sent to FERC alumni who said yes to job news. Adults only. FERC sends them, not us.",
        },
        "tr_note": "Introductions are separate. They earn FERC money (next section).",
        "co_h": "For all of Chiang Mai",
        "co": [
            "Many Chiang Mai charities and clubs have donors abroad, as FERC does.",
            "Other groups can get a giving page like FERC’s. Gifts go to the group’s own bank account, with a record of each gift. Price for other groups: ฿30,000 to set up, then ฿10,000 a month, stop any month. For FERC, its giving page is part of step 1 and free.",
            "If you introduce someone who then hires us, for this or any other work, we give FERC 20% of what they pay us in their first year, as their payments reach us.",
        ],
        "intro_btn": "Introduce someone",
        "intro_subject": "An introduction: Hongdam",
        "intro_body": "Dear …,\n\nI would like to introduce NaN from Hongdam (copied here). They made FERC’s giving page and school map. I think they could help you with …\n\nIf you hire them, they give FERC 20% of what you pay them in the first year, for our students.\n\nBest wishes,\nEveline",
        "ch_h": "Choose and send",
        "nav_h": "On this page",
        "nav_extras": "Extras",
        "nav_trade": "Pay in trade",
        "nav_co": "For all of Chiang Mai",
        "nav_choose": "Choose and send",
        "float": "Choose",
        "step_of": "Step {n} of 5",
        "more": "More about step {n}",
        "pv_h": "Your email will say:",
        "pv_to": "To",
        "pv_subject": "Subject",
        "board_screen": "Print this page to tick it with a pen, or choose on the website.",
        "board_web": "Choose on the website",
        "board_or": "Choose one:",
        "ch_p": "Tick what FERC wants. Nothing is ticked yet. The board decides on 31 October; you can send a first choice now and change it later.",
        "ch_plan": "The plan: steps 1, 2 and 4 (free)",
        "ch_step5": "5 📋 Sponsor reports: talk in January",
        "ch_web": "3 🖥️ Website: choose one (free)",
        "ch_web_talk": "Talk first",
        "ch_wp_only": "🔒 Only with 3A, WordPress",
        "board_one": "Choose one: 3A or 3B",
        "ch_extras": "Extras",
        "ch_pay": "How FERC pays for extras",
        "pay": ["Money", "Half money, half trade", "Talk first"],
        "ch_trade": "Trade FERC could offer",
        "ch_groups": "Groups that may want the same giving page (names, optional)",
        "ch_name": "Your name",
        "ch_total": "Total for extras",
        "ch_none": "none",
        "ch_and": "and",
        "ch_money": "In money",
        "ch_send": "Send to NaN by email",
        "ch_copy": "Copy",
        "ch_help": "The button opens your email program with this text. Then press Send there. No email program? Press Copy and paste the text into any email to nan@motdang.net.",
        "ch_copied": "Copied. Paste it into an email to nan@motdang.net.",
        "ch_subject": "FERC: our choices",
        "ch_msg_h": "FERC’s choices",
        "priv_h": "Students’ privacy",
        "priv": [
            "On the website: only what a student ticked yes to on the permission box.",
            "Students’ email, LINE and phone numbers stay off the website.",
            "Contact with schools and students goes through CMSEO, as now.",
        ],
        "q_h": "Questions for you",
        "q_p": "Tap an answer. Your answers go in the same email as your choices.",
        "q_note": "Note (optional)",
        "q_answers": "Answers",
        "qa": [
            ("map", "What did you think of the school map?", "one", ["✓ Good as it is", "✎ Good, with changes", "? Not seen yet"], True),
            ("myriad", "Leaving Myriad: what is hardest?", "many", ["The legal side", "The bank", "Telling donors"], True),
            ("treasurer", "May we ask the treasurer about e-Donation?", "one", ["✓ Yes, ask the treasurer", "I will ask", "✗ Not now"], False),
            ("cards", "Does FERC want card payments on the website?", "one", ["✓ Yes", "✗ No", "? Not sure"], False),
            ("host", "Which company hosts the website today?", "one", ["? I don’t know"], True),
            ("tools", "Does FERC use these free tools for charities?", "many", ["Google for Nonprofits", "Canva for Nonprofits", "✗ Neither", "? I don’t know"], False),
            ("budget", "Is there money for paid tools?", "one", ["Free tools only", "Some money", "The board decides"], False),
        ],
        "src_h": "Sources",
        "photos": "Photos by Takeaway, a Wikimedia Commons user",
        "board_title": "FERC · Plan for the board, 31 October 2026",
        "board_lede": "Five steps from Hongdam. The board decides. Eveline says yes to each part. We do the work.",
        "board_ask": "For the board: yes or no to steps 1 to 4 (free) and to each extra. Step 5: we bring a price in January.",
        "board_cols": ("Yes", "No", "Step", "When", "Cost to FERC"),
        "board_tick": "Tick, add your name and the date, then send a photo of each page to nan@motdang.net.",
        "board_groups": "Groups that may want a giving page like FERC’s (other groups pay ฿30,000 to set up, then ฿10,000 a month):",
        "print": "Print",
        "board_sign": "Name: ____________________   Date: ____________",
        "back": "Back to the plan",
    },
    "de": {
        "lang": "de-CH",
        "voice": "de-CH",
        "title": "FERC · Plan für Spenden",
        "desc": "Ein Plan in fünf Schritten für FERC: Spenden aus jedem Land, ein Newsletter für mehr als 500 Personen, die Website mit der Schulkarte, mehr Sichtbarkeit und Patenberichte mit weniger Aufwand.",
        "skip": "Zum Plan springen",
        "other": ("English", "../"),
        "aa": "Schriftgrösse",
        "theme": "Hell oder dunkel",
        "read": "Vorlesen",
        "stop": "Stopp",
        "kick": "Für Eveline Willi und Heinz · Montag, 26. Oktober 2026, 19 Uhr",
        "h1": "Mehr Spenden für FERC: ein Plan in fünf Schritten",
        "lede": [
            "Unsere Arbeit für die Schritte 1 bis 4 ist für FERC gratis.",
            "Der Vorstand von FERC entscheidet am 31. Oktober. Dann machen wir die Arbeit, und Sie sagen Ja zu jedem Teil.",
        ],
        "go_choose": "Auswählen und senden",
        "board_btn": "Seite für den Vorstand",
        "road": "Eine Bergstrasse in der Provinz Chiang Mai",
        "who_h": "Wer wir sind",
        "who": [
            "Hongdam ist eine kleine Web-Firma in Chiang Mai und Chiang Rai. Wir sind sechs Personen: aus Thailand, Myanmar und den USA.",
            "Wir bauen Websites und Online-Werkzeuge auf Thai und Englisch, für Firmen, gemeinnützige Organisationen und Vereine. Wir betreiben auch motdang.net, einen Online-Stadtführer für Chiang Mai.",
            "Für FERC haben wir schon eine Muster-Spendenseite und eine Karte der 34 Schulen gemacht.",
            "Am Treffen: NaN (Ihre Ansprechperson), Marcus (Myat Kaung Thant) und Michael.",
        ],
        "desk_btn": "Muster-Spendenseite und Karte ansehen",
        "write": "NaN schreiben",
        "told_h": "Was Sie uns gesagt haben",
        "told": [
            "Zuerst: Bank und Spenden. Danach: Bekanntheit und soziale Medien.",
            "In sechs Monaten: viel mehr Spenden und viel mehr Sichtbarkeit und Klicks in den sozialen Medien.",
            "Bis zum neuen Jahr haben Sie wenig Zeit.",
            "Sie möchten, dass der Vorstand zustimmt. Er trifft sich am 31. Oktober.",
            "Die Website bleibt auf WordPress. Sie und Heinz halten sie aktuell.",
            "Zuerst Englisch. Vielleicht Thai.",
            "Schulen und Schüler: nur über das CMSEO.",
        ],
        "time_h": "Wann",
        "time": [
            ("31. Okt.", "Vorstandssitzung von FERC: Ja oder Nein"),
            ("November", "1 🌍 Wege zu spenden · 2 ✉️ Newsletter · 4 📣 Mehr Menschen sehen FERC"),
            ("28. Nov.", "Ihr Vortrag im Expat Club"),
            ("29. Nov.", "Spendenanlass"),
            ("Dezember", "Beiträge und Newsletter für Weihnachten"),
            ("Januar", "3 🖥️ Website · 5 📋 Patenberichte beginnen"),
            ("März", "3 🖥️ Website und 5 📋 Berichts-Werkzeug bereit, mit einer kurzen Anleitung"),
        ],
        "plan_h": "Der Plan",
        "we": "Wir machen",
        "you": "Sie machen",
        "when": "Wann",
        "cost": "Kosten für FERC",
        "steps": [
            {
                "h": "Spenden aus jedem Land",
                "short": "Spenden aus jedem Land",
                "p": "FERC verlässt Myriad. (Myriad USA und Myriad Australia leiten heute Spenden aus den USA und Australien an FERC weiter.) Wir helfen bei den Unterlagen für den Ausstieg. Dann kommt auf fercthailand.org eine Seite «So können Sie spenden», mit einem Abschnitt pro Land. Jeder Abschnitt sagt, ob es eine Spendenbestätigung gibt.",
                "table": [
                    ("Thailand", "Banküberweisung wie heute. Seit dem 1. Januar 2026 läuft ein thailändischer Steuerabzug für eine Spende an eine Stiftung über e-Donation, das Online-System der Steuerbehörde. Wir fragen den Kassier, ob FERC eingetragen ist. Falls nicht, klären wir, was für den Eintrag nötig ist."),
                    ("Schweiz", "Banküberweisung mit Schweizer Spendenbestätigung, wie heute. Die Website erklärt es klarer."),
                    ("USA", "CAF America, eine gemeinnützige Organisation in den USA, nimmt die Spende an, gibt eine US-Spendenbestätigung und schickt das Geld an FERC. Die Seite von FERC auf Every.org, einer amerikanischen Spenden-Website, läuft über Myriad USA und wird deshalb vielleicht eingestellt, wenn FERC Myriad verlässt."),
                    ("Australien", "Eine australische gemeinnützige Organisation, die australische Spendenbestätigungen ausstellen darf, zum Beispiel Global Development Group, nimmt Spenden für FERC an. Das dauert länger als bis November. Bis dahin: Überweisung auf das thailändische Konto von FERC."),
                    ("Grossbritannien, Niederlande, andere", "Überweisung auf das thailändische Konto von FERC, zum Beispiel mit Wise, einem Dienst für Geldüberweisungen. Keine Spendenbestätigung im Land des Spenders."),
                ],
                "we": "Die Wege vergleichen, mit Kosten und Dauer. Die Unterlagen für den Ausstieg bei Myriad und für CAF America vorbereiten. Eine kurze E-Mail an die Spender in den USA und Australien schreiben. Die Seite «So können Sie spenden» bauen.",
                "you": "Dem Kassier sagen, dass wir zu e-Donation fragen. Uns ein eigenes Administrator-Login für fercthailand.org geben. Die Anträge unterschreiben. Die E-Mail an die Spender schicken.",
                "when": "November, vor dem 28.",
                "cost": "Unsere Arbeit: gratis. CAF America verlangt eine Gebühr pro US-Spende. Wir verlangen eine Offerte.",
            },
            {
                "h": "Newsletter für mehr als 500 Personen",
                "short": "Newsletter zu Brevo",
                "p": "MailPoet, Ihr Newsletter-Programm, ist bis 500 Kontakte gratis, und FERC hat 500 erreicht. Brevo, ein anderer Newsletter-Dienst, ist auch für mehr als 500 Kontakte gratis. Brevo verschickt 300 E-Mails pro Tag. Ein Newsletter an 500 Personen geht also über zwei Tage: 300 am ersten Tag, die anderen 200 am nächsten Tag mit einem weiteren Klick. In der Gratisversion endet jeder Newsletter mit einer kleinen Zeile «Sent with Brevo». (MailerLite, ein ähnlicher Dienst, ist jetzt nur noch bis 250 Kontakte gratis.)",
                "we": "Die Liste zu Brevo übertragen. Wer sich abgemeldet hat, bleibt abgemeldet. Ein FERC-Design für den Newsletter und ein Anmeldeformular auf fercthailand.org machen. Eine Anleitung auf einer Seite schreiben. Der erste Newsletter informiert die Spender über die neuen Wege aus Schritt 1.",
                "you": "Ja sagen zum Umzug. Dann verschicken Sie jeden Newsletter selbst, mit Hilfe der Anleitung.",
                "when": "November",
                "cost": "Gratis",
            },
            {
                "h": "Website: neues Aussehen, mit der Schulkarte",
                "short": "Website erneuert, mit der Schulkarte",
                "p": "Sie können wählen, wo die neue Website läuft.",
                "ab": [
                    ("A", "Website auf WordPress, wie heute", "Bei WordPress bleiben", "Wir bauen das neue Aussehen im WordPress von FERC. Sie und Heinz bearbeiten die Seite wie bisher. Die meisten Sicherheitslücken bei WordPress liegen in Plugins (Erweiterungen): 2025 wurden 11’334 neue Lücken gefunden, 91 % davon in Plugins. Angreifer nutzen eine neue Lücke oft innerhalb von 5 Stunden. Eine WordPress-Seite braucht deshalb jede Woche Updates: siehe die Zusatzleistung «WordPress-Pflege».", "Unsere Arbeit: gratis. FERC bezahlt das Hosting wie heute."),
                    ("B", "Website auf einem einfacheren System", "Zu einer einfacheren Website wechseln, die wir betreiben", "Gleiche Adresse, fercthailand.org. Weniger Teile zum Aktualisieren, also weniger zu schützen. Sie ändern die Texte direkt auf der Seite, wie in der Übungskopie Ihrer Spendenseite. Wir übertragen die alten Seiten und Bilder.", "Unsere Arbeit: gratis. Wir betreiben sie, heute ohne Kosten."),
                ],
                "rec": "Wir empfehlen B. Wenn FERC A lieber hat, bauen wir in WordPress.",
                "list": [
                    "Ein Knopf «Patenschaft übernehmen» auf jeder Seite",
                    "Die Seite «So können Sie spenden» aus Schritt 1",
                    "Geschichten von Schülern, nur wenn sie im Einwilligungsfeld Ja angekreuzt haben",
                    "Die Schulkarte: 34 Schulen, jede mit Namen, Bezirk und Foto",
                    "Schneller auf dem Handy",
                    "Eine kurze Anleitung und eine Stunde mit Ihnen und Heinz, um alles zu zeigen",
                ],
                "map": "Die Schulkarte ansehen",
                "we": "Die neue Website bauen, A oder B.",
                "you": "A oder B wählen. Uns sagen, bei welcher Firma die Website heute gehostet ist.",
                "when": "Januar",
                "cost": "Unsere Arbeit: gratis. A: FERC bezahlt das Hosting wie heute. B: Wir betreiben sie, heute ohne Kosten.",
            },
            {
                "h": "Mehr Menschen sehen FERC",
                "short": "Beiträge, ein kurzes Video, Google Ad Grants",
                "list": [
                    "Zwei Beiträge pro Woche auf Facebook und LinkedIn im November und Dezember: der Vortrag, der Spendenanlass, Weihnachten",
                    "Ein kurzes Video aus den Fotos der Schulkarte",
                    "Google Ad Grants: Gratis-Werbung in der Google-Suche für gemeinnützige Organisationen, bis 10’000 US-Dollar pro Monat. Google verlangt eine schnelle, sichere Website; Schritt 3 gibt FERC eine. Wir prüfen, ob FERC sie bekommen kann, und stellen den Antrag.",
                    "Eine Zählung der Website-Besuche und der Klicks auf «So können Sie spenden», für den Vorstand",
                ],
                "we": "Die Beiträge schreiben und das Video machen. Ad Grants beantragen.",
                "you": "Einmal pro Monat Ja sagen zu den Beiträgen des Monats. FERC veröffentlicht sie, oder gibt uns Zugang dafür.",
                "when": "November und Dezember",
                "cost": "Gratis",
            },
            {
                "h": "Ab Januar: Patenberichte mit weniger Aufwand",
                "short": "Patenberichte mit weniger Aufwand",
                "p": "Heute: Heinz sammelt zweimal im Jahr rund 100 Schülerberichte. Sie machen daraus Berichte für die Paten. FERC führt zwei Listen: die Hauptliste und die Liste des Kassiers.",
                "list": [
                    "Eine gemeinsame Liste statt zwei, mit einer Spalte für die Einwilligung jedes Schülers",
                    "Den Bericht eines Schülers einmal eintippen; daraus entsteht der Patenbericht.",
                    "Eine Seite, die zeigt, welche Berichte da sind, fehlen oder verschickt sind",
                ],
                "p2": "Die Liste enthält Angaben über Schüler unter 18. FERC bestimmt, wer sie öffnen kann. Der Kontakt mit den Schulen läuft wie heute über das CMSEO.",
                "when": "Ab Januar, wenn der Vorstand es möchte",
                "cost": "Ein Preis, den wir im Januar mit dem Vorstand vereinbaren",
            },
        ],
        "dao": "Doi Chiang Dao in den Wolken",
        "ex_h": "Zusatzleistungen, die FERC wählen kann",
        "ex_p": "Jede Zusatzleistung ist freiwillig. Preise für FERC, in thailändischen Baht. Bis zur Hälfte kann FERC mit Gegenleistungen bezahlen.",
        "once": "einmalig",
        "month": "pro Monat",
        "stop_any": "monatlich kündbar",
        "extras": {
            "book": ("Spendenliste für den Kassier", "Jede Spende ist eine Zeile: Weg, Gebühr, Baht und Schweizer Franken. Ein Dankeschön an jeden Spender. Jeden Monat eine Übersicht für den Vorstand. Nur wenn der Kassier es möchte."),
            "posts": ("Beiträge von Januar bis Juni", "Zwei Beiträge pro Woche nach den Gratis-Monaten. Sie sagen einmal pro Monat Ja."),
            "kit": ("Paket für Vortrag und Spendenanlass", "Folien in grosser Schrift für Ihren Vortrag am 28. November. Karten «So können Sie spenden» mit QR-Code für jeden Tisch am 29. November. Eine Dankes-E-Mail an die Gäste am 30. November."),
            "ads": ("Betreuung von Ad Grants", "Wenn Google Ja sagt: Wir halten die Gratis-Werbung nach den Regeln von Google am Laufen und schicken dem Vorstand jeden Monat eine Zeile."),
            "alumni": ("Umfrage für Ehemalige", "Fragen an ehemalige FERC-Schüler als kurzes Formular auf Thai und Englisch, im eigenen Google-Konto von FERC."),
            "usf": ("Unterlagen für US-Stiftungen", "Die englischen Unterlagen, die eine US-Stiftung verlangt, bevor sie einer Organisation im Ausland spendet. Nur wenn eine US-Stiftung unter den Spendern von FERC ist."),
            "thai": ("Website auf Thai", "Thai-Seiten neben den englischen, geprüft von einer Person mit Thai als Muttersprache."),
            "wpcare": ("WordPress-Pflege", "Für Wahl A: Jede Woche aktualisieren wir WordPress und die Plugins, prüfen auf neue Sicherheitslücken und machen eine Sicherungskopie."),
        },
        "tr_h": "Mit Gegenleistungen bezahlen",
        "tr_p": "FERC kann bis zur Hälfte jeder Zusatzleistung mit einer Gegenleistung statt mit Geld bezahlen. Zum Beispiel:",
        "trades": {
            "credit": "Eine Zeile unten auf fercthailand.org, «Website und Spendenseite: Hongdam», ein Dank im Newsletter, und die Erlaubnis, die Seiten von FERC als unsere Arbeit zu zeigen.",
            "thanks": "Unser Name auf der Dankesfolie und eine Tischkarte am Spendenanlass vom 29. November.",
            "jobs": "Unsere Stellenangebote an ehemalige FERC-Schüler, die Ja zu Stellen-News gesagt haben. Nur Erwachsene. FERC verschickt sie, nicht wir.",
        },
        "tr_note": "Empfehlungen sind etwas anderes. Sie bringen FERC Geld (nächster Abschnitt).",
        "co_h": "Für ganz Chiang Mai",
        "co": [
            "Viele gemeinnützige Organisationen und Vereine in Chiang Mai haben Spender im Ausland, wie FERC.",
            "Andere Gruppen können eine Spendenseite wie die von FERC bekommen. Die Spenden gehen auf das eigene Bankkonto der Gruppe, mit einer Übersicht über jede Spende. Preis für andere Gruppen: 30’000 Baht für die Einrichtung, dann 10’000 Baht pro Monat, monatlich kündbar. Für FERC ist die Spendenseite Teil von Schritt 1 und gratis.",
            "Wenn Sie uns jemanden vorstellen, der uns dann für diese oder eine andere Arbeit einen Auftrag gibt, spenden wir FERC 20 % von dem, was er uns im ersten Jahr bezahlt, sobald seine Zahlungen eintreffen.",
        ],
        "intro_btn": "Jemanden vorstellen",
        "intro_subject": "Eine Empfehlung: Hongdam",
        "intro_body": "Liebe/r …\n\nIch möchte Ihnen NaN von Hongdam vorstellen (in Kopie). Hongdam hat die Spendenseite und die Schulkarte von FERC gemacht. Ich glaube, Hongdam könnte Ihnen helfen bei …\n\nWenn Sie mit Hongdam zusammenarbeiten, erhält FERC 20 % von dem, was Sie Hongdam im ersten Jahr bezahlen, für unsere Schüler.\n\nHerzliche Grüsse\nEveline",
        "ch_h": "Auswählen und senden",
        "nav_h": "Auf dieser Seite",
        "nav_extras": "Zusatzleistungen",
        "nav_trade": "Mit Gegenleistungen bezahlen",
        "nav_co": "Für ganz Chiang Mai",
        "nav_choose": "Auswählen und senden",
        "float": "Auswählen",
        "step_of": "Schritt {n} von 5",
        "more": "Mehr zu Schritt {n}",
        "pv_h": "Ihre E-Mail lautet:",
        "pv_to": "An",
        "pv_subject": "Betreff",
        "board_screen": "Drucken Sie diese Seite, um mit dem Stift anzukreuzen, oder wählen Sie auf der Website.",
        "board_web": "Auf der Website auswählen",
        "board_or": "Eines wählen:",
        "ch_p": "Kreuzen Sie an, was FERC möchte. Noch ist nichts angekreuzt. Der Vorstand entscheidet am 31. Oktober; Sie können jetzt eine erste Wahl schicken und sie später ändern.",
        "ch_plan": "Der Plan: Schritte 1, 2 und 4 (gratis)",
        "ch_step5": "5 📋 Patenberichte: im Januar besprechen",
        "ch_web": "3 🖥️ Website: eines wählen (gratis)",
        "ch_web_talk": "Zuerst sprechen",
        "ch_wp_only": "🔒 Nur mit 3A, WordPress",
        "board_one": "Eines wählen: 3A oder 3B",
        "ch_extras": "Zusatzleistungen",
        "ch_pay": "Wie FERC die Zusatzleistungen bezahlt",
        "pay": ["Geld", "Halb Geld, halb Gegenleistung", "Zuerst sprechen"],
        "ch_trade": "Gegenleistungen, die FERC anbieten könnte",
        "ch_groups": "Gruppen, die die gleiche Spendenseite möchten (Namen, freiwillig)",
        "ch_name": "Ihr Name",
        "ch_total": "Summe der Zusatzleistungen",
        "ch_none": "keine",
        "ch_and": "und",
        "ch_money": "Davon in Geld",
        "ch_send": "Per E-Mail an NaN schicken",
        "ch_copy": "Kopieren",
        "ch_help": "Der Knopf öffnet Ihr E-Mail-Programm mit diesem Text. Drücken Sie dort auf Senden. Kein E-Mail-Programm? Drücken Sie Kopieren und fügen Sie den Text in eine E-Mail an nan@motdang.net ein.",
        "ch_copied": "Kopiert. Fügen Sie es in eine E-Mail an nan@motdang.net ein.",
        "ch_subject": "FERC: unsere Wahl",
        "ch_msg_h": "Die Wahl von FERC",
        "priv_h": "Schutz der Schüler",
        "priv": [
            "Auf der Website: nur das, wozu ein Schüler im Einwilligungsfeld Ja angekreuzt hat.",
            "E-Mail, LINE und Telefonnummern der Schüler stehen nicht auf der Website.",
            "Kontakt mit Schulen und Schülern läuft über das CMSEO, wie heute.",
        ],
        "q_h": "Fragen an Sie",
        "q_p": "Tippen Sie auf eine Antwort. Ihre Antworten gehen in die gleiche E-Mail wie Ihre Wahl.",
        "q_note": "Notiz (freiwillig)",
        "q_answers": "Antworten",
        "qa": [
            ("map", "Wie hat Ihnen die Schulkarte gefallen?", "one", ["✓ Gut so", "✎ Gut, mit Änderungen", "? Noch nicht gesehen"], True),
            ("myriad", "Ausstieg bei Myriad: Was ist am schwierigsten?", "many", ["Das Rechtliche", "Die Bank", "Die Information an die Spender"], True),
            ("treasurer", "Dürfen wir den Kassier zu e-Donation fragen?", "one", ["✓ Ja, fragen Sie den Kassier", "Ich frage selbst", "✗ Jetzt nicht"], False),
            ("cards", "Möchte FERC Kartenzahlungen auf der Website?", "one", ["✓ Ja", "✗ Nein", "? Weiss nicht"], False),
            ("host", "Bei welcher Firma ist die Website heute gehostet?", "one", ["? Weiss nicht"], True),
            ("tools", "Nutzt FERC diese Gratis-Werkzeuge für gemeinnützige Organisationen?", "many", ["Google for Nonprofits", "Canva for Nonprofits", "✗ Keines", "? Weiss nicht"], False),
            ("budget", "Gibt es Geld für bezahlte Programme?", "one", ["Nur gratis", "Etwas Geld", "Der Vorstand entscheidet"], False),
        ],
        "src_h": "Quellen",
        "photos": "Fotos von Takeaway, einem Nutzer von Wikimedia Commons",
        "board_title": "FERC · Plan für den Vorstand, 31. Oktober 2026",
        "board_lede": "Fünf Schritte von Hongdam. Der Vorstand entscheidet. Eveline sagt Ja zu jedem Teil. Wir machen die Arbeit.",
        "board_ask": "Für den Vorstand: Ja oder Nein zu den Schritten 1 bis 4 (gratis) und zu jeder Zusatzleistung. Schritt 5 legen wir im Januar mit einem Preis vor.",
        "board_cols": ("Ja", "Nein", "Schritt", "Wann", "Kosten für FERC"),
        "board_tick": "Ankreuzen, Name und Datum dazuschreiben, dann ein Foto jeder Seite an nan@motdang.net schicken.",
        "board_groups": "Gruppen, die eine Spendenseite wie die von FERC möchten (andere Gruppen zahlen 30’000 Baht für die Einrichtung, dann 10’000 Baht pro Monat):",
        "print": "Drucken",
        "board_sign": "Name: ____________________   Datum: ____________",
        "back": "Zurück zum Plan",
    },
}

# One name and one icon per step, used everywhere (plan, contents, chooser, board, email).
# "core": the lines shown; the step's p/table/list/p2 fold under "More about step N".
STEPMETA = {
    "en": [
        {"icon": "🌍", "short": "Ways to give", "core": [
            "A “How to give” page on fercthailand.org, one box per country.",
            "Help with leaving Myriad.",
            "From the USA, with a tax receipt: CAF America.",
            "Thai tax receipts: e-Donation. We check with the treasurer.",
        ], "p2": "The sample giving page on hongdam.net shows the idea. The “How to give” page goes on fercthailand.org."},
        {"icon": "✉️", "short": "Newsletter", "core": [
            "Move the list from MailPoet (free up to 500) to Brevo (free for more).",
            "Brevo sends 300 emails a day, so 500 people take two days.",
            "The first newsletter tells donors the new ways to give.",
        ]},
        {"icon": "🖥️", "short": "Website", "p": None, "core": [
            "New look, a “Sponsor a student” button, the school map.",
            "Choose A or B:",
        ], "ab": [
            ("A", "WordPress, as now", "WordPress, as now", "We build inside your WordPress. You edit as now. It needs updates every week (extra: WordPress care).", "Our work: free. FERC pays for hosting, as now."),
            ("B", "Simpler website, we host it", "★ Simpler website, we host it", "Same address. Fewer parts to keep safe. You change the words on the page itself.", "Our work: free. We host it at no charge today."),
        ], "rec": "★ We recommend B. If FERC prefers A, we build in WordPress.",  # stylecheck: allow — NaN asked for this recommendation (23 Oct)
        "p2": "Why weekly updates on WordPress: in 2025, 11,334 new security holes were found in WordPress, 91% of them in plugins (add-ons). Attackers often use a new hole within 5 hours. With B, we move the old pages and pictures across, and you change words as on the practice copy of your giving page."},
        {"icon": "📣", "short": "More people see FERC", "core": [
            "Two posts a week in November and December.",
            "A short video from the school map.",
            "Free Google ads for charities (Ad Grants), if Google says yes.",
        ]},
        {"icon": "📋", "short": "Sponsor reports", "core": [
            "From January: one shared list instead of two.",
            "Type a report once; the sponsor’s report is made from it.",
        ]},
    ],
    "de": [
        {"icon": "🌍", "short": "Wege zu spenden", "core": [
            "Eine Seite «So können Sie spenden» auf fercthailand.org, ein Abschnitt pro Land.",
            "Hilfe beim Ausstieg bei Myriad.",
            "Aus den USA, mit Spendenbestätigung: CAF America.",
            "Thailändische Spendenbestätigungen: e-Donation. Wir klären das mit dem Kassier.",
        ], "p2": "Die Muster-Spendenseite auf hongdam.net zeigt die Idee. Die Seite «So können Sie spenden» kommt auf fercthailand.org."},
        {"icon": "✉️", "short": "Newsletter", "core": [
            "Die Liste von MailPoet (gratis bis 500) zu Brevo (gratis für mehr) übertragen.",
            "Brevo verschickt 300 E-Mails pro Tag; 500 Personen dauern also zwei Tage.",
            "Der erste Newsletter informiert die Spender über die neuen Wege.",
        ]},
        {"icon": "🖥️", "short": "Website", "p": None, "core": [
            "Neues Aussehen, ein Knopf «Patenschaft übernehmen», die Schulkarte.",
            "A oder B wählen:",
        ], "ab": [
            ("A", "WordPress, wie heute", "WordPress, wie heute", "Wir bauen in Ihrem WordPress. Sie bearbeiten wie bisher. Es braucht jede Woche Updates (Zusatzleistung: WordPress-Pflege).", "Unsere Arbeit: gratis. FERC bezahlt das Hosting wie heute."),
            ("B", "Einfachere Website, von uns betrieben", "★ Einfachere Website, von uns betrieben", "Gleiche Adresse. Weniger Teile zu schützen. Sie ändern die Texte direkt auf der Seite.", "Unsere Arbeit: gratis. Wir betreiben sie, heute ohne Kosten."),
        ], "rec": "★ Wir empfehlen B. Wenn FERC A lieber hat, bauen wir in WordPress.",
        "p2": "Warum jede Woche Updates bei WordPress: 2025 wurden 11’334 neue Sicherheitslücken in WordPress gefunden, 91 % davon in Plugins (Erweiterungen). Angreifer nutzen eine neue Lücke oft innerhalb von 5 Stunden. Bei B übertragen wir die alten Seiten und Bilder, und Sie ändern Texte wie in der Übungskopie Ihrer Spendenseite."},
        {"icon": "📣", "short": "Mehr Menschen sehen FERC", "core": [
            "Zwei Beiträge pro Woche im November und Dezember.",
            "Ein kurzes Video aus der Schulkarte.",
            "Gratis-Werbung bei Google für gemeinnützige Organisationen (Ad Grants), wenn Google Ja sagt.",
        ]},
        {"icon": "📋", "short": "Patenberichte", "core": [
            "Ab Januar: eine gemeinsame Liste statt zwei.",
            "Einen Bericht einmal eintippen; daraus entsteht der Patenbericht.",
        ]},
    ],
}
for _lang, _metas in STEPMETA.items():
    for _step, _meta in zip(WORDS[_lang]["steps"], _metas):
        _step.update(_meta)

SOURCES = [
    ("CAF America: Friends Funds", "https://cafamerica.org/friends-funds/"),
    ("DFAT: Overseas Aid Gift Deduction Scheme", "https://www.dfat.gov.au/development/who-we-work-with/ngos/oagds"),
    ("Global Development Group (Australia)", "https://globaldevelopmentgroup.org/au/help/"),
    ("THE STANDARD: donations to foundations through e-Donation from 1 January 2026", "https://thestandard.co/donation-tax-deduction-e-donation-2026/"),
    ("Revenue Department: e-Donation", "https://www.rd.go.th/region/04/saraburi/85/6565.html"),
    ("Brevo pricing", "https://www.brevo.com/pricing/"),
    ("MailerLite: free plan update (250 subscribers from 16 June 2026)", "https://www.mailerlite.com/help/free-plan-update-faq"),
    ("Patchstack: State of WordPress Security in 2026", "https://patchstack.com/whitepaper/state-of-wordpress-security-in-2026/"),
    ("Google for Nonprofits: Ad Grants", "https://www.google.com/grants/"),
    ("Myriad USA (formerly King Baudouin Foundation United States)", "https://myriadusa.org/"),
]

PHOTOS = [
    ("road", "https://commons.wikimedia.org/wiki/File:Chiang_mai_province_road_1263.jpg", "CC BY 3.0", "https://creativecommons.org/licenses/by/3.0"),
    ("dao", "https://commons.wikimedia.org/wiki/File:Doi_Chiang_Dao_in_the_clouds.jpg", "CC BY-SA 3.0", "https://creativecommons.org/licenses/by-sa/3.0"),
]

e = html.escape


def baht(n, w=None):
    if w and w["lang"].startswith("de"):
        return f"{n:,}".replace(",", "’") + " Baht"
    return "฿" + f"{n:,}"


def price(w, once, month):
    if once:
        return f"{baht(once, w)} {w['once']}"
    return f"{baht(month, w)} {w['month']}, {w['stop_any']}"


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
  <button class="btn" type="button" id="aa" aria-pressed="false"><span aria-hidden="true">A<span class="a2">A</span></span> {e(w['aa'])}</button>
  <button class="btn" type="button" id="theme"><span aria-hidden="true">◐</span> {e(w['theme'])}</button>
</div>
"""


def readbtn(w):
    return f'<button class="read" type="button"><span aria-hidden="true">🔊</span> {e(w["read"])}</button>'


def sec(id_, title, body, w, cls="sec"):
    return f"""<section class="{cls}" id="{id_}" aria-labelledby="{id_}-h"><div class="wrap">
  <div class="hrow"><h2 id="{id_}-h">{title}</h2>{readbtn(w)}</div>
  {body}
</div></section>
"""


def ul(items, cls="told"):
    return f'<ul class="{cls}">' + "".join(f"<li>{e(x)}</li>" for x in items) + "</ul>"


def ico(x):
    return f'<span aria-hidden="true">{x}</span>'


def step_name(n, s):
    return f'{n} {ico(s["icon"])} {e(s["short"])}'


def step_html(w, i, s):
    out = [f'<li class="step" id="step{i}"><section aria-labelledby="step{i}-h">']
    out.append(f'<div class="hrow"><p class="of">{e(w["step_of"].format(n=i))}</p>{readbtn(w)}</div>')
    out.append(f'<h3 id="step{i}-h">{step_name(i, s)}</h3>')
    out.append(ul(s["core"], "core"))
    if "ab" in s:
        out.append('<div class="ab">' + "".join(
            f'<div class="opt{" rec" if code == "B" else ""}"><p class="tag">{i}{code}</p><h4>{e(title)}</h4><p>{e(text)}</p><p class="small-ink">{e(cost)}</p></div>'
            for code, _, title, text, cost in s["ab"]) + "</div>")
        out.append(f'<p class="ask">{e(s["rec"])}</p>')
    dl = []
    for k in ("we", "you", "when", "cost"):
        if k in s and not (k == "cost" and "ab" in s):
            dl.append(f"<div><dt>{e(w[k])}</dt><dd>{e(s[k])}</dd></div>")
    out.append(f'<dl class="facts">{"".join(dl)}</dl>')
    more = []
    if s.get("p"):
        more.append(f"<p>{e(s['p'])}</p>")
    if "table" in s:
        rows = "".join(f'<tr><th scope="row">{e(a)}</th><td>{e(b)}</td></tr>' for a, b in s["table"])
        more.append(f'<table class="routes"><tbody>{rows}</tbody></table>')
    if "list" in s:
        more.append(ul(s["list"], ""))
    if "map" in s:
        more.append(f'<p><a class="btn" href="{MAP}">{e(s["map"])} →</a></p>')
    if s.get("p2"):
        more.append(f"<p>{e(s['p2'])}</p>")
    if more:
        out.append(f'<details><summary>{e(w["more"].format(n=i))}</summary>{"".join(more)}</details>')
    out.append("</section></li>")
    return "".join(out)


def foot(w, rel):
    src = "".join(f'<li><a href="{u}">{e(t)}</a></li>' for t, u in SOURCES)
    ph = " · ".join(
        f'{e(w[k])}: <a href="{u}">Wikimedia Commons</a>, <a href="{lu}">{e(l)}</a>'
        for k, u, l, lu in PHOTOS
    )
    return f"""<footer class="wrap foot">
  <h2>{e(w['src_h'])}</h2>
  <ul>{src}</ul>
  <p class="small">{e(w['photos'])}. {ph}</p>
</footer>
<script src="{rel}app.js"></script>
</body>
</html>
"""


def mailto(to, subject, body, cc=""):
    from urllib.parse import quote
    q = f"subject={quote(subject)}&body={quote(body)}"
    if cc:
        q = f"cc={quote(cc)}&" + q
    return f"mailto:{to}?{q}"


def plan_items(w):
    """(number, label, step) for the chooser and board; step 3 splits into 3A and 3B."""
    out = []
    for i, s in enumerate(w["steps"][:4]):
        if "ab" in s:
            for code, short, _, _, cost in s["ab"]:
                out.append((f"{i+1}{code}", short, s | {"cost": cost}))
        else:
            out.append((str(i + 1), s["short"], s))
    return out


def questions(w):
    out = []
    for key, q, kind, opts, note in w["qa"]:
        typ = "radio" if kind == "one" else "checkbox"
        items = "".join(
            f'<label class="pick chip"><input type="{typ}" name="q-{key}" value="{e(o)}"> <span>{e(o)}</span></label>'
            for o in opts)
        n = (f'<label class="field small-field">{e(w["q_note"])}<input type="text" name="qn-{key}"></label>' if note else "")
        out.append(f'<fieldset class="q" data-q="{key}" data-text="{e(q)}"><legend>{e(q)}</legend><div class="chips">{items}</div>{n}</fieldset>')
    return "".join(out)


def chooser(w):
    st = w["steps"]
    steps = "".join(
        f'<label class="pick"><input type="checkbox" name="step" value="{n}" data-label="{e(n + " " + s["icon"] + " " + s["short"])}"> <span>{step_name(n, s)}</span></label>'
        for n, short, s in plan_items(w) if not n.startswith("3")
    )
    web = "".join(
        f'<label class="pick card{" rec" if code == "B" else ""}"><input type="radio" name="web" value="3{code}" data-label="{e("3" + code + " " + short)}"> <span><b>3{code}</b> {e(title)}<i class="needs">{e(cost)}</i></span></label>'
        for code, short, title, _, cost in st[2]["ab"]
    ) + f'<label class="pick"><input type="radio" name="web" value="talk" data-label="3 {e(w["ch_web_talk"])}"> <span>{e(w["ch_web_talk"])}</span></label>'
    s5 = f'<label class="pick"><input type="checkbox" name="step" value="5" data-label="{e(w["ch_step5"])}"> <span>{e(w["ch_step5"])}</span></label>'

    def extra_pick(k, o, m):
        needs = ' data-needs="3A"' if k == "wpcare" else ""
        note = f'<i class="needs lock">{e(w["ch_wp_only"])}</i>' if k == "wpcare" else ""
        name = w["extras"][k][0]
        label = e(name + " (" + price(w, o, m) + ")")
        return (f'<label class="pick"><input type="checkbox" name="extra" value="{k}" data-once="{o}" data-month="{m}"{needs} data-label="{label}">'
                f' <span>{e(name)} <b class="pr">{e(price(w, o, m))}</b>{note}</span></label>')
    extras = "".join(extra_pick(k, o, m) for k, o, m in EXTRAS)
    pay = "".join(
        f'<label class="pick"><input type="radio" name="pay" value="{e(p)}"> <span>{e(p)}</span></label>'
        for p in w["pay"]
    )
    trades = "".join(
        f'<label class="pick"><input type="checkbox" name="trade" value="{k}" data-label="{e(t)}"> <span>{e(t)}</span></label>'
        for k, t in w["trades"].items()
    )
    cfg = json.dumps({
        "to": MAIL, "subject": w["ch_subject"], "head": w["ch_msg_h"],
        "plan": w["ch_plan"], "extras": w["ch_extras"], "pay": w["ch_pay"], "trade": w["ch_trade"],
        "groups": w["ch_groups"], "name": w["ch_name"], "total": w["ch_total"], "none": w["ch_none"],
        "once": w["once"], "month": w["month"], "copied": w["ch_copied"],
        "and": w["ch_and"], "money": w["ch_money"], "de": w["lang"].startswith("de"),
        "half": w["pay"][1], "web": w["ch_web"], "answers": w["q_answers"],
    }, ensure_ascii=False)
    return f"""<p>{e(w['ch_p'])}</p>
<form id="chooser" action="#choose" onsubmit="return false" data-cfg="{e(cfg)}">
  <fieldset><legend>{e(w['ch_plan'])}</legend>{steps}</fieldset>
  <fieldset><legend>{e(w['ch_web'])}</legend>{web}</fieldset>
  <fieldset><legend>{e(w['ch_step5'].split(':')[0])}</legend>{s5}</fieldset>
  <fieldset><legend>➕ {e(w['ch_extras'])}</legend>{extras}</fieldset>
  <fieldset><legend>{e(w['ch_pay'])}</legend>{pay}</fieldset>
  <fieldset><legend>🤝 {e(w['ch_trade'])}</legend>{trades}</fieldset>
  <h3 class="qh">❓ {e(w['q_h'])}</h3>
  <p>{e(w['q_p'])}</p>
  {questions(w)}
  <label class="field">🏘️ {e(w['ch_groups'])}<textarea name="groups" rows="2"></textarea></label>
  <label class="field">{e(w['ch_name'])}<input type="text" name="name" autocomplete="name"></label>
  <p class="total" id="total" aria-live="polite">{e(w['ch_total'])}: {e(w['ch_none'])}</p>
  <div class="preview"><p class="pv-h">{e(w['pv_h'])}</p><p class="pv-to">{e(w['pv_to'])}: {MAIL}<br>{e(w['pv_subject'])}: {e(w['ch_subject'])}</p><pre id="pv"></pre></div>
  <p class="help">{e(w['ch_help'])}</p>
  <p class="sendrow"><a class="cta send" id="send" href="mailto:{MAIL}">✉️ {e(w['ch_send'])}</a> <button class="btn send" type="button" id="copy">📋 {e(w['ch_copy'])}</button></p>
  <p class="small-ink" id="copied" aria-live="polite"></p>
</form>
"""


def page(w, rel, path):
    told = ul(w["told"])
    st = w["steps"]
    steps = "".join(step_html(w, i + 1, s) for i, s in enumerate(st))
    time = '<ol class="time">' + "".join(f'<li><span class="d">{e(a)}</span> <span>{e(b)}</span></li>' for a, b in w["time"]) + "</ol>"
    lede = "".join(f'<p class="lede">{e(x)}</p>' for x in w["lede"])
    who = "".join(f"<p>{e(x)}</p>" for x in w["who"]) + f'<p class="row"><a class="btn" href="{DESK}">{e(w["desk_btn"])} →</a> <a class="btn" href="mailto:{MAIL}?subject=FERC">{e(w["write"])}: {MAIL}</a></p>'
    extras = '<ul class="extras">' + "".join(
        f'<li><h3>{e(w["extras"][k][0])}</h3><p class="pr">{e(price(w, o, m))}</p><p>{e(w["extras"][k][1])}</p></li>'
        for k, o, m in EXTRAS
    ) + "</ul>"
    trade = f"<p>{e(w['tr_p'])}</p>" + ul(w["trades"].values()) + f"<p>{e(w['tr_note'])}</p>"
    intro = mailto("", w["intro_subject"], w["intro_body"], cc=MAIL)
    comm = "".join(f"<p>{e(x)}</p>" for x in w["co"]) + f'<p class="row"><a class="btn" href="{e(intro)}">✉️ {e(w["intro_btn"])}</a> <a class="btn" href="{DESK}">{e(w["desk_btn"])}</a></p>'
    nav = [(f"#step{i+1}", step_name(i + 1, s)) for i, s in enumerate(st)] + [
        ("#extras", f'{ico("➕")} {e(w["nav_extras"])}'),
        ("#trade", f'{ico("🤝")} {e(w["nav_trade"])}'),
        ("#community", f'{ico("🏘️")} {e(w["nav_co"])}'),
        ("#choose", f'{ico("✅")} {e(w["nav_choose"])}'),
    ]
    navhtml = f'<nav class="toc" aria-labelledby="toc-h"><div class="wrap"><h2 id="toc-h">{e(w["nav_h"])}</h2><ul>' + "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in nav) + "</ul></div></nav>"
    return head(w, rel, w["title"], path) + f"""
<header class="band hero" style="background-image:url({rel}img/road.jpg)">
  <p class="kick">{e(w['kick'])}</p>
  <section class="in" aria-labelledby="h1">
    <div class="hrow"><h1 id="h1">{e(w['h1'])}</h1></div>
    <p class="row"><a class="cta light" href="#choose">✅ {e(w['go_choose'])}</a> <a class="cta ghost" href="board/">🖨️ {e(w['board_btn'])}</a></p>
    {lede}
    <p class="row">{readbtn(w)}</p>
  </section>
  <p class="cred">{e(w['road'])}</p>
</header>
<main>
{navhtml}
{sec("who", e(w["who_h"]), who, w)}
{sec("told", e(w["told_h"]), told, w, "sec alt")}
{sec("when", e(w["time_h"]), time, w)}
<section class="sec" id="plan" aria-labelledby="plan-h"><div class="wrap">
  <h2 id="plan-h">{e(w['plan_h'])}</h2>
  <ol class="steps">{steps}</ol>
</div></section>
<div class="band short" style="background-image:url({rel}img/dao.jpg);background-position:center 40%" role="img" aria-label="{e(w['dao'])}"><p class="cred">{e(w['dao'])}</p></div>
{sec("extras", ico("➕") + " " + e(w["ex_h"]), f"<p>{e(w['ex_p'])}</p>" + extras, w)}
{sec("trade", ico("🤝") + " " + e(w["tr_h"]), trade, w, "sec alt")}
{sec("community", ico("🏘️") + " " + e(w["co_h"]), comm, w)}
{sec("choose", ico("✅") + " " + e(w["ch_h"]), chooser(w), w, "sec alt choose")}
{sec("privacy", e(w["priv_h"]), ul(w["priv"]), w)}
</main>
<a class="float" id="float" href="#choose">✅ {e(w['float'])}</a>
""" + foot(w, rel)


def board(w, rel, path):
    c0, c1, c2c, c2, c3 = w["board_cols"]
    st = w["steps"]

    def row(n, s, label=None):
        return (f'<tr><td class="box" data-l="{e(c0)}">☐</td><td class="box" data-l="{e(c1)}">☐</td>'
                f'<th scope="row">{label or step_name(n, s)}</th><td data-l="{e(c2)}">{e(s["when"])}</td><td data-l="{e(c3)}">{e(s["cost"])}</td></tr>')
    rows = row(1, st[0]) + row(2, st[1])
    opts = " &nbsp; ".join(f'☐ 3{code} {e(short)}' for code, short, _, _, _ in st[2]["ab"]) + f' &nbsp; ☐ {e(w["ch_web_talk"])}'
    costs = " ".join(f"3{code}: {e(cost)}" for code, _, _, _, cost in st[2]["ab"])
    rows += (f'<tr><td colspan="2" class="box"></td><th scope="row">{step_name(3, st[2])}<br><span class="opts">{e(w["board_or"])} {opts}</span></th>'
             f'<td data-l="{e(c2)}">{e(st[2]["when"])}</td><td data-l="{e(c3)}">{costs}</td></tr>')
    rows += row(4, st[3])
    rows += (f'<tr><td colspan="2" class="box"></td><th scope="row">{step_name(5, st[4])}</th>'
             f'<td data-l="{e(c2)}">{e(st[4]["when"])}</td><td data-l="{e(c3)}">{e(st[4]["cost"])}</td></tr>')
    ex = "".join(
        f'<tr><td class="box" data-l="{e(c0)}">☐</td><td class="box" data-l="{e(c1)}">☐</td><th scope="row">{e(w["extras"][k][0])}'
        + (f'<br><span class="opts">{e(w["ch_wp_only"])}</span>' if k == "wpcare" else "")
        + f'</th><td colspan="2" data-l="{e(c3)}">{e(price(w, o, m))}</td></tr>'
        for k, o, m in EXTRAS
    )
    pay = " &nbsp; ".join(f"☐ {e(p)}" for p in w["pay"])
    priv = ul(w["priv"], "")
    return head(w, rel, w["board_title"], path) + f"""
<main class="wrap boardpage" id="plan">
  <p class="noprint row"><a class="btn" href="../">← {e(w['back'])}</a> <button class="btn" type="button" onclick="window.print()">🖨️ {e(w['print'])}</button> <a class="btn" href="../#choose">✅ {e(w['board_web'])}</a></p>
  <p class="noprint help">{e(w['board_screen'])}</p>
  <h1>{e(w['board_title'])}</h1>
  <p class="lede">{e(w['board_lede'])}</p>
  <p class="ask">{e(w['board_ask'])}</p>
  <p class="ask">{e(w['board_tick'])}</p>
  <table class="board"><thead><tr><th scope="col" class="box">{e(c0)}</th><th scope="col" class="box">{e(c1)}</th><th scope="col">{e(c2c)}</th><th scope="col">{e(c2)}</th><th scope="col">{e(c3)}</th></tr></thead><tbody>{rows}</tbody></table>
  <h2>{ico("➕")} {e(w['ex_h'])}</h2>
  <p>{e(w['ex_p'])}</p>
  <table class="board"><thead><tr><th scope="col" class="box">{e(c0)}</th><th scope="col" class="box">{e(c1)}</th><th scope="col">{e(w['ch_extras'])}</th><th scope="col" colspan="2">{e(c3)}</th></tr></thead><tbody>{ex}</tbody></table>
  <p><b>{e(w['ch_pay'])}:</b> {pay}</p>
  <p><b>{ico("🤝")} {e(w['tr_h'])}:</b></p>
  {ul(w["trades"].values(), "")}
  <h2>{ico("🏘️")} {e(w['co_h'])}</h2>
  <p>{e(w['co'][2])}</p>
  <p>{e(w['board_groups'])} ________________________________</p>
  <p>{e(w['board_sign'])}</p>
  <h2>{e(w['priv_h'])}</h2>
  {priv}
  <p class="small">{e(w['who'][0])} {MAIL} · {URL}</p>
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
