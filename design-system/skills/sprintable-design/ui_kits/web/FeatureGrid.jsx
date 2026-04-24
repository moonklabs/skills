// FeatureGrid.jsx
function FeatureGrid() {
  const features = [
    { icon: 'zap', title: 'Cycles, not boards', body: 'A sprint has a start, a scope, and an end. We optimise for shipping it, not for columns.' },
    { icon: 'git-branch', title: 'Linked to the code', body: 'Every issue knows its branch, its PR, its deploy. The status bar tells you the truth.' },
    { icon: 'terminal', title: 'Keyboard-first', body: 'Every action has a shortcut. The command palette is the default UI.' },
    { icon: 'radio', title: 'Real-time, actually', body: 'Your cursor is on the issue. Theirs is too. Nothing to refresh.' },
    { icon: 'filter', title: 'Views, saved', body: 'Filter once, save it, pin it. The view is the query is the URL.' },
    { icon: 'lock', title: 'Security that shuts up', body: 'SOC 2, SSO, SCIM. Set once, auditable forever, out of the way.' },
  ];
  return (
    <section style={{ padding: '80px 32px', maxWidth: 1200, margin: '0 auto' }}>
      <div style={{ maxWidth: 720, marginBottom: 56 }}>
        <div style={{ fontFamily: 'var(--font-mono)', fontSize: 11, color: 'var(--brand-light)', fontWeight: 510, textTransform: 'uppercase', letterSpacing: 0.4, marginBottom: 12 }}>FEATURES</div>
        <h2 style={{ fontSize: 48, fontWeight: 510, lineHeight: 1, letterSpacing: '-1.056px', color: 'var(--fg-1)', margin: 0 }}>
          Built for the people shipping.
        </h2>
      </div>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 16 }}>
        {features.map((f) => (
          <div key={f.title} style={{
            background: 'var(--surface-alpha-2)', border: '1px solid var(--border-default)',
            borderRadius: 12, padding: 24, display: 'flex', flexDirection: 'column', gap: 10, minHeight: 200,
          }}>
            <div style={{
              width: 32, height: 32, borderRadius: 8,
              background: 'var(--surface-alpha-3)', border: '1px solid var(--border-subtle)',
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              color: 'var(--brand-light)',
            }}>
              <i data-lucide={f.icon} style={{ width: 16, height: 16 }} />
            </div>
            <div style={{ fontSize: 20, fontWeight: 590, letterSpacing: '-0.24px', color: 'var(--fg-1)', marginTop: 6 }}>{f.title}</div>
            <div style={{ fontSize: 15, lineHeight: 1.6, color: 'var(--fg-3)', letterSpacing: '-0.165px' }}>{f.body}</div>
          </div>
        ))}
      </div>
    </section>
  );
}
window.FeatureGrid = FeatureGrid;
