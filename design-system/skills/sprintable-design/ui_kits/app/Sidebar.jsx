// Sidebar.jsx
function Sidebar() {
  const [active, setActive] = React.useState('active');
  const NavItem = ({ id, icon, label, count, section = false }) => {
    const isActive = active === id;
    return (
      <div onClick={() => setActive(id)} style={{
        display: 'flex', alignItems: 'center', gap: 8,
        padding: '4px 8px', margin: '1px 6px', borderRadius: 5,
        cursor: 'pointer', userSelect: 'none',
        background: isActive ? 'var(--surface-alpha-3)' : 'transparent',
        color: isActive ? 'var(--fg-1)' : 'var(--fg-2)',
        fontSize: 13, fontWeight: 510,
        transition: 'background 120ms, color 120ms',
      }}
      onMouseEnter={(e) => !isActive && (e.currentTarget.style.background = 'var(--surface-alpha-2)')}
      onMouseLeave={(e) => !isActive && (e.currentTarget.style.background = 'transparent')}>
        <i data-lucide={icon} style={{ width: 14, height: 14, strokeWidth: 1.6, color: isActive ? 'var(--brand-light)' : 'var(--fg-3)' }}/>
        <span style={{ flex: 1 }}>{label}</span>
        {count != null && <span style={{ fontSize: 11, color: 'var(--fg-4)', fontFamily: 'var(--font-mono)' }}>{count}</span>}
      </div>
    );
  };
  const SectionHeader = ({ children }) => (
    <div style={{
      padding: '14px 14px 4px',
      fontFamily: 'var(--font-mono)', fontSize: 10, color: 'var(--fg-4)',
      textTransform: 'uppercase', letterSpacing: 0.4,
    }}>{children}</div>
  );
  return (
    <aside style={{
      width: 228, background: 'var(--bg-panel)',
      borderRight: '1px solid var(--border-subtle)',
      display: 'flex', flexDirection: 'column',
      height: '100vh', flexShrink: 0,
    }}>
      <div style={{
        padding: '12px 14px', display: 'flex', alignItems: 'center', gap: 8,
        borderBottom: '1px solid var(--border-subtle)',
      }}>
        <img src="../../assets/sprintable-logo-square.png" style={{ width: 20, height: 20 }}/>
        <span style={{ color: 'var(--fg-1)', fontSize: 13, fontWeight: 590, letterSpacing: -0.2, flex: 1 }}>Platform</span>
        <i data-lucide="chevron-down" style={{ width: 14, height: 14, color: 'var(--fg-4)' }}/>
      </div>
      <div style={{
        margin: '10px 10px 2px', padding: '5px 10px',
        background: 'var(--surface-alpha-1)', border: '1px solid var(--border-default)',
        borderRadius: 6, display: 'flex', alignItems: 'center', gap: 8,
        color: 'var(--fg-3)', fontSize: 12,
      }}>
        <i data-lucide="search" style={{ width: 12, height: 12 }}/>
        <span style={{ flex: 1 }}>Search…</span>
        <span style={{ fontFamily: 'var(--font-mono)', fontSize: 10, color: 'var(--fg-4)' }}>⌘K</span>
      </div>
      <div style={{ flex: 1, overflowY: 'auto', paddingBottom: 14 }}>
        <div style={{ paddingTop: 8 }}>
          <NavItem id="inbox" icon="inbox" label="Inbox" count={3}/>
          <NavItem id="mine" icon="user" label="My issues" count={7}/>
        </div>
        <SectionHeader>Your work</SectionHeader>
        <NavItem id="active" icon="zap" label="Active sprint" count={12}/>
        <NavItem id="backlog" icon="layers" label="Backlog" count={38}/>
        <NavItem id="triage" icon="alert-circle" label="Triage" count={2}/>
        <NavItem id="docs" icon="file-text" label="Docs"/>
        <SectionHeader>Teams</SectionHeader>
        <NavItem id="platform" icon="hash" label="Platform"/>
        <NavItem id="growth" icon="hash" label="Growth"/>
        <NavItem id="design" icon="hash" label="Design"/>
      </div>
      <div style={{
        borderTop: '1px solid var(--border-subtle)', padding: 10,
        display: 'flex', alignItems: 'center', gap: 8,
      }}>
        <div style={{ width: 22, height: 22, borderRadius: 11, background: 'linear-gradient(135deg,#3385f8,#0059a5)' }}/>
        <span style={{ color: 'var(--fg-2)', fontSize: 12, fontWeight: 510, flex: 1 }}>aria@sprintable</span>
        <i data-lucide="settings" style={{ width: 13, height: 13, color: 'var(--fg-3)' }}/>
      </div>
    </aside>
  );
}
window.Sidebar = Sidebar;
