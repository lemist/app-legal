#!/usr/bin/env python3
"""Generate localized NoteWhen support HTML pages."""

from __future__ import annotations

import json
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent
CONTACT_URL = "https://github.com/lemist/app-legal/issues"

LOCALES: dict[str, dict[str, str]] = {
    "en": {
        "lang": "en",
        "dir": "ltr",
        "title": "NoteWhen Support",
        "meta_description": "Support information for NoteWhen, a personal health event tracking app for iOS.",
        "intro": "This page explains how to get help with NoteWhen and answers common questions about using the app.",
        "contact_heading": "Contact us",
        "contact_body": 'If you need assistance, report a bug, or request a feature, please contact us through <a href="{contact}">GitHub Issues</a>.',
        "help_heading": "Common topics",
        "gs_title": "Getting started",
        "gs_body": "NoteWhen lets you define health events (such as symptoms, medications, sleep, or exercise) and record each occurrence with a timestamp and optional notes. Use the + button on the Events tab to add events, tap an event to view history, or use the widget for quick recording.",
        "icloud_title": "iCloud sync",
        "icloud_body": "Your data is stored on your device and synced through your private iCloud account when you are signed in to iCloud. If data does not appear on another device, confirm you are using the same Apple ID and that iCloud is enabled for NoteWhen in iOS Settings.",
        "health_title": "Apple Health",
        "health_body": "You can import workouts, sleep, and water from Apple Health, and optionally save entries you log in NoteWhen back to Apple Health. Manage read and write permissions in the Health app or iOS Settings. If access was denied, open an event detail screen and use the sync controls to request access again.",
        "reminders_title": "Reminders",
        "reminders_body": "Configure logging and medication reminders in Settings. Reminders are delivered as local notifications on your device only.",
        "widget_title": "Widget",
        "widget_body": "Add the NoteWhen widget to record events quickly from your Home Screen. The widget shows shortcuts for your active events. Event history is stored in the main app, not the widget.",
        "reports_title": "AI monthly reports",
        "reports_body": "Optional monthly reports summarize your tracked events using AI. Reports require an active subscription. Generated reports are saved in the app and synced via iCloud. AI output is for personal reference only, not medical advice.",
        "subs_title": "Subscriptions",
        "subs_body": "Manage AI monthly report subscriptions in Settings &gt; Apple ID &gt; Subscriptions. Purchases are processed by Apple; we do not store your payment card details.",
        "privacy_heading": "Privacy",
        "privacy_body": 'See our <a href="{privacy_href}">Privacy Policy</a> for how NoteWhen handles your information.',
        "medical_heading": "Medical note",
        "medical_body": "NoteWhen is for personal tracking only. It is not a medical device. Consult a qualified healthcare professional for medical decisions.",
    },
    "de": {
        "lang": "de",
        "dir": "ltr",
        "title": "NoteWhen Support",
        "meta_description": "Support-Informationen für NoteWhen, eine persönliche Gesundheits- und Ereignis-Tracking-App für iOS.",
        "intro": "Diese Seite erklärt, wie Sie Hilfe zu NoteWhen erhalten, und beantwortet häufige Fragen zur Nutzung der App.",
        "contact_heading": "Kontakt",
        "contact_body": 'Wenn Sie Hilfe benötigen, einen Fehler melden oder eine Funktion vorschlagen möchten, kontaktieren Sie uns über <a href="{contact}">GitHub Issues</a>.',
        "help_heading": "Häufige Themen",
        "gs_title": "Erste Schritte",
        "gs_body": "Mit NoteWhen können Sie Gesundheitsereignisse (z. B. Symptome, Medikamente, Schlaf oder Bewegung) definieren und jedes Vorkommen mit Zeitstempel und optionalen Notizen erfassen. Verwenden Sie die +-Taste auf dem Tab „Ereignisse“, um Ereignisse hinzuzufügen, tippen Sie auf ein Ereignis für den Verlauf oder nutzen Sie das Widget für die Schnellerfassung.",
        "icloud_title": "iCloud-Synchronisierung",
        "icloud_body": "Ihre Daten werden auf Ihrem Gerät gespeichert und über Ihr privates iCloud-Konto synchronisiert, wenn Sie bei iCloud angemeldet sind. Wenn Daten auf einem anderen Gerät fehlen, prüfen Sie, ob dieselbe Apple-ID verwendet wird und iCloud für NoteWhen in den iOS-Einstellungen aktiviert ist.",
        "health_title": "Apple Health",
        "health_body": "Sie können Workouts, Schlaf und Wasser aus Apple Health importieren und optional in NoteWhen erfasste Einträge zurück nach Apple Health schreiben. Verwalten Sie Lese- und Schreibberechtigungen in der Health-App oder in den iOS-Einstellungen. Wenn der Zugriff verweigert wurde, öffnen Sie eine Ereignisdetailansicht und nutzen Sie die Sync-Steuerung, um erneut Zugriff anzufordern.",
        "reminders_title": "Erinnerungen",
        "reminders_body": "Konfigurieren Sie Protokollierungs- und Medikamentenerinnerungen in den Einstellungen. Erinnerungen werden nur als lokale Benachrichtigungen auf Ihrem Gerät zugestellt.",
        "widget_title": "Widget",
        "widget_body": "Fügen Sie das NoteWhen-Widget hinzu, um Ereignisse schnell vom Home-Bildschirm aus zu erfassen. Das Widget zeigt Verknüpfungen für Ihre aktiven Ereignisse. Der Ereignisverlauf wird in der Haupt-App gespeichert, nicht im Widget.",
        "reports_title": "KI-Monatsberichte",
        "reports_body": "Optionale Monatsberichte fassen Ihre erfassten Ereignisse mithilfe von KI zusammen. Berichte erfordern ein aktives Abonnement. Generierte Berichte werden in der App gespeichert und über iCloud synchronisiert. KI-Ausgaben dienen nur der persönlichen Referenz, nicht der medizinischen Beratung.",
        "subs_title": "Abonnements",
        "subs_body": "Verwalten Sie Abonnements für KI-Monatsberichte unter Einstellungen &gt; Apple-ID &gt; Abonnements. Käufe werden von Apple abgewickelt; wir speichern keine Zahlungskartendaten.",
        "privacy_heading": "Datenschutz",
        "privacy_body": 'In unserer <a href="{privacy_href}">Datenschutzerklärung</a> erfahren Sie, wie NoteWhen mit Ihren Informationen umgeht.',
        "medical_heading": "Medizinischer Hinweis",
        "medical_body": "NoteWhen dient nur der persönlichen Dokumentation. Es ist kein Medizinprodukt. Konsultieren Sie bei medizinischen Entscheidungen qualifiziertes medizinisches Fachpersonal.",
    },
}


def fmt(text: str, privacy_href: str) -> str:
    return text.format(contact=CONTACT_URL, privacy_href=privacy_href)


def privacy_href_for(code: str) -> str:
    return "privacy.html" if code == "en" else f"privacy.{code}.html"


def render_page(code: str, locale: dict[str, str]) -> str:
    privacy_href = privacy_href_for(code)
    l = {key: fmt(value, privacy_href) for key, value in locale.items()}

    topic_blocks = []
    for key in ("gs", "icloud", "health", "reminders", "widget", "reports", "subs"):
        topic_blocks.append(f"    <h3>{l[key + '_title']}</h3>")
        topic_blocks.append(f"    <p>{l[key + '_body']}</p>")
    topics = "\n".join(topic_blocks)

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
    h2 {{
      font-size: 1.25rem;
      margin: 32px 0 12px;
    }}
    h3 {{
      font-size: 1.05rem;
      margin: 24px 0 8px;
    }}
    p, li {{ font-size: 1rem; }}
    a {{ color: var(--link); }}
    .intro {{
      color: var(--muted);
      margin-bottom: 24px;
    }}
    .card {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px 18px;
      margin: 16px 0 24px;
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
    <p class="intro">{l['intro']}</p>

    <h2>{l['contact_heading']}</h2>
    <div class="card">
      <p>{l['contact_body']}</p>
    </div>

    <h2>{l['help_heading']}</h2>
{topics}

    <h2>{l['privacy_heading']}</h2>
    <p>{l['privacy_body']}</p>

    <h2>{l['medical_heading']}</h2>
    <p>{l['medical_body']}</p>

    <footer>
      <p>&copy; 2026 NoteWhen</p>
    </footer>
  </main>
</body>
</html>
"""


def main() -> None:
    locales_path = OUTPUT_DIR / "support-locales.json"
    if locales_path.exists():
        with locales_path.open(encoding="utf-8") as handle:
            LOCALES.update(json.load(handle))

    for code, locale in LOCALES.items():
        filename = "support.html" if code == "en" else f"support.{code}.html"
        output_path = OUTPUT_DIR / filename
        output_path.write_text(render_page(code, locale), encoding="utf-8")
        print(f"Wrote {output_path.name}")


if __name__ == "__main__":
    main()
