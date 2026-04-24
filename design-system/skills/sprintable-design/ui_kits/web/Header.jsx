// Header.jsx — Sprintable marketing sticky header
function Header() {
  const [scrolled, setScrolled] = React.useState(false);
  React.useEffect(() => {
    const on = () => setScrolled(window.scrollY > 8);
    window.addEventListener('scroll', on); on();
    return () => window.removeEventListener('scroll', on);
  }, []);
  const linkStyle = {
    color: 'var(--fg-2)', fontSize: 13, fontWeight: 510, textDecoration: 'none',
    padding: '6px 10px', borderRadius: 6, transition: 'color 120ms, background 120ms',
  };
  const [hover, setHover] = React.useState(null);
  const Link = ({ k, children }) => (
    <a href="#" style={{
      ...linkStyle,
      color: hover === k ? 'var(--fg-1)' : 'var(--fg-2)',
      background: hover === k ? 'var(--surface-alpha-2)' : 'transparent',
    }} onMouseEnter={() => setHover(k)} onMouseLeave={() => setHover(null)}>{children}</a>
  );
  return (
    <header style={{
      position: 'sticky', top: 0, zIndex: 20,
      background: scrolled ? 'rgba(15,16,17,0.72)' : 'transparent',
      backdropFilter: scrolled ? 'blur(12px)' : 'none',
      borderBottom: scrolled ? '1px solid var(--border-subtle)' : '1px solid transparent',
      transition: 'all 180ms cubic-bezier(0.2,0,0,1)',
    }}>
      <div style={{
        maxWidth: 1200, margin: '0 auto', padding: '14px 32px',
        display: 'flex', alignItems: 'center', gap: 32,
      }}>
        <a href="#" style={{ display: 'flex', alignItems: 'center', gap: 8, textDecoration: 'none' }}>
          <img src="../../assets/sprintable-logo-square.png" alt="" style={{ width: 22, height: 22 }} />
          <span style={{ color: 'var(--fg-1)', fontSize: 16, fontWeight: 590, letterSpacing: -0.3 }}>sprintable</span>
        </a>
        <nav style={{ display: 'flex', gap: 4, marginLeft: 16 }}>
          <Link k="product">Product</Link>
          <Link k="pricing">Pricing</Link>
          <Link k="changelog">Changelog</Link>
          <Link k="docs">Docs</Link>
          <Link k="customers">Customers</Link>
        </nav>
        <div style={{ marginLeft: 'auto', display: 'flex', gap: 8, alignItems: 'center' }}>
          <Link k="signin">Sign in</Link>
          <button style={{
            background: 'var(--brand-primary)', color: 'var(--fg-inverse)', border: 'none',
            padding: '7px 14px', borderRadius: 6, fontSize: 13, fontWeight: 510,
            cursor: 'pointer', fontFamily: 'inherit',
            fontFeatureSettings: '"cv01","ss03"',
            transition: 'background 120ms',
          }}
            onMouseEnter={(e) => (e.currentTarget.style.background = 'var(--accent-hover)')}
            onMouseLeave={(e) => (e.currentTarget.style.background = 'var(--brand-primary)')}>
            Start free
          </button>
        </div>
      </div>
    </header>
  );
}
window.Header = Header;
