// Opens the side panel when the toolbar icon is clicked.
chrome.runtime.onInstalled.addListener(() => {
  if (chrome.sidePanel && chrome.sidePanel.setPanelBehavior) {
    chrome.sidePanel.setPanelBehavior({ openPanelOnActionClick: true });
  }
});

// Keyboard shortcut: open the side panel in the last focused window.
chrome.commands.onCommand.addListener((command) => {
  if (command !== 'open-side-panel') return;
  if (!chrome.sidePanel || !chrome.sidePanel.open) return;
  chrome.windows.getLastFocused({}, (win) => {
    if (!win || win.id === undefined) return;
    chrome.sidePanel.open({ windowId: win.id });
  });
});

