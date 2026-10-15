# Privacy draft: maintainer review

Informational drafting assistance only; not legal advice. The requested pm-toolkit privacy-policy skill requires qualified privacy counsel review before publication. The public policy is visibly marked draft. Do not use its URL as a final App Store privacy policy yet.

## Evidence and data inventory — inspected 2026-10-15

| Data/activity | Current behavior | Release confirmation |
| --- | --- | --- |
| Selected images, text, editing choices and project thumbnails | Local project files; no photo upload in current content flows | Check the release binary and device-backup behavior |
| Photo library | Apple picker for selected imports; add-only permission for saving | Verify denied-permission flow on device |
| Catalogue, artwork and private package requests | Cloudflare R2 and Worker; host may see IP/request metadata | Confirm accounts, logging configuration, processor roles and retention |
| Subscription transaction | Signed StoreKit transaction sent to broker, verified with Apple; broker checks current status | Confirm production deployment; Worker configuration inspected is Sandbox |
| Preferences and installation ID | UserDefaults/local storage | Confirm full local inventory and removal behavior |
| Event telemetry | Local OSLog; no VibeTelemetryURL in inspected Info.plist | Recheck effective release build settings and runtime endpoint, not just source plist |
| Optional remote event payload | Installation ID, timestamp, template/format/count, duration, onboarding and purchase context | Update policy, legal basis and user controls BEFORE enabling |
| Support email and attachments | No configured public email yet | Choose provider, contact channel, access controls and retention |
| Website | Static assets; no added analytics, forms, JS, cookies or local storage | GitHub hosting technical data still applies |

Source paths in the separate `/Users/michelecoppola/Documents/vibe` repo:

- `Vibe/Core/Services/Telemetry.swift` and `Vibe.xcodeproj/Vibe-Info.plist`
- `Vibe/Features/Projects/Services/ProjectStore+Sessions.swift`, project deletion services and editor import/export services
- `Vibe/Features/Subscriptions/PROPackageBroker.swift`, `EntitlementStore.swift` and `Views/PaywallView.swift`
- `worker/src/index.ts`, `worker/wrangler.jsonc` and `worker/README.md`
- `docs/product/app_behavior.md`, `docs/product/technical_architecture.md`, `docs/brand/brand-guide.md`

Code indicates implemented capability, not proof of production operation, App Store availability, contractual safeguards or legal compliance.

## Publication checklist

- [ ] Replace all bracketed placeholders with verified operator name, public address and privacy email; add a working support email.
- [ ] Confirm launch countries and intended ages; counsel determines applicable EU/UK, California and other rules. Do not add age thresholds or jurisdiction-specific rights as unsupported boilerplate.
- [ ] Confirm each legal basis; device permission does not automatically establish GDPR consent for all processing.
- [ ] Confirm provider roles, DPAs where required, locations and actual international-transfer mechanisms.
- [ ] Set support, broker, security-log and backup retention periods or specific justified criteria. Do not invent fixed periods.
- [ ] Establish and test request receipt, identity verification, access/deletion/objection handling and applicable deadlines; add supervisory authority and representative/DPO details if required.
- [ ] Confirm any sale/sharing statement under the relevant legal definitions and all actual business practices.
- [ ] Verify local storage, device backups, temporary exports, caches and deletion behavior against the release binary.
- [ ] Recheck telemetry endpoints in release configuration and generated Info.plist. If enabled, revise public disclosures and implement required consent/choices first.
- [ ] Verify Cloudflare production settings and security operations; do not claim audits or additional encryption without evidence.
- [ ] Obtain qualified legal review, resolve all LEGAL REVIEW REQUIRED markers, set the effective date and decide how material changes will be communicated.
- [ ] Review asset rights and every public claim; update the marketing CTA only after an App Store URL exists.
- [ ] After deployment, confirm all pages under the actual GitHub Pages subpath. Update app privacy configuration separately when authorized.

## Primary references

- [European Commission: individual data-protection rights](https://commission.europa.eu/law/law-topic/data-protection/information-individuals_en)
- [GitHub General Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement)
- [Apple privacy](https://www.apple.com/legal/privacy/)
- [Cloudflare privacy](https://www.cloudflare.com/privacypolicy/)
- [Apple subscription management](https://support.apple.com/en-us/118428)

Check provider terms and legal requirements again at publication. This inventory is a technical drafting aid, not a compliance certification.
