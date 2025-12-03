const palette = [
  '#22c55e', '#3b82f6', '#f59e0b', '#ec4899', '#a855f7', '#ef4444', '#14b8a6',
  '#eab308', '#8b5cf6', '#0ea5e9'
];

const PRICE_STATE_KEY = 'stockdb-ui-state';
const PORTFOLIO_DATA_KEY = 'stockdb-portfolios';
const PORTFOLIO_UI_KEY = 'stockdb-portfolio-ui';
const ACTIVE_TAB_KEY = 'stockdb-active-tab';

let priceChart;
let portfolioChart;
let lastSeriesMeta = [];
let lastPortfolioMeta = [];
let availableSymbols = [];
let portfolios = [];

function setStatus(msg, isError = false) {
  const el = document.getElementById('status');
  el.textContent = msg;
  el.style.color = isError ? '#ef4444' : '#94a3b8';
}

function setPortfolioStatus(msg, isError = false) {
  const el = document.getElementById('pf-status');
  el.textContent = msg;
  el.style.color = isError ? '#ef4444' : '#94a3b8';
}

function defaultDates(startId, endId, yearsBack = 1) {
  const startInput = document.getElementById(startId);
  const endInput = document.getElementById(endId);
  if (!startInput.value) {
    const start = new Date();
    start.setFullYear(start.getFullYear() - yearsBack);
    startInput.value = start.toISOString().slice(0, 10);
  }
  if (!endInput.value) {
    const end = new Date();
    endInput.value = end.toISOString().slice(0, 10);
  }
}

async function loadSymbols(selected = []) {
  try {
    const res = await fetch('/api/symbols');
    const symbols = await res.json();
    availableSymbols = symbols;
    const select = document.getElementById('symbols');
    select.innerHTML = '';
    symbols.forEach((sym, idx) => {
      const opt = document.createElement('option');
      opt.value = sym;
      opt.textContent = sym;
      if (selected.includes(sym)) {
        opt.selected = true;
      } else if (!selected.length && idx < 3) {
        opt.selected = true;
      }
      select.appendChild(opt);
    });
    if (!symbols.length) setStatus('No symbols in database. Fetch data first.', true);
    renderPortfolioList(); // refresh symbol dropdowns in portfolio editor
  } catch (err) {
    console.error(err);
    setStatus('Failed to load symbols', true);
  }
}

function getSelectedSymbols() {
  const select = document.getElementById('symbols');
  return Array.from(select.selectedOptions).map((o) => o.value);
}

function buildChart(ctx, labels, datasets) {
  return new Chart(ctx, {
    type: 'line',
    data: { labels, datasets },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: { mode: 'nearest', intersect: false, position: 'nearest' },
      },
      interaction: { mode: 'index', intersect: false },
      scales: {
        x: { ticks: { color: '#cbd5e1' }, grid: { color: 'rgba(255,255,255,0.05)' } },
        y: { ticks: { color: '#cbd5e1' }, grid: { color: 'rgba(255,255,255,0.05)' } },
      },
      elements: {
        point: { radius: 0, hitRadius: 10, hoverRadius: 4, hoverBorderWidth: 2 },
      },
    },
  });
}

async function fetchPrices() {
  const symbols = getSelectedSymbols();
  if (!symbols.length) {
    setStatus('Select at least one symbol', true);
    return;
  }
  const start = document.getElementById('start').value;
  const end = document.getElementById('end').value;
  const normalize = document.getElementById('normalize').checked;
  setStatus('Loading...');
  try {
    const params = new URLSearchParams({ symbols: symbols.join(','), start, end });
    const res = await fetch(`/api/prices?${params.toString()}`);
    if (!res.ok) throw new Error(await res.text());
    const payload = await res.json();
    const data = payload.data || {};
    const allDates = new Set();
    Object.values(data).forEach((rows) => rows.forEach((r) => allDates.add(r.date)));
    const labels = Array.from(allDates).sort();
    const datasets = Object.entries(data).map(([sym, rows], idx) => {
      const sortedRows = [...rows].sort((a, b) => (a.date < b.date ? -1 : 1));
      const baseRow = sortedRows.find((r) => r.close != null);
      const base = baseRow?.close;
      const baseDate = baseRow?.date;
      const lastRow = [...sortedRows].reverse().find((r) => r.close != null);
      const lastVal = lastRow?.close ?? null;
      const lastDate = lastRow?.date ?? null;
      const map = new Map(sortedRows.map((r) => [r.date, r.close]));
      return {
        label: sym,
        data: labels.map((d) => {
          const val = map.get(d);
          if (val == null) return null;
          if (!normalize || base == null) return val;
          return Number(((val / base) * 100).toFixed(2));
        }),
        borderColor: palette[idx % palette.length],
        backgroundColor: hexToRgba(palette[idx % palette.length], 0.1),
        borderWidth: 2,
        tension: 0.2,
        spanGaps: true,
        pointRadius: 0,
        meta: {
          sym,
          color: palette[idx % palette.length],
          lastVal,
          base,
          startDate: baseDate,
          endDate: lastDate,
        },
      };
    });
    const ctx = document.getElementById('chart').getContext('2d');
    if (priceChart) priceChart.destroy();
    priceChart = buildChart(ctx, labels, datasets);
    lastSeriesMeta = datasets.map((d) => d.meta);
    renderSeriesPanel(normalize);
    persistPriceState({ symbols, start, end, normalize });
    setStatus(
      `Showing ${symbols.join(', ')} from ${start} to ${end}` +
        (normalize ? ' (normalized to first price = 100)' : '')
    );
  } catch (err) {
    console.error(err);
    setStatus('Failed to load prices', true);
  }
}

function renderSeriesPanel(normalize) {
  const container = document.getElementById('series-list');
  if (!lastSeriesMeta.length) {
    container.textContent = 'No data loaded';
    return;
  }
  container.innerHTML = '';
  const sorted = [...lastSeriesMeta].sort((a, b) => {
    if (a.base != null && a.lastVal != null && b.base != null && b.lastVal != null) {
      const ga = a.lastVal / a.base;
      const gb = b.lastVal / b.base;
      return gb - ga; // descending by multiple
    }
    if (a.lastVal != null && b.lastVal == null) return -1;
    if (a.lastVal == null && b.lastVal != null) return 1;
    return 0;
  });

  sorted.forEach((s) => {
    const div = document.createElement('div');
    div.className = 'series-item';
    div.addEventListener('mouseenter', () => highlightSeries(s.sym));
    div.addEventListener('mouseleave', () => clearHighlight());
    const dot = document.createElement('div');
    dot.className = 'series-dot';
    dot.style.background = s.color;
    const text = document.createElement('div');
    const last = s.lastVal != null ? s.lastVal.toFixed(2) : '—';
    const base = s.base != null ? s.base.toFixed(2) : '—';
    const growth =
      s.base != null && s.lastVal != null ? (s.lastVal / s.base).toFixed(2) + 'x' : '—';
    const cagr = computeCagrText(s.base, s.lastVal, s.startDate, s.endDate);
    const growthText = cagr ? `growth ${growth} · annual ${cagr}` : `growth ${growth}`;
    text.innerHTML = `<strong>${s.sym}</strong><br/><span class="muted">first ${base} · last ${last} · ${growthText}</span>`;
    div.appendChild(dot);
    div.appendChild(text);
    container.appendChild(div);
  });
}

function hexToRgba(hex, alpha) {
  const h = hex.replace('#', '');
  const bigint = parseInt(h, 16);
  const r = (bigint >> 16) & 255;
  const g = (bigint >> 8) & 255;
  const b = bigint & 255;
  return `rgba(${r}, ${g}, ${b}, ${alpha})`;
}

function highlightSeries(sym) {
  if (!priceChart) return;
  priceChart.data.datasets.forEach((ds) => {
    const base = ds.meta?.color || ds.borderColor;
    if (ds.meta?.sym === sym) {
      ds.borderColor = base;
      ds.borderWidth = 3;
      ds.backgroundColor = hexToRgba(base, 0.25);
    } else {
      ds.borderColor = hexToRgba(base, 0.15);
      ds.borderWidth = 1;
      ds.backgroundColor = hexToRgba(base, 0.05);
    }
  });
  priceChart.update('none');
}

function clearHighlight() {
  if (!priceChart) return;
  priceChart.data.datasets.forEach((ds) => {
    const base = ds.meta?.color || ds.borderColor;
    ds.borderColor = base;
    ds.borderWidth = 2;
    ds.backgroundColor = hexToRgba(base, 0.1);
  });
  priceChart.update('none');
}

function loadPriceState() {
  try {
    const raw = localStorage.getItem(PRICE_STATE_KEY);
    if (!raw) return null;
    return JSON.parse(raw);
  } catch (err) {
    console.warn('Failed to read saved state', err);
    return null;
  }
}

function persistPriceState(state) {
  try {
    localStorage.setItem(PRICE_STATE_KEY, JSON.stringify(state));
  } catch (err) {
    console.warn('Failed to save state', err);
  }
}

// -------- Portfolio logic --------

function loadPortfolioData() {
  try {
    const raw = localStorage.getItem(PORTFOLIO_DATA_KEY);
    if (!raw) return [];
    const parsed = JSON.parse(raw);
    if (!Array.isArray(parsed)) return [];
    return parsed;
  } catch (err) {
    console.warn('Failed to load portfolios', err);
    return [];
  }
}

function persistPortfolioData() {
  try {
    localStorage.setItem(PORTFOLIO_DATA_KEY, JSON.stringify(portfolios));
  } catch (err) {
    console.warn('Failed to save portfolios', err);
  }
}

function loadPortfolioUIState() {
  try {
    const raw = localStorage.getItem(PORTFOLIO_UI_KEY);
    if (!raw) return null;
    return JSON.parse(raw);
  } catch (err) {
    console.warn('Failed to read portfolio UI state', err);
    return null;
  }
}

function persistPortfolioUIState(state) {
  try {
    localStorage.setItem(PORTFOLIO_UI_KEY, JSON.stringify(state));
  } catch (err) {
    console.warn('Failed to save portfolio UI state', err);
  }
}

function ensureDefaultPortfolio() {
  if (portfolios.length) return;
  const fallbackSymbols = availableSymbols.length ? availableSymbols.slice(0, 2) : ['AAPL', 'MSFT'];
  portfolios.push({
    id: `p-${Date.now()}`,
    name: 'Sample 60/40',
    allocations: [
      { sym: fallbackSymbols[0] || 'AAPL', pct: 60 },
      { sym: fallbackSymbols[1] || 'MSFT', pct: 40 },
    ],
    expanded: false,
  });
}

function expandOnly(id) {
  portfolios.forEach((p) => {
    p.expanded = p.id === id;
  });
  persistPortfolioData();
}

function renderPortfolioList() {
  const container = document.getElementById('portfolio-list');
  container.innerHTML = '';
  ensureDefaultPortfolio();
  portfolios.forEach((pf) => {
    const card = document.createElement('div');
    card.className = 'portfolio-card';
    card.dataset.id = pf.id;
    card.classList.toggle('expanded', pf.expanded);

    const header = document.createElement('div');
    header.className = 'portfolio-card-header';
    const nameInput = document.createElement('input');
    nameInput.type = 'text';
    nameInput.value = pf.name || '';
    nameInput.placeholder = 'Portfolio name';
    nameInput.addEventListener('input', () => {
      pf.name = nameInput.value;
      persistPortfolioData();
      renderPortfolioSelect();
    });
    const actions = document.createElement('div');
    actions.className = 'portfolio-actions';
    const toggleBtn = document.createElement('button');
    toggleBtn.textContent = pf.expanded ? 'Done' : 'Edit';
    toggleBtn.className = 'ghost';
    toggleBtn.addEventListener('click', () => {
      if (pf.expanded) {
        pf.expanded = false;
      } else {
        expandOnly(pf.id);
      }
      persistPortfolioData();
      renderPortfolioList();
    });
    const deleteBtn = document.createElement('button');
    deleteBtn.textContent = 'Delete';
    deleteBtn.className = 'ghost danger';
    deleteBtn.addEventListener('click', () => {
      portfolios = portfolios.filter((p) => p.id !== pf.id);
      persistPortfolioData();
      renderPortfolioList();
      renderPortfolioSelect();
    });
    actions.appendChild(toggleBtn);
    actions.appendChild(deleteBtn);
    header.appendChild(nameInput);
    header.appendChild(actions);

    const allocList = document.createElement('div');
    allocList.className = 'alloc-list';

    (pf.allocations || []).forEach((alloc, idx) => {
      const row = document.createElement('div');
      row.className = 'alloc-row';
      const symSelect = document.createElement('select');
      availableSymbols.forEach((sym) => {
        const opt = document.createElement('option');
        opt.value = sym;
        opt.textContent = sym;
        if (sym === alloc.sym) opt.selected = true;
        symSelect.appendChild(opt);
      });
      symSelect.value = alloc.sym;
      symSelect.addEventListener('change', () => {
        alloc.sym = symSelect.value;
        persistPortfolioData();
        renderPortfolioSelect();
      });

      const pctInput = document.createElement('input');
      pctInput.type = 'number';
      pctInput.min = '0';
      pctInput.max = '100';
      pctInput.step = '1';
      pctInput.value = alloc.pct;
      pctInput.addEventListener('input', () => {
        alloc.pct = Number(pctInput.value);
        persistPortfolioData();
      });

      const removeBtn = document.createElement('button');
      removeBtn.textContent = '×';
      removeBtn.className = 'ghost danger';
      removeBtn.addEventListener('click', () => {
        pf.allocations.splice(idx, 1);
        persistPortfolioData();
        renderPortfolioList();
        renderPortfolioSelect();
      });

      row.appendChild(symSelect);
      row.appendChild(pctInput);
      row.appendChild(removeBtn);
      allocList.appendChild(row);
    });

    const addAllocBtn = document.createElement('button');
    addAllocBtn.textContent = 'Add symbol';
    addAllocBtn.className = 'ghost add-symbol-btn';
    addAllocBtn.addEventListener('click', () => {
      const nextSym = availableSymbols[0] || 'AAPL';
      pf.allocations.push({ sym: nextSym, pct: 10 });
      persistPortfolioData();
      renderPortfolioList();
    });

    const summary = document.createElement('div');
    summary.className = 'pf-summary muted small';
    const total = (pf.allocations || []).reduce((sum, a) => sum + Number(a.pct || 0), 0);
    const topLine = (pf.allocations || [])
      .map((a) => `${a.sym} ${Number(a.pct || 0).toFixed(0)}%`)
      .slice(0, 3)
      .join(' • ');
    summary.textContent = `Total ${total.toFixed(0)}%${topLine ? ` • ${topLine}` : ''}`;

    card.appendChild(header);
    card.appendChild(summary);
    if (pf.expanded) {
      card.appendChild(allocList);
      card.appendChild(addAllocBtn);
    }
    container.appendChild(card);
  });
  renderPortfolioSelect();
}

function renderPortfolioSelect() {
  const select = document.getElementById('portfolio-select');
  if (!select) return;
  const prev = Array.from(select.selectedOptions).map((o) => o.value);
  select.innerHTML = '';
  portfolios.forEach((pf) => {
    const opt = document.createElement('option');
    opt.value = pf.id;
    opt.textContent = pf.name || 'Untitled';
    if (prev.includes(pf.id)) opt.selected = true;
    select.appendChild(opt);
  });
}

function getSelectedPortfolioIds() {
  const select = document.getElementById('portfolio-select');
  return Array.from(select.selectedOptions).map((o) => o.value);
}

function buildPriceMaps(data) {
  const maps = {};
  Object.entries(data).forEach(([sym, rows]) => {
    const sorted = [...rows].sort((a, b) => (a.date < b.date ? -1 : 1));
    maps[sym] = sorted;
  });
  return maps;
}

function forwardFilledRatios(rows, labels) {
  if (!rows.length) return { ratios: labels.map(() => null), base: null };
  const base = rows.find((r) => r.close != null)?.close ?? null;
  if (base == null) return { ratios: labels.map(() => null), base: null };
  const map = new Map(rows.map((r) => [r.date, r.close]));
  let last = null;
  const ratios = labels.map((d) => {
    const val = map.get(d);
    if (val != null) last = val;
    if (last == null) return null;
    return last / base;
  });
  return { ratios, base };
}

function aggregatePortfolioSeries(pf, priceMaps, labels) {
  let weights = (pf.allocations || [])
    .map((a) => ({ sym: a.sym, weight: Number(a.pct) / 100 }))
    .filter((w) => w.weight > 0);
  const total = weights.reduce((sum, w) => sum + w.weight, 0);
  if (total > 0) {
    weights = weights.map((w) => ({ ...w, weight: w.weight / total })); // normalize to 1.0 if sum != 100%
  } else {
    return labels.map(() => null);
  }
  const series = labels.map(() => null);
  weights.forEach((w) => {
    const rows = priceMaps[w.sym] || [];
    const { ratios, base } = forwardFilledRatios(rows, labels);
    if (base == null) return;
    ratios.forEach((r, idx) => {
      if (r == null) return;
      series[idx] = (series[idx] ?? 0) + r * w.weight;
    });
  });
  return series;
}

function buildPortfolioDatasets(selectedPortfolios, priceData, labels, normalize) {
  const priceMaps = buildPriceMaps(priceData);
  return selectedPortfolios.map((pf, idx) => {
    const rawSeries = aggregatePortfolioSeries(pf, priceMaps, labels);
    const baseVal = rawSeries.find((v) => v != null) ?? null;
    const lastVal = [...rawSeries].reverse().find((v) => v != null) ?? null;
  const data = rawSeries.map((v) => {
    if (v == null) return null;
    if (!normalize || baseVal == null) return Number(v.toFixed(4));
    return Number(((v / baseVal) * 100).toFixed(2));
  });
    const startIdx = rawSeries.findIndex((v) => v != null);
    const endIdx = rawSeries.map((v, i) => ({ v, i })).reverse().find((x) => x.v != null)?.i ?? null;
    const startDate = startIdx >= 0 ? labels[startIdx] : null;
    const endDate = endIdx != null && endIdx >= 0 ? labels[endIdx] : null;
    return {
      label: pf.name || 'Portfolio',
      data,
      borderColor: palette[idx % palette.length],
      backgroundColor: hexToRgba(palette[idx % palette.length], 0.1),
      borderWidth: 2,
      tension: 0.2,
      spanGaps: true,
      pointRadius: 0,
      meta: {
        id: pf.id,
        name: pf.name || 'Portfolio',
        color: palette[idx % palette.length],
        base: baseVal,
        lastVal,
        startDate,
        endDate,
      },
    };
  });
}

async function fetchPortfolios() {
  const ids = getSelectedPortfolioIds();
  if (!ids.length) {
    setPortfolioStatus('Select at least one portfolio', true);
    return;
  }
  const start = document.getElementById('pf-start').value;
  const end = document.getElementById('pf-end').value;
  const normalize = document.getElementById('pf-normalize').checked;
  const selected = portfolios.filter((p) => ids.includes(p.id));
  const symbolsNeeded = new Set();
  selected.forEach((pf) => (pf.allocations || []).forEach((a) => symbolsNeeded.add(a.sym)));
  if (!symbolsNeeded.size) {
    setPortfolioStatus('No symbols in selected portfolios', true);
    return;
  }
  setPortfolioStatus('Loading...');
  try {
    const params = new URLSearchParams({
      symbols: Array.from(symbolsNeeded).join(','),
      start,
      end,
    });
    const res = await fetch(`/api/prices?${params.toString()}`);
    if (!res.ok) throw new Error(await res.text());
    const payload = await res.json();
    const data = payload.data || {};
    const allDates = new Set();
    Object.values(data).forEach((rows) => rows.forEach((r) => allDates.add(r.date)));
    const labels = Array.from(allDates).sort();
    const datasets = buildPortfolioDatasets(selected, data, labels, normalize);
    const ctx = document.getElementById('pf-chart').getContext('2d');
    if (portfolioChart) portfolioChart.destroy();
    portfolioChart = buildChart(ctx, labels, datasets);
    lastPortfolioMeta = datasets.map((d) => d.meta);
    renderPortfolioPanel();
    persistPortfolioUIState({ selected: ids, start, end, normalize });
    setPortfolioStatus(
      `Showing ${selected.length} portfolio(s) from ${start} to ${end}` +
        (normalize ? ' (normalized to index 100)' : '')
    );
  } catch (err) {
    console.error(err);
    setPortfolioStatus('Failed to load portfolios', true);
  }
}

function renderPortfolioPanel() {
  const container = document.getElementById('pf-series-list');
  if (!lastPortfolioMeta.length) {
    container.textContent = 'No data loaded';
    return;
  }
  container.innerHTML = '';
  const sorted = [...lastPortfolioMeta].sort((a, b) => {
    if (a.base != null && a.lastVal != null && b.base != null && b.lastVal != null) {
      const ga = a.lastVal / a.base;
      const gb = b.lastVal / b.base;
      return gb - ga;
    }
    if (a.lastVal != null && b.lastVal == null) return -1;
    if (a.lastVal == null && b.lastVal != null) return 1;
    return 0;
  });
  sorted.forEach((s) => {
    const div = document.createElement('div');
    div.className = 'series-item';
    div.addEventListener('mouseenter', () => highlightPortfolio(s.id));
    div.addEventListener('mouseleave', () => clearPortfolioHighlight());
    const dot = document.createElement('div');
    dot.className = 'series-dot';
    dot.style.background = s.color;
    const last = s.lastVal != null ? s.lastVal.toFixed(2) : '—';
    const base = s.base != null ? s.base.toFixed(2) : '—';
    const growth =
      s.base != null && s.lastVal != null ? (s.lastVal / s.base).toFixed(2) + 'x' : '—';
    const cagr = computeCagrText(s.base, s.lastVal, s.startDate, s.endDate);
    const growthText = cagr ? `growth ${growth} · annual ${cagr}` : `growth ${growth}`;
    const text = document.createElement('div');
    text.innerHTML = `<strong>${s.name}</strong><br/><span class="muted">first ${base} · last ${last} · ${growthText}</span>`;
    div.appendChild(dot);
    div.appendChild(text);
    container.appendChild(div);
  });
}

function highlightPortfolio(id) {
  if (!portfolioChart) return;
  portfolioChart.data.datasets.forEach((ds) => {
    const base = ds.meta?.color || ds.borderColor;
    if (ds.meta?.id === id) {
      ds.borderColor = base;
      ds.borderWidth = 3;
      ds.backgroundColor = hexToRgba(base, 0.25);
    } else {
      ds.borderColor = hexToRgba(base, 0.15);
      ds.borderWidth = 1;
      ds.backgroundColor = hexToRgba(base, 0.05);
    }
  });
  portfolioChart.update('none');
}

function clearPortfolioHighlight() {
  if (!portfolioChart) return;
  portfolioChart.data.datasets.forEach((ds) => {
    const base = ds.meta?.color || ds.borderColor;
    ds.borderColor = base;
    ds.borderWidth = 2;
    ds.backgroundColor = hexToRgba(base, 0.1);
  });
  portfolioChart.update('none');
}

function computeCagrText(base, last, startDate, endDate) {
  if (base == null || last == null || !startDate || !endDate) return '';
  const start = new Date(startDate);
  const end = new Date(endDate);
  const msPerYear = 365.25 * 24 * 60 * 60 * 1000;
  const years = (end - start) / msPerYear;
  if (years <= 0) return '';
  const cagr = Math.pow(last / base, 1 / years) - 1;
  if (!Number.isFinite(cagr)) return '';
  return `${(cagr * 100).toFixed(2)}%/yr`;
}

// -------- Tabs --------

function setActiveTab(tabId) {
  document.querySelectorAll('.tab-btn').forEach((btn) => {
    btn.classList.toggle('active', btn.dataset.target === tabId);
  });
  document.querySelectorAll('.tab-panel').forEach((panel) => {
    panel.classList.toggle('active', panel.id === tabId);
  });
  try {
    localStorage.setItem(ACTIVE_TAB_KEY, tabId);
  } catch (err) {
    console.warn('Failed to save active tab', err);
  }
}

function loadActiveTab() {
  try {
    return localStorage.getItem(ACTIVE_TAB_KEY);
  } catch (err) {
    return null;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  // price tab state
  const saved = loadPriceState();
  if (saved?.start) document.getElementById('start').value = saved.start;
  if (saved?.end) document.getElementById('end').value = saved.end;
  if (typeof saved?.normalize === 'boolean') {
    document.getElementById('normalize').checked = saved.normalize;
  }
  defaultDates('start', 'end');

  // portfolio state
  const savedUI = loadPortfolioUIState();
  if (savedUI?.start) document.getElementById('pf-start').value = savedUI.start;
  if (savedUI?.end) document.getElementById('pf-end').value = savedUI.end;
  if (typeof savedUI?.normalize === 'boolean') {
    document.getElementById('pf-normalize').checked = savedUI.normalize;
  }
  defaultDates('pf-start', 'pf-end');

  portfolios = loadPortfolioData();
  ensureDefaultPortfolio();
  renderPortfolioList();

  loadSymbols(saved?.symbols || []);

  const persistPriceControls = () => {
    persistPriceState({
      symbols: getSelectedSymbols(),
      start: document.getElementById('start').value,
      end: document.getElementById('end').value,
      normalize: document.getElementById('normalize').checked,
    });
  };

  document.getElementById('start').addEventListener('change', persistPriceControls);
  document.getElementById('end').addEventListener('change', persistPriceControls);
  document.getElementById('normalize').addEventListener('change', persistPriceControls);
  document.getElementById('symbols').addEventListener('change', persistPriceControls);
  document.getElementById('refresh').addEventListener('click', (e) => {
    e.preventDefault();
    fetchPrices();
  });

  document.getElementById('add-portfolio').addEventListener('click', () => {
    portfolios.forEach((p) => (p.expanded = false));
    portfolios.push({
      id: `p-${Date.now()}`,
      name: 'New portfolio',
      allocations: availableSymbols.slice(0, 2).map((sym) => ({ sym, pct: 50 })),
      expanded: true,
    });
    persistPortfolioData();
    renderPortfolioList();
  });

  const persistPortfolioControls = () => {
    persistPortfolioUIState({
      selected: getSelectedPortfolioIds(),
      start: document.getElementById('pf-start').value,
      end: document.getElementById('pf-end').value,
      normalize: document.getElementById('pf-normalize').checked,
    });
  };
  document.getElementById('pf-start').addEventListener('change', persistPortfolioControls);
  document.getElementById('pf-end').addEventListener('change', persistPortfolioControls);
  document.getElementById('pf-normalize').addEventListener('change', persistPortfolioControls);
  document.getElementById('portfolio-select').addEventListener('change', persistPortfolioControls);
  document.getElementById('pf-refresh').addEventListener('click', (e) => {
    e.preventDefault();
    fetchPortfolios();
  });

  // tabs
  document.querySelectorAll('.tab-btn').forEach((btn) => {
    btn.addEventListener('click', () => setActiveTab(btn.dataset.target));
  });
  const startTab = loadActiveTab() || 'prices-tab';
  setActiveTab(startTab);
});
