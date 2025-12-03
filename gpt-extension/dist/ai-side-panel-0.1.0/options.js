/* global chrome */
(function () {
  const rows = document.getElementById('rows');
  const form = document.getElementById('addForm');
  const labelInput = document.getElementById('label');
  const urlInput = document.getElementById('url');

  const DEFAULT_SITES = window.DEFAULT_SITES || [
    { label: 'ChatGPT (chatgpt.com)', url: 'https://chatgpt.com/' },
    { label: 'ChatGPT (chat.openai.com)', url: 'https://chat.openai.com/' }
  ];

  function normalizeUrl(u) {
    try {
      const url = new URL(u);
      if (url.protocol !== 'https:') return null;
      // Ensure trailing slash for consistency
      if (!url.pathname.endsWith('/')) url.pathname += '/';
      url.hash = '';
      return url.toString();
    } catch (_) {
      return null;
    }
  }

  async function loadSites() {
    const { sites = DEFAULT_SITES } = await chrome.storage.sync.get({ sites: DEFAULT_SITES });
    return Array.isArray(sites) ? sites : DEFAULT_SITES;
  }

  function render(sites) {
    rows.innerHTML = '';
    sites.forEach((site, idx) => {
      const tr = document.createElement('tr');
      const tdLabel = document.createElement('td');
      const tdUrl = document.createElement('td');
      const tdAct = document.createElement('td');
      tdAct.className = 'actions';

      tdLabel.textContent = site.label || site.url;
      tdUrl.textContent = site.url;

      const del = document.createElement('button');
      del.textContent = 'Delete';
      del.addEventListener('click', async () => {
        const updated = (await loadSites()).filter((_, i) => i !== idx);
        await chrome.storage.sync.set({ sites: updated });
        render(updated);
      });

      tdAct.appendChild(del);
      tr.appendChild(tdLabel);
      tr.appendChild(tdUrl);
      tr.appendChild(tdAct);
      rows.appendChild(tr);
    });
  }

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const label = labelInput.value.trim();
    const normalized = normalizeUrl(urlInput.value.trim());
    if (!label || !normalized) {
      alert('Please enter a label and a valid HTTPS URL (e.g., https://example.com/).');
      return;
    }
    const sites = await loadSites();
    if (sites.some(s => s.url === normalized)) {
      alert('This URL is already in the list.');
      return;
    }
    const updated = [...sites, { label, url: normalized }];
    await chrome.storage.sync.set({ sites: updated });
    labelInput.value = '';
    urlInput.value = '';
    render(updated);
  });

  (async function init() {
    render(await loadSites());
  })();
})();
