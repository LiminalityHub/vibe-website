# Verification — 2026-10-15

## Result
The website is deployed at <https://liminalityhub.github.io/vibe-website/>. Privacy content remains a pre-launch draft; deployment is not approval for legal publication or evidence that the iOS app is live.

## Checks performed
- Dependency-free `python3 scripts/check_site.py`: all three pages, local navigation/assets, fragment targets, unique IDs, English language/title/headings and artifact boundary passed.
- Local HTTP smoke check: all three pages, stylesheet and both image assets returned 200 under `/site/`, simulating project Pages hosting. The short check closed image connections after checking headers, producing harmless server-side broken-pipe messages; the regular browser loaded the images fully.
- Browser inspection: desktop marketing and support full-page captures, desktop privacy introduction; 390px mobile marketing/support and privacy introduction. No observed layout defects remained after the privacy-notice correction.
- Browser measurements at 320px: all three documents had scroll width equal to viewport width and no main-content elements extending past the right edge. All three also measured 390px scroll width at the 390px viewport.
- Keyboard Enter opened the support FAQ and privacy contents disclosure; skip link moved focus to `main`.
- Workflow reviewed against GitHub's official static starter; upload path is restricted to `site/`.
- GitHub Actions run 38778902405 succeeded: `Verify static site`, `Configure Pages`, artifact upload and Pages deployment passed.
- Published homepage returned HTTP 200 and rendered the expected HTML. GitHub Pages API confirms public HTTPS site at `https://liminalityhub.github.io/vibe-website/`.

## Review scope and limitations
One-agent review performed inline to honor the approved build plan; no independent reviewer was used. The visual pass identified the mobile privacy contents delaying the draft notice. One correction batch moved the notice up and collapsed the contents; the confirmation pass verified that correction. Product and design documentation match the final implementation.

No automated external-link crawl, assistive-technology audit or cross-browser matrix was performed. The policy's release configuration, operational provider settings and legal commitments must be confirmed using `privacy-review.md` before launch. The repository is public, so every source file and maintainer note is publicly readable even though Pages deploys only `site/`.
