# Repository Guidelines

This repository hosts a minimal Chrome Extension that opens a Side Panel with quick access to AI assistants. Use this guide to contribute consistently and safely.

## Project Structure & Module Organization
- Root files: `manifest.json`, `background.js`, `sidepanel.html`, `sidepanel.js`, `rules.json`.
- Assets: place icons or images in `assets/` (create if needed).
- No build system by default; extension loads as “unpacked”.

## Build, Test, and Development Commands
- Load locally: Chrome → `chrome://extensions` → Enable Developer Mode → Load Unpacked → select repo root.
- Reload after changes: click “Reload” on the extension card.
- Zip for sharing: `zip -r dist.zip . -x '*.git*' 'dist*'` (optional).

## Coding Style & Naming Conventions
- JavaScript: ES2020+, 2-space indentation, semicolons required.
- Filenames: lower-kebab-case for files (`background.js`, `sidepanel.html`).
- Keep functions small and focused; prefer early returns.
- Permissions: request the minimum; document any additions in PRs.

## Testing Guidelines
- Manual testing: verify Side Panel opens via the toolbar icon and keyboard shortcut; confirm site switching works.
- Cross-domain embedding may fail due to site headers; ensure fallback UX (e.g., “Open in Tab” button) remains functional.
- When adding features, include a brief test checklist in the PR description.

## Commit & Pull Request Guidelines
- Commits: imperative mood, concise scope. Example: `feat: add keyboard shortcut to open side panel`.
- PRs: include purpose, screenshots or short Loom/GIF (if UI changes), steps to test, and any permission changes.
- Link issues with `Closes #NN` when applicable.

## Security & Configuration Tips
- Least-privilege permissions in `manifest.json` are mandatory; avoid broad host access unless justified.
- Header-modification rules in `rules.json` should target specific domains only and be explained in PRs.
- Do not include secrets; this project has no server-side components.

## Agent-Specific Instructions
- Follow this AGENTS.md when creating or editing files.
- Keep changes minimal and focused; prefer incremental PRs.
