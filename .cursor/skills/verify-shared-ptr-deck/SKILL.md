---
name: verify-shared-ptr-deck
description: Build the Mastering C++ shared_ptr slidev deck (slidev-shared-ptr-presentation/) and verify the production build boots and renders its themed slide shell.
---
# shared_ptr deck verification

## Launch
Node 22.12+. `npm install --ignore-scripts` in slidev-shared-ptr-presentation/ (deps unpinned; executed proof used slidev 51.8.2). Build: `npm run build` (slidev build --theme seriph) -> dist/.

## Doctor + Drive
`python3 .cursor/skills/verify-shared-ptr-deck/verify.py` (stdlib only) runs the real production build, serves dist with SPA fallback on an ephemeral loopback port, renders in headless Chrome and asserts build success plus a substantial rendered capture (overview.png: themed shell and slide list of all 15 slides). FAILURES=0 exit 0.

## Evidence
build.log, overview.png, result.json in .verification-evidence/shared-ptr-deck/. Build green itself proves every slide's Vue template compiles (slidev transforms each slide through vite:vue).

## Cleanup
Ephemeral server terminated; dist/ is a build artifact.

## Known boundaries
External images (placehold.co, flaticon, giphy) and Google fonts need network at view time. /images/memory-leak-visualization.gif referenced by one slide does not exist in the repo (no public/ dir) - Vite externalizes it; that slide's local image is broken. Old `# ---` comment-marker lines render as literal "—" headings on some slides (cosmetic, pre-existing authoring style). No per-slide pixel acceptance, no export/PDF, no presenter mode, no hosted claim (netlify.toml/vercel.json exist but deployment unverified).
