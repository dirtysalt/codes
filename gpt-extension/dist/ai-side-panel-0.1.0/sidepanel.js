/* global chrome */
(function () {
  const siteSelect = document.getElementById('site');
  const iframe = document.getElementById('frame');
  const openTabBtn = document.getElementById('openTab');
  const manageBtn = document.getElementById('manage');
  const openTabBtn2 = document.getElementById('openTab2');
  const retryBtn = document.getElementById('retry');
  const overlay = document.getElementById('overlay');

  const DEFAULT_URL = window.DEFAULT_URL || 'https://chatgpt.com/';
  const DEFAULT_SITES = window.DEFAULT_SITES || [
    { label: 'ChatGPT (chatgpt.com)', url: 'https://chatgpt.com/' },
    { label: 'ChatGPT (chat.openai.com)', url: 'https://chat.openai.com/' }
  ];

  function renderSites(sites, selectedUrl) {
    siteSelect.innerHTML = '';
    sites.forEach(({ label, url }) => {
      const opt = document.createElement('option');
      opt.value = url;
      opt.textContent = label || url;
      siteSelect.appendChild(opt);
    });
    if (sites.some(s => s.url === selectedUrl)) {
      siteSelect.value = selectedUrl;
    } else if (sites.length) {
      siteSelect.value = sites[0].url;
      selectedUrl = sites[0].url;
    }
    setIframeSrc(siteSelect.value);
  }

  async function loadPrefs() {
    try {
      const { sites = DEFAULT_SITES, selectedUrl = DEFAULT_URL } = await chrome.storage.sync.get({ sites: DEFAULT_SITES, selectedUrl: DEFAULT_URL });
      renderSites(sites, selectedUrl);
    } catch (e) {
      renderSites(DEFAULT_SITES, DEFAULT_URL);
    }
  }

  let loadTimer = null;
  function setIframeSrc(url) {
    overlay.style.display = 'none';
    // Reset iframe to force a fresh navigation path
    iframe.removeAttribute('src');
    // Start a watchdog: if no load within 4s, show overlay
    if (loadTimer) clearTimeout(loadTimer);
    loadTimer = setTimeout(() => {
      overlay.style.display = 'flex';
    }, 4000);
    iframe.src = url;
  }

  iframe.addEventListener('load', () => {
    if (loadTimer) clearTimeout(loadTimer);
    overlay.style.display = 'none';
  });

  siteSelect.addEventListener('change', async () => {
    const url = siteSelect.value;
    setIframeSrc(url);
    try {
      await chrome.storage.sync.set({ selectedUrl: url });
    } catch (_) {}
  });

  openTabBtn.addEventListener('click', () => {
    const url = siteSelect.value;
    chrome.tabs.create({ url });
  });

  if (manageBtn) {
    manageBtn.addEventListener('click', () => {
      if (chrome.runtime.openOptionsPage) {
        chrome.runtime.openOptionsPage();
      } else {
        chrome.tabs.create({ url: 'options.html' });
      }
    });
  }

  if (openTabBtn2) {
    openTabBtn2.addEventListener('click', () => {
      const url = siteSelect.value;
      chrome.tabs.create({ url });
    });
  }

  if (retryBtn) {
    retryBtn.addEventListener('click', () => {
      setIframeSrc(siteSelect.value);
    });
  }

  loadPrefs();
})();
