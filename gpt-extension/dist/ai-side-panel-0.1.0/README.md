AI Side Panel (Chrome Extension)

Quick start
- Load at chrome://extensions → Developer Mode → Load unpacked → select this folder.
- Open via toolbar icon or shortcut: Ctrl+Shift+Y (Win/Linux) or Command+Shift+Y (macOS).
 - Choose ChatGPT, DeepSeek (chat.deepseek.com), Gemini (google), or Qwen in the panel. If the view is blank, click “Open in Tab”.

Customize shortcut
- Change at chrome://extensions/shortcuts. Search for “AI Side Panel” and set your preferred keys.

Manage sites (Options)
- Open the extension’s Options page from the extension card or from the Side Panel’s “Manage Sites” button.
- Add your own HTTPS URLs (e.g., https://chat.qwen.ai/). These appear in the Side Panel selector.
 - To change first-run defaults, edit `defaults.js` (shared by Side Panel and Options).

Notes
- Some sites block iframes via X-Frame-Options or CSP. The extension includes DNR rules to remove common blocking headers for listed hosts, but this may not always work and may conflict with site policies.
- Permissions are limited to the Side Panel API, storage, and the listed hosts for DNR.

Build and package
- Optional: add extra approved hosts for DNR in `build/hosts.json` (e.g., "example.com").
- Optional: tweak icon colors in `build/branding.json`.
- Run: `python3 tools/build.py`
- Output: `dist/ai-side-panel-<version>/` and `dist/ai-side-panel-<version>.zip`
