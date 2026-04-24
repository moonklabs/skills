// theme-toggle.js — lightweight light/dark switcher
// Reads + writes localStorage('sprintable-theme'). Renders a pill toggle in the top-right.
(function () {
  const KEY = 'sprintable-theme';
  const root = document.documentElement;
  const saved = localStorage.getItem(KEY) || 'dark';
  root.setAttribute('data-theme', saved);

  function mount() {
    if (document.getElementById('sprintable-theme-toggle')) return;
    const wrap = document.createElement('div');
    wrap.id = 'sprintable-theme-toggle';
    wrap.style.cssText = [
      'position:fixed','top:12px','right:12px','z-index:9999',
      'display:inline-flex','gap:2px','padding:2px',
      'background:var(--surface-alpha-2)',
      'border:1px solid var(--border-default)',
      'border-radius:9999px',
      'font-family:var(--font-sans)','font-feature-settings:"cv01","ss03"',
      'backdrop-filter:blur(8px)',
      'box-shadow:0 0 0 1px var(--shadow-ring-alpha)',
    ].join(';');

    const mkBtn = (theme, label, svg) => {
      const b = document.createElement('button');
      b.type = 'button';
      b.dataset.theme = theme;
      b.innerHTML = svg + '<span style="margin-left:5px">' + label + '</span>';
      b.style.cssText = [
        'all:unset','cursor:pointer','display:inline-flex','align-items:center',
        'padding:4px 10px','border-radius:9999px',
        'font-size:11px','font-weight:510','letter-spacing:-0.1px',
        'color:var(--fg-3)','transition:background 120ms,color 120ms',
      ].join(';');
      b.onclick = () => apply(theme);
      return b;
    };
    const sun  = '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>';
    const moon = '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
    wrap.appendChild(mkBtn('light', 'Light', sun));
    wrap.appendChild(mkBtn('dark',  'Dark',  moon));
    document.body.appendChild(wrap);
    paint();
  }

  function paint() {
    const theme = root.getAttribute('data-theme') || 'dark';
    document.querySelectorAll('#sprintable-theme-toggle button').forEach((b) => {
      const active = b.dataset.theme === theme;
      b.style.background = active ? 'var(--bg-surface)' : 'transparent';
      b.style.color = active ? 'var(--fg-1)' : 'var(--fg-3)';
      b.style.boxShadow = active ? '0 0 0 1px var(--border-default)' : 'none';
    });
  }

  function apply(theme) {
    root.setAttribute('data-theme', theme);
    localStorage.setItem(KEY, theme);
    paint();
    window.dispatchEvent(new CustomEvent('sprintable-theme-change', { detail: theme }));
  }

  window.sprintableTheme = { get: () => root.getAttribute('data-theme'), set: apply };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mount);
  } else {
    mount();
  }
})();
