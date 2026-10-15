# Vibe website

Live buildless static marketing, support and draft privacy website: <https://liminalityhub.github.io/vibe-website/>. Source: <https://github.com/LiminalityHub/vibe-website>. No JavaScript, runtime dependencies, tracking or backend. The iOS repository is separate.

## Preview locally

From this folder:

```sh
python3 scripts/check_site.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory site
```

Open http://127.0.0.1:8000/ in your browser. Pages are `/`, `/support/` and `/privacy/`. Stop the server with Ctrl-C. For repository-subpath testing, serve the project root and visit `/site/`; the same relative paths work at `/REPOSITORY/` on Pages.

## GitHub Pages

This public repository deploys `site/` through `.github/workflows/pages.yml` on every push to `main` and on manual dispatch. GitHub Pages uses Actions as its source and enforces HTTPS. No custom domain is configured.

The website is live, but the privacy policy remains a draft and support has no operational email. Complete `notes/privacy-review.md` before presenting the policy as final. The workflow uploads only the public website, but **the entire source repository is public**. The `notes/` directory, `DESIGN.md`, `PRODUCT.md`, and verification scripts are visible to everyone; do not put private operator details or credentials here.

Workflow based on [GitHub’s static Pages starter](https://github.com/actions/starter-workflows/blob/main/pages/static.yml) and [custom Pages workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages), checked 2026-10-15.

## Updating content

Edit the three HTML pages in `site/` and shared `site/assets/site.css`. Update shared headers and footers on all pages together. Keep page links relative; root-absolute `/assets/` paths break project Pages hosting. Replace the coming-soon text with an App Store link only when one is available. Do not add a fabricated email link or waitlist form.

The website has no canonical URL or absolute social-preview URL beyond its current Pages address. App Store URLs and the iOS app’s privacy URL are intentionally untouched.

See `notes/assets.md` for image provenance, `notes/verification.md` for deployment verification, and `DESIGN.md` for the website design system.
