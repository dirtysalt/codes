(function () {
  // Default sites and starting URL used by Side Panel and Options.
  // Edit this file to change first-run defaults.
  const sites = [
    { label: 'ChatGPT (chatgpt.com)', url: 'https://chatgpt.com/' },
    { label: 'Gemini (gemini.google.com)', url: 'https://gemini.google.com/' },
    { label: 'DeepSeek (chat.deepseek.com)', url: 'https://chat.deepseek.com/' },
    { label: 'Qwen (chat.qwen.ai)', url: 'https://chat.qwen.ai/' }
  ];

  window.DEFAULT_URL = 'https://chatgpt.com/';
  window.DEFAULT_SITES = sites;
})();
