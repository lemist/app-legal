# app-legal

Public static legal pages (privacy policies, terms, etc.) for iOS apps, hosted on **GitHub Pages**.

## Live URLs

After GitHub Pages is enabled:

| App | Privacy Policy |
|-----|----------------|
| NoteWhen (English) | https://lemist.github.io/app-legal/notewhen/privacy.html |
| NoteWhen (localized) | `privacy.<locale>.html` — e.g. `privacy.de.html`, `privacy.zh-Hans.html`, `privacy.ja.html` |

Supported locales: `en`, `de`, `es`, `fr`, `hi`, `it`, `ja`, `ko`, `pt-BR`, `ru`, `ar`, `zh-Hans`, `zh-Hant`.

Regenerate pages after editing translations:

```bash
python3 notewhen/build-privacy-pages.py
```

Index: https://lemist.github.io/app-legal/

## Adding a new app

1. Create a folder named after the app slug, e.g. `myapp/`
2. Add `privacy.html` (and optional `terms.html`) inside it
3. Link it from `index.html`
4. Push to `main` — GitHub Actions deploys automatically

Suggested URL pattern for App Store Connect:

`https://lemist.github.io/app-legal/<app-slug>/privacy.html`

## One-time GitHub setup

1. Create a **public** repository named `app-legal` under your GitHub account
2. Push this folder to `main`
3. Go to **Settings → Pages → Build and deployment → Source: GitHub Actions**
4. Run or wait for the **Deploy legal pages to GitHub Pages** workflow

GitHub Pages is free on public repositories.

## Local preview

```bash
python3 -m http.server 8080
```

Open http://localhost:8080/notewhen/privacy.html
