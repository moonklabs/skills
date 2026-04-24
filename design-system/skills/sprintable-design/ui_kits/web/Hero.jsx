// Hero.jsx — marketing hero
function Hero() {
  return (
    <section style={{ padding: '80px 32px 100px', maxWidth: 1200, margin: '0 auto', textAlign: 'center' }}>
      <div style={{
        display: 'inline-flex', alignItems: 'center', gap: 8,
        border: '1px solid var(--border-default)', borderRadius: 9999,
        padding: '4px 12px 4px 4px', marginBottom: 28, background: 'var(--surface-alpha-2)',
      }}>
        <span style={{
          background: 'var(--brand-primary)', color: 'var(--fg-inverse)', fontSize: 10, fontWeight: 590,
          padding: '2px 8px', borderRadius: 9999, letterSpacing: 0.2,
        }}>NEW</span>
        <span style={{ fontSize: 12, color: 'var(--fg-2)', fontWeight: 510 }}>
          Sprintable 3.0 — automated cycles →
        </span>
      </div>
      <h1 style={{
        fontSize: 72, fontWeight: 510, lineHeight: 1.0, letterSpacing: '-1.584px',
        color: 'var(--fg-1)', margin: 0, maxWidth: 900, marginInline: 'auto',
      }}>
        Ship a sprint<br/>in an afternoon.
      </h1>
      <p style={{
        fontSize: 18, fontWeight: 400, lineHeight: 1.6, letterSpacing: '-0.165px',
        color: 'var(--fg-3)', maxWidth: 560, margin: '24px auto 36px',
      }}>
        Sprintable is where small teams plan, estimate, and ship — in one place.
        Built for engineers who want to stop managing the tracker.
      </p>
      <div style={{ display: 'flex', gap: 12, justifyContent: 'center' }}>
        <button style={{
          background: 'var(--brand-primary)', color: 'var(--fg-inverse)', border: 'none',
          padding: '10px 18px', borderRadius: 6, fontSize: 14, fontWeight: 510,
          cursor: 'pointer', fontFamily: 'inherit', fontFeatureSettings: '"cv01","ss03"',
        }}>Start building</button>
        <button style={{
          background: 'var(--surface-alpha-1)', color: '#e2e4e7',
          border: '1px solid var(--border-default)',
          padding: '10px 18px', borderRadius: 6, fontSize: 14, fontWeight: 510,
          cursor: 'pointer', fontFamily: 'inherit', fontFeatureSettings: '"cv01","ss03"',
        }}>Book a demo</button>
      </div>
      {/* Product screenshot placeholder */}
      <div style={{
        marginTop: 72, maxWidth: 1040, marginInline: 'auto',
        border: '1px solid var(--border-default)', borderRadius: 12,
        background: 'var(--bg-panel)', overflow: 'hidden',
        boxShadow: '0 2px 4px rgba(0,0,0,0.4), 0 0 0 1px rgba(0,0,0,0.2)',
      }}>
        <AppPreview />
      </div>
    </section>
  );
}

// A tiny inline app mockup for the hero image. Not a full UI; just a believable peek.
function AppPreview() {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '200px 1fr', height: 420, background: 'var(--bg-panel)' }}>
      <aside style={{ borderRight: '1px solid var(--border-subtle)', padding: '16px 10px', fontSize: 12, color: 'var(--fg-3)' }}>
        <div style={{ fontFamily: 'var(--font-mono)', fontSize: 10, color: 'var(--fg-4)', padding: '0 6px 10px', textTransform: 'uppercase', letterSpacing: 0.4 }}>workspace</div>
        {['Inbox', 'My issues', 'Active sprint', 'Backlog', 'Triage'].map((t, i) => (
          <div key={t} style={{
            padding: '5px 8px', borderRadius: 5, marginBottom: 1,
            background: i === 2 ? 'var(--surface-alpha-3)' : 'transparent',
            color: i === 2 ? 'var(--fg-1)' : 'var(--fg-2)',
            fontWeight: i === 2 ? 510 : 400,
          }}>{t}</div>
        ))}
        <div style={{ fontFamily: 'var(--font-mono)', fontSize: 10, color: 'var(--fg-4)', padding: '18px 6px 10px', textTransform: 'uppercase', letterSpacing: 0.4 }}>teams</div>
        {['Platform', 'Growth', 'Design'].map((t) => (
          <div key={t} style={{ padding: '5px 8px', color: 'var(--fg-2)', fontSize: 12 }}>{t}</div>
        ))}
      </aside>
      <main style={{ padding: 20, textAlign: 'left' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10, paddingBottom: 16, borderBottom: '1px solid var(--border-subtle)' }}>
          <span style={{ color: 'var(--fg-1)', fontSize: 14, fontWeight: 510 }}>Active sprint · wk-42</span>
          <span style={{
            border: '1px solid var(--border-solid-1)', borderRadius: 9999, padding: '2px 8px',
            fontSize: 11, color: 'var(--fg-2)', fontWeight: 510,
          }}>8 left</span>
        </div>
        {[
          ['PLT-428', 'Ship deploy preview API', '#27a644', 'In progress', 'aria'],
          ['PLT-431', 'Webhook retry cap bug', '#27a644', 'In progress', 'kenji'],
          ['PLT-433', 'Audit logs export', '#8a8f98', 'Backlog', 'jean'],
          ['PLT-435', 'Billing event firehose', '#10b981', 'Done', 'max'],
          ['PLT-440', 'Idle-connection killer', '#8a8f98', 'Backlog', 'aria'],
        ].map((row, i) => (
          <div key={i} style={{
            display: 'grid', gridTemplateColumns: '70px 1fr 110px 70px',
            gap: 12, alignItems: 'center', padding: '10px 4px',
            borderBottom: i < 4 ? '1px solid var(--border-subtle)' : 'none',
          }}>
            <span style={{ fontFamily: 'var(--font-mono)', fontSize: 11, color: 'var(--fg-4)' }}>{row[0]}</span>
            <span style={{ color: 'var(--fg-1)', fontSize: 13, fontWeight: 510 }}>{row[1]}</span>
            <span style={{ display: 'inline-flex', alignItems: 'center', gap: 6, fontSize: 12, color: 'var(--fg-2)' }}>
              <span style={{ width: 6, height: 6, borderRadius: 3, background: row[2] }}/>{row[3]}
            </span>
            <span style={{ fontSize: 11, color: 'var(--fg-3)', fontFamily: 'var(--font-mono)' }}>{row[4]}</span>
          </div>
        ))}
      </main>
    </div>
  );
}
window.Hero = Hero;
