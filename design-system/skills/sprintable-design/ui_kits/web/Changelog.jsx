// Changelog.jsx — single-column timeline
function Changelog() {
  const entries = [
    { v: '3.0', date: 'Apr 18, 2026', title: 'Automated cycles', body: 'Sprints roll forward on their own. Unfinished work migrates, estimates carry over, stand-up summaries write themselves.' },
    { v: '2.9', date: 'Apr 02, 2026', title: 'Triage mode', body: 'Zero-inbox for bug reports. Keyboard-driven, multi-select, and it remembers where you left off.' },
    { v: '2.8', date: 'Mar 18, 2026', title: 'SOC 2 Type II', body: 'We finished the audit. Report available in Settings → Security.' },
  ];
  return (
    <section style={{ padding: '80px 32px', maxWidth: 820, margin: '0 auto' }}>
      <div style={{ marginBottom: 48 }}>
        <div style={{ fontFamily: 'var(--font-mono)', fontSize: 11, color: 'var(--brand-light)', fontWeight: 510, textTransform: 'uppercase', letterSpacing: 0.4, marginBottom: 12 }}>CHANGELOG</div>
        <h2 style={{ fontSize: 32, fontWeight: 400, letterSpacing: '-0.704px', color: 'var(--fg-1)', margin: 0 }}>Shipped recently</h2>
      </div>
      <div>
        {entries.map((e, i) => (
          <article key={e.v} style={{
            display: 'grid', gridTemplateColumns: '140px 1fr', gap: 32,
            padding: '32px 0', borderTop: '1px solid var(--border-subtle)',
            borderBottom: i === entries.length - 1 ? '1px solid var(--border-subtle)' : 'none',
          }}>
            <div>
              <div style={{
                display: 'inline-flex', alignItems: 'center', gap: 6,
                background: 'var(--surface-alpha-3)', border: '1px solid var(--border-subtle)',
                borderRadius: 2, padding: '1px 8px 1px 2px', marginBottom: 10,
              }}>
                <span style={{ background: 'var(--brand-primary)', color: 'var(--fg-inverse)', padding: '1px 6px', borderRadius: 2, fontSize: 10, fontWeight: 590, fontFamily: 'var(--font-mono)' }}>v{e.v}</span>
              </div>
              <div style={{ fontFamily: 'var(--font-mono)', fontSize: 11, color: 'var(--fg-4)' }}>{e.date}</div>
            </div>
            <div>
              <h3 style={{ fontSize: 20, fontWeight: 590, letterSpacing: '-0.24px', color: 'var(--fg-1)', margin: '0 0 10px' }}>{e.title}</h3>
              <p style={{ fontSize: 15, lineHeight: 1.6, color: 'var(--fg-2)', letterSpacing: '-0.165px', margin: 0 }}>{e.body}</p>
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}
window.Changelog = Changelog;
