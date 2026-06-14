#!/usr/bin/env python3
"""Generate localized NoteWhen privacy policy HTML pages."""

from __future__ import annotations

from pathlib import Path

OUTPUT_DIR = Path(__file__).parent

CONTACT_URL = "https://github.com/lemist/app-legal/issues"
EULA_URL = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"
EFFECTIVE_DATE = "June 9, 2026"

LOCALES: dict[str, dict[str, str]] = {
    "en": {
        "lang": "en",
        "dir": "ltr",
        "title": "NoteWhen Privacy Policy",
        "meta_description": "Privacy Policy for NoteWhen, a personal health event tracking app for iOS.",
        "effective_date": "Effective date: June 9, 2026",
        "summary_label": "Summary:",
        "summary": "NoteWhen is a personal health event tracker. Your tracking data is stored on your devices and in your private iCloud account. With your permission, the app can read and write selected exercise, sleep, and water data with Apple Health. If you use AI monthly reports, an aggregated summary of your data is sent to our report-generation services to produce the report. We do not sell your data or use third-party analytics.",
        "intro": 'This Privacy Policy describes how NoteWhen ("we", "us", or "the app") handles information when you use the NoteWhen iOS app and related widget. By using the app, you agree to this policy.',
        "s1_title": "1. Who we are",
        "s1_p1": 'NoteWhen is an iOS app. For privacy questions, contact us via <a href="{contact}">GitHub Issues</a>.',
        "s2_title": "2. Information you provide and we store",
        "s2_intro": "Depending on how you use the app, we process the following categories of data:",
        "s2_li1": "<strong>Health and wellness events</strong> you choose to track, such as symptoms, medications, blood pressure, bowel movements, menstrual periods, mood, anxiety questionnaires (PHQ-9 and GAD-7), sleep, exercise, water intake, meals, and notes you attach to each occurrence.",
        "s2_li2": "<strong>Event configuration</strong>, including event names, icons, categories, reminder schedules, and medication reminder times.",
        "s2_li3": "<strong>AI monthly reports</strong>, including generated report text and suggestions, if you use that feature.",
        "s2_li4": "<strong>App preferences</strong>, such as language, appearance, and reminder settings.",
        "s2_p1": "This data is stored locally on your device and, when you are signed in to iCloud, synced through your private iCloud account across your devices. We do not operate a separate account system or backend database for your tracking data.",
        "s3_title": "3. Apple Health (HealthKit)",
        "s3_p1": 'If you enable Health integration, NoteWhen may <strong>read</strong> workout, sleep, and water intake data from Apple Health to import into your event history. With your permission, the app may also <strong>write</strong> exercise, sleep, and water entries that you log in NoteWhen to Apple Health so your records stay in sync across apps.',
        "s3_li1": "<strong>Read access:</strong> imports workouts, sleep sessions, and water samples from Apple Health into NoteWhen.",
        "s3_li2": "<strong>Write access:</strong> saves workouts, sleep sessions, and water intake that you record in NoteWhen to Apple Health. Entries imported from Apple Health are not written back.",
        "s3_li3": "HealthKit data is processed on your device. Data you import or log is stored in your app database and iCloud as described above.",
        "s3_li4": "We do not use HealthKit data for advertising, and we do not sell HealthKit data.",
        "s3_li5": "You can grant, limit, or revoke read and write access for each data type at any time in the Health app or iOS Settings.",
        "s4_title": "4. AI monthly reports",
        "s4_p1": "When you generate a monthly report, the app builds a text summary from your tracked events for the selected month and sends it over HTTPS to our report-generation services. Those services use third-party AI technology to produce the report. The request includes your selected app language and generation instructions; it does not include your Apple ID or iCloud credentials.",
        "s4_li1": "Report generation is designed to process requests transiently and not persist your tracking summary after the report is returned.",
        "s4_li2": "Generated reports are saved in your app data and synced via your iCloud account.",
        "s4_li3": "AI output is for personal reference only and is not medical advice.",
        "s4_p2": "You can avoid sending data for report generation by not generating monthly reports or by not subscribing to / using that feature.",
        "s5_title": "5. Widget data",
        "s5_p1": "The NoteWhen widget displays quick-record shortcuts using a limited copy of event metadata (such as event name, icon, and sort order) shared between the app and the widget. Occurrence history is not stored for the widget.",
        "s6_title": "6. Notifications",
        "s6_p1": "NoteWhen schedules <strong>local</strong> notifications on your device for event logging reminders, medication reminders, and optional monthly report availability. Notification content may include event or medication names you configured. We do not send push notifications from our own servers with your health data.",
        "s7_title": "7. Subscriptions and payments",
        "s7_p1": "Optional subscriptions for AI monthly reports are processed entirely by Apple through your Apple ID. We receive subscription status from Apple’s StoreKit to unlock features. We do not receive or store your payment card details.",
        "s8_title": "8. What we do not collect",
        "s8_li1": "We do not sell your personal or health data.",
        "s8_li2": "We do not use third-party advertising or analytics SDKs in the app.",
        "s8_li3": "We do not require you to create a separate NoteWhen account.",
        "s9_title": "9. Data retention and deletion",
        "s9_li1": "Your tracking data remains until you delete it in the app, delete the app, or remove data from iCloud.",
        "s9_li2": "Events you delete are kept in an inactive state for 30 days before permanent deletion, as described in the app.",
        "s9_li3": "Deleting the app from a device removes local data on that device; iCloud copies may remain until you manage iCloud storage in iOS Settings.",
        "s10_title": "10. Children",
        "s10_p1": "NoteWhen is not directed at children under 13 (or the minimum age required in your country). We do not knowingly collect personal information from children.",
        "s11_title": "11. International users",
        "s11_p1": "Your iCloud data is handled under Apple’s privacy terms and the region associated with your Apple ID. AI report requests may be routed to servers outside your country when processed by our report-generation services.",
        "s12_title": "12. Your choices",
        "s12_li1": "Choose which events to track and what details to record.",
        "s12_li2": "Disable iCloud sync by signing out of iCloud or disabling iCloud for NoteWhen in iOS Settings.",
        "s12_li3": "Revoke or limit HealthKit read and write access in the Health app or iOS Settings.",
        "s12_li4": "Turn off reminders in the app Settings.",
        "s12_li5": "Manage or cancel subscriptions in Settings &gt; Apple ID &gt; Subscriptions.",
        "s13_title": "13. Medical disclaimer",
        "s13_p1": "NoteWhen is for personal tracking only. It is not a medical device and does not provide diagnosis or treatment. Always consult a qualified healthcare professional for medical decisions.",
        "s14_title": "14. Changes to this policy",
        "s14_p1": "We may update this Privacy Policy from time to time. The effective date at the top of this page will change when we do. Continued use of the app after an update means you accept the revised policy.",
        "s15_title": "15. Contact",
        "s15_p1": 'Questions about this Privacy Policy: <a href="{contact}">{contact}</a>',
        "footer": '&copy; 2026 NoteWhen. <a href="{eula}">Apple Standard EULA</a> applies to app use.',
        "eula_label": "Apple Standard EULA",
    },
    "de": {
        "lang": "de",
        "dir": "ltr",
        "title": "NoteWhen Datenschutzerklärung",
        "meta_description": "Datenschutzerklärung für NoteWhen, eine persönliche Gesundheits- und Ereignis-Tracking-App für iOS.",
        "effective_date": "Gültig ab: 9. Juni 2026",
        "summary_label": "Zusammenfassung:",
        "summary": "NoteWhen ist ein persönlicher Gesundheits-Tracker. Ihre Tracking-Daten werden auf Ihren Geräten und in Ihrem privaten iCloud-Konto gespeichert. Mit Ihrer Erlaubnis kann die App ausgewählte Trainings-, Schlaf- und Wasserdaten mit Apple Health lesen und schreiben. Wenn Sie KI-Monatsberichte nutzen, wird eine zusammengefasste Übersicht Ihrer Daten an unsere Berichtserstellungsdienste gesendet. Wir verkaufen Ihre Daten nicht und verwenden keine Analyse-SDKs von Drittanbietern.",
        "intro": 'Diese Datenschutzerklärung beschreibt, wie NoteWhen („wir“, „uns“ oder „die App“) Informationen verarbeitet, wenn Sie die NoteWhen-iOS-App und das zugehörige Widget nutzen. Mit der Nutzung der App stimmen Sie dieser Richtlinie zu.',
        "s1_title": "1. Wer wir sind",
        "s1_p1": 'NoteWhen ist eine iOS-App. Bei Datenschutzfragen kontaktieren Sie uns über <a href="{contact}">GitHub Issues</a>.',
        "s2_title": "2. Von Ihnen bereitgestellte und von uns gespeicherte Informationen",
        "s2_intro": "Je nach Nutzung der App verarbeiten wir folgende Datenkategorien:",
        "s2_li1": "<strong>Gesundheits- und Wellness-Ereignisse</strong>, die Sie verfolgen möchten, z. B. Symptome, Medikamente, Blutdruck, Stuhlgang, Menstruation, Stimmung, Angstfragebögen (PHQ-9 und GAD-7), Schlaf, Bewegung, Wasseraufnahme, Mahlzeiten und Notizen zu jedem Eintrag.",
        "s2_li2": "<strong>Ereigniskonfiguration</strong>, einschließlich Namen, Symbole, Kategorien, Erinnerungsplänen und Medikamentenerinnerungen.",
        "s2_li3": "<strong>KI-Monatsberichte</strong>, einschließlich generiertem Berichtstext und Vorschlägen, sofern Sie diese Funktion nutzen.",
        "s2_li4": "<strong>App-Einstellungen</strong>, z. B. Sprache, Erscheinungsbild und Erinnerungen.",
        "s2_p1": "Diese Daten werden lokal auf Ihrem Gerät gespeichert und bei angemeldetem iCloud-Konto über Ihr privates iCloud-Konto auf Ihren Geräten synchronisiert. Wir betreiben kein separates Kontosystem oder Backend für Ihre Tracking-Daten.",
        "s3_title": "3. Apple Health (HealthKit)",
        "s3_p1": 'Wenn Sie die Health-Integration aktivieren, kann NoteWhen Trainings-, Schlaf- und Wasserdaten aus Apple Health <strong>lesen</strong>, um sie in Ihren Ereignisverlauf zu importieren. Mit Ihrer Erlaubnis kann die App auch Bewegungs-, Schlaf- und Wassereinträge, die Sie in NoteWhen erfassen, in Apple Health <strong>schreiben</strong>, damit Ihre Aufzeichnungen appübergreifend synchron bleiben.',
        "s3_li1": "<strong>Lesezugriff:</strong> importiert Workouts, Schlafsitzungen und Wasserproben aus Apple Health in NoteWhen.",
        "s3_li2": "<strong>Schreibzugriff:</strong> speichert Workouts, Schlafsitzungen und Wasseraufnahme, die Sie in NoteWhen erfassen, in Apple Health. Aus Apple Health importierte Einträge werden nicht zurückgeschrieben.",
        "s3_li3": "HealthKit-Daten werden auf Ihrem Gerät verarbeitet. Importierte oder erfasste Daten werden in Ihrer App-Datenbank und in iCloud gespeichert.",
        "s3_li4": "Wir nutzen HealthKit-Daten nicht für Werbung und verkaufen sie nicht.",
        "s3_li5": "Sie können Lese- und Schreibzugriff für jeden Datentyp jederzeit in der Health-App oder in den iOS-Einstellungen erteilen, einschränken oder widerrufen.",
        "s4_title": "4. KI-Monatsberichte",
        "s4_p1": "Wenn Sie einen Monatsbericht erstellen, erstellt die App eine Textzusammenfassung Ihrer erfassten Ereignisse für den gewählten Monat und sendet sie per HTTPS an unsere Berichtserstellungsdienste. Diese Dienste nutzen KI-Technologie von Drittanbietern. Die Anfrage enthält Ihre gewählte App-Sprache und Generierungsanweisungen, aber nicht Ihre Apple-ID oder iCloud-Anmeldedaten.",
        "s4_li1": "Die Berichtserstellung ist so ausgelegt, dass Anfragen nur vorübergehend verarbeitet werden und Ihre Tracking-Zusammenfassung nach Rückgabe des Berichts nicht gespeichert wird.",
        "s4_li2": "Generierte Berichte werden in Ihren App-Daten gespeichert und über Ihr iCloud-Konto synchronisiert.",
        "s4_li3": "KI-Ausgaben dienen nur der persönlichen Referenz und sind keine medizinische Beratung.",
        "s4_p2": "Sie können die Übermittlung von Daten zur Berichtserstellung vermeiden, indem Sie keine Monatsberichte erstellen oder diese Funktion nicht abonnieren bzw. nicht nutzen.",
        "s5_title": "5. Widget-Daten",
        "s5_p1": "Das NoteWhen-Widget zeigt Schnellerfassungs-Shortcuts mithilfe einer begrenzten Kopie von Ereignismetadaten (z. B. Name, Symbol und Sortierreihenfolge), die zwischen App und Widget geteilt werden. Der Ereignisverlauf wird nicht im Widget gespeichert.",
        "s6_title": "6. Benachrichtigungen",
        "s6_p1": "NoteWhen plant <strong>lokale</strong> Benachrichtigungen auf Ihrem Gerät für Ereigniserinnerungen, Medikamentenerinnerungen und optional verfügbare Monatsberichte. Benachrichtigungen können von Ihnen konfigurierte Ereignis- oder Medikamentennamen enthalten. Wir senden keine Push-Benachrichtigungen von eigenen Servern mit Ihren Gesundheitsdaten.",
        "s7_title": "7. Abonnements und Zahlungen",
        "s7_p1": "Optionale Abonnements für KI-Monatsberichte werden vollständig von Apple über Ihre Apple-ID abgewickelt. Wir erhalten den Abonnementstatus über StoreKit, um Funktionen freizuschalten. Wir erhalten oder speichern keine Zahlungskartendaten.",
        "s8_title": "8. Was wir nicht erfassen",
        "s8_li1": "Wir verkaufen Ihre persönlichen oder Gesundheitsdaten nicht.",
        "s8_li2": "Wir verwenden keine Werbe- oder Analyse-SDKs von Drittanbietern in der App.",
        "s8_li3": "Wir verlangen kein separates NoteWhen-Konto.",
        "s9_title": "9. Datenspeicherung und Löschung",
        "s9_li1": "Ihre Tracking-Daten bleiben erhalten, bis Sie sie in der App löschen, die App deinstallieren oder Daten aus iCloud entfernen.",
        "s9_li2": "Gelöschte Ereignisse werden 30 Tage lang inaktiv gehalten, bevor sie endgültig gelöscht werden, wie in der App beschrieben.",
        "s9_li3": "Das Löschen der App von einem Gerät entfernt lokale Daten auf diesem Gerät; iCloud-Kopien können bleiben, bis Sie den iCloud-Speicher in den iOS-Einstellungen verwalten.",
        "s10_title": "10. Kinder",
        "s10_p1": "NoteWhen richtet sich nicht an Kinder unter 13 Jahren (oder dem in Ihrem Land geltenden Mindestalter). Wir erfassen wissentlich keine personenbezogenen Daten von Kindern.",
        "s11_title": "11. Internationale Nutzer",
        "s11_p1": "Ihre iCloud-Daten unterliegen den Datenschutzbedingungen von Apple und der Region Ihrer Apple-ID. KI-Berichtsanfragen können bei der Verarbeitung durch unsere Berichtserstellungsdienste an Server außerhalb Ihres Landes weitergeleitet werden.",
        "s12_title": "12. Ihre Wahlmöglichkeiten",
        "s12_li1": "Wählen Sie, welche Ereignisse Sie verfolgen und welche Details Sie erfassen.",
        "s12_li2": "Deaktivieren Sie die iCloud-Synchronisierung, indem Sie sich von iCloud abmelden oder iCloud für NoteWhen in den iOS-Einstellungen deaktivieren.",
        "s12_li3": "Widerrufen oder beschränken Sie HealthKit-Lese- und Schreibzugriff in der Health-App oder in den iOS-Einstellungen.",
        "s12_li4": "Schalten Sie Erinnerungen in den App-Einstellungen aus.",
        "s12_li5": "Verwalten oder kündigen Sie Abonnements unter Einstellungen &gt; Apple-ID &gt; Abonnements.",
        "s13_title": "13. Medizinischer Haftungsausschluss",
        "s13_p1": "NoteWhen dient nur der persönlichen Dokumentation. Es ist kein Medizinprodukt und bietet keine Diagnose oder Behandlung. Konsultieren Sie bei medizinischen Entscheidungen stets qualifiziertes medizinisches Fachpersonal.",
        "s14_title": "14. Änderungen dieser Richtlinie",
        "s14_p1": "Wir können diese Datenschutzerklärung von Zeit zu Zeit aktualisieren. Das Gültigkeitsdatum oben auf dieser Seite ändert sich entsprechend. Die weitere Nutzung der App nach einer Aktualisierung gilt als Zustimmung zur überarbeiteten Richtlinie.",
        "s15_title": "15. Kontakt",
        "s15_p1": 'Fragen zu dieser Datenschutzerklärung: <a href="{contact}">{contact}</a>',
        "footer": '&copy; 2026 NoteWhen. Für die App-Nutzung gilt die <a href="{eula}">Apple Standard-EULA</a>.',
        "eula_label": "Apple Standard-EULA",
    },
}

def fmt(text: str) -> str:
    return text.format(contact=CONTACT_URL, eula=EULA_URL)


def render_page(locale: dict[str, str]) -> str:
    l = {key: fmt(value) for key, value in locale.items()}

    def section(title_key: str, body: str) -> str:
        return f"    <h2>{l[title_key]}</h2>\n{body}"

    def p(key: str) -> str:
        return f"    <p>\n      {l[key]}\n    </p>"

    def ul(*keys: str) -> str:
        items = "\n".join(f"      <li>{l[key]}</li>" for key in keys)
        return f"    <ul>\n{items}\n    </ul>"

    sections = "\n\n".join(
        [
            p("intro"),
            section("s1_title", p("s1_p1")),
            section(
                "s2_title",
                "\n".join(
                    [
                        p("s2_intro"),
                        ul("s2_li1", "s2_li2", "s2_li3", "s2_li4"),
                        p("s2_p1"),
                    ]
                ),
            ),
            section(
                "s3_title",
                "\n".join([p("s3_p1"), ul("s3_li1", "s3_li2", "s3_li3", "s3_li4", "s3_li5")]),
            ),
            section(
                "s4_title",
                "\n".join([p("s4_p1"), ul("s4_li1", "s4_li2", "s4_li3"), p("s4_p2")]),
            ),
            section("s5_title", p("s5_p1")),
            section("s6_title", p("s6_p1")),
            section("s7_title", p("s7_p1")),
            section("s8_title", ul("s8_li1", "s8_li2", "s8_li3")),
            section("s9_title", ul("s9_li1", "s9_li2", "s9_li3")),
            section("s10_title", p("s10_p1")),
            section("s11_title", p("s11_p1")),
            section(
                "s12_title",
                ul("s12_li1", "s12_li2", "s12_li3", "s12_li4", "s12_li5"),
            ),
            section("s13_title", p("s13_p1")),
            section("s14_title", p("s14_p1")),
            section("s15_title", p("s15_p1")),
        ]
    )

    return f"""<!DOCTYPE html>
<html lang="{l['lang']}" dir="{l['dir']}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{l['title']}</title>
  <meta name="description" content="{l['meta_description']}">
  <style>
    :root {{
      color-scheme: light dark;
      --bg: #ffffff;
      --text: #1d1d1f;
      --muted: #6e6e73;
      --border: #d2d2d7;
      --link: #0066cc;
      --card: #f5f5f7;
    }}
    @media (prefers-color-scheme: dark) {{
      :root {{
        --bg: #000000;
        --text: #f5f5f7;
        --muted: #a1a1a6;
        --border: #424245;
        --link: #2997ff;
        --card: #1c1c1e;
      }}
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.6;
      color: var(--text);
      background: var(--bg);
    }}
    main {{
      max-width: 720px;
      margin: 0 auto;
      padding: 32px 20px 64px;
    }}
    h1 {{
      font-size: 2rem;
      line-height: 1.15;
      margin: 0 0 8px;
    }}
    .meta {{
      color: var(--muted);
      font-size: 0.95rem;
      margin-bottom: 28px;
    }}
    h2 {{
      font-size: 1.25rem;
      margin: 32px 0 12px;
    }}
    p, li {{ font-size: 1rem; }}
    ul {{ padding-left: 1.25rem; }}
    li {{ margin: 8px 0; }}
    a {{ color: var(--link); }}
    .summary {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px 18px;
      margin: 24px 0;
    }}
    footer {{
      margin-top: 48px;
      padding-top: 24px;
      border-top: 1px solid var(--border);
      color: var(--muted);
      font-size: 0.9rem;
    }}
  </style>
</head>
<body>
  <main>
    <h1>{l['title']}</h1>
    <p class="meta">{l['effective_date']}</p>

    <div class="summary">
      <p><strong>{l['summary_label']}</strong> {l['summary']}</p>
    </div>

{sections}

    <footer>
      <p>{l['footer']}</p>
    </footer>
  </main>
</body>
</html>
"""


def main() -> None:
    import json

    locales_path = OUTPUT_DIR / "privacy-locales.json"
    if locales_path.exists():
        with locales_path.open(encoding="utf-8") as handle:
            LOCALES.update(json.load(handle))

    for code, locale in LOCALES.items():
        filename = "privacy.html" if code == "en" else f"privacy.{code}.html"
        output_path = OUTPUT_DIR / filename
        output_path.write_text(render_page(locale), encoding="utf-8")
        print(f"Wrote {output_path.name}")


if __name__ == "__main__":
    main()
