// Footer.jsx
function Footer() {
  const cols = [
    ['Product', ['Features', 'Pricing', 'Changelog', 'Integrations', 'API']],
    ['Company', ['About', 'Customers', 'Blog', 'Careers', 'Contact']],
    ['Resources', ['Docs', 'Changelog', 'Status', 'Brand']],
    ['Legal', ['Terms', 'Privacy', 'Security', 'DPA']],
  ];
  return (
    <footer style={{ padding: '80px 32px 48px', maxWidth: 1200, margin: '0 auto', borderTop: '1px solid var(--border-subtle)' }}>
      <div style={{ display: 'grid', gridTemplateColumns: '1.5fr repeat(4, 1fr)', gap: 32, marginBottom: 56 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 12 }}>
            <img src="../../assets/sprintable-logo-square.png" alt="" style={{ width: 22, height: 22 }} />
            <span style={{ color: 'var(--fg-1)', fontSize: 16, fontWeight: 590, letterSpacing: -0.3 }}>sprintable</span>
          </div>
          <p style={{ color: 'var(--fg-3)', fontSize: 13, letterSpacing: '-0.13px', lineHeight: 1.5, maxWidth: 260, margin: 0 }}>
            Plan, estimate, and ship — in one place.
          </p>
        </div>
        {cols.map(([h, items]) => (
          <div key={h}>
            <div style={{ fontFamily: 'var(--font-mono)', fontSize: 11, color: 'var(--fg-4)', textTransform: 'uppercase', letterSpacing: 0.4, marginBottom: 14 }}>{h}</div>
            {items.map((i) => (
              <a key={i} href="#" style={{ display: 'block', color: 'var(--fg-2)', fontSize: 13, padding: '5px 0', textDecoration: 'none' }}>{i}</a>
            ))}
          </div>
        ))}
      </div>
      <div style={{
        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
        paddingTop: 24, borderTop: '1px solid var(--border-subtle)',
        color: 'var(--fg-4)', fontSize: 12, fontFamily: 'var(--font-mono)',
      }}>
        <span>© 2026 Sprintable, Inc.</span>
        <span style={{ display: 'inline-flex', alignItems: 'center', gap: 6 }}>
          <span style={{ width: 6, height: 6, borderRadius: 3, background: '#27a644' }}/>
          All systems operational
        </span>
      </div>
    </footer>
  );
}
window.Footer = Footer;
