# Vibe website

Standalone, buildless English marketing, support and draft privacy website. No JavaScript, runtime dependencies, tracking or backend. The iOS repository remains separate.

## Preview locally

From this folder:

```sh
python3 scripts/check_site.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory site
```

Open http://127.0.0.1:8000/ in your browser. Pages are `/`, `/support/` and `/privacy/`. Stop the server with Ctrl-C. For repository-subpath testing, serve the project root and visit `/site/`; the same relative paths work at `/REPOSITORY/` on Pages.

## GitHub Pages setup (not performed)

1. Complete the release checklist in `notes/privacy-review.md`. The privacy page is visibly a draft and support has no operational contact email.
2. Create a separate GitHub repository. For standard free GitHub Pages hosting, use a public repository; private-repository support depends on your GitHub plan. Do not add these files to the iOS repository.
3. Initialize this folder as its own Git repository with `main`, commit the files and connect the new repository. No repository has been initialized or remote created by this implementation.
4. In the new repository, open **Settings → Pages → Build and deployment → Source → GitHub Actions**.
5. Push `main`, or run **Deploy Vibe website to GitHub Pages** from Actions. This publishes only `site/`; notes, scripts and design documentation are excluded from the Pages artifact.
6. Open the URL reported by the `github-pages` environment and verify all three pages under its repository prefix. HTTPS is provided by GitHub Pages. No custom domain is configured.

Workflow based on [GitHub’s static Pages starter](https://github.com/actions/starter-workflows/blob/main/pages/static.yml) and [custom Pages workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages), checked 2026-10-15.

**Important:** Excluding notes from the Pages artifact does not make them confidential in a public source repository. Keep private operator deliberations and credentials outside the repository. Current notes contain no credentials or private contact information.

## Updating content

Edit the three HTML pages in `site/` and shared `site/assets/site.css`. Update shared headers and footers on all pages together. Keep page links relative; root-absolute `/assets/` paths break project Pages hosting. Replace the coming-soon text with an App Store link only when one is available. Do not add a fabricated email link or waitlist form.

The website has no canonical URL or absolute social-preview URL until the domain is known. Add those once the deployment URL is confirmed. App Store URLs and the iOS app’s privacy URL are intentionally untouched.

See `notes/assets.md` for image provenance and `DESIGN.md` for the website design system.
