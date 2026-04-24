// TopBar.jsx
function TopBar({ onOpenPalette }) {
  const Chip = ({ children, onClick }) => (
    <button onClick={onClick} style={{
      background: 'transparent', color: 'var(--fg-2)',
      border: '1px solid var(--border-solid-1)', borderRadius: 9999,
      padding: '3px 10px', fontSize: 12, fontWeight: 510,
      cursor: 'pointer', fontFamily: 'inherit',
      display: 'inline-flex', alignItems: 'center', gap: 5,
    }}>{children}</button>
  );
  return (
    <header style={{
      height: 52, padding: '0 16px',
      borderBottom: '1px solid var(--border-subtle)',
      display: 'flex', alignItems: 'center', gap: 12,
      background: 'var(--bg-marketing)',
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 8, fontSize: 13 }}>
        <i data-lucide="zap" style={{ width: 14, height: 14, color: 'var(--brand-light)' }}/>
        <span style={{ color: 'var(--fg-1)', fontWeight: 510 }}>Active sprint</span>
        <span style={{ color: 'var(--fg-4)' }}>·</span>
        <span style={{ color: 'var(--fg-3)', fontFamily: 'var(--font-mono)', fontSize: 12 }}>wk-42</span>
      </div>
      <div style={{ marginLeft: 'auto', display: 'flex', gap: 6 }}>
        <Chip>
          <i data-lucide="filter" style={{ width: 11, height: 11 }}/>
          Filter
        </Chip>
        <Chip>
          <i data-lucide="arrow-up-down" style={{ width: 11, height: 11 }}/>
          Priority
        </Chip>
        <Chip>Display</Chip>
        <button style={{
          background: 'var(--surface-alpha-2)', color: 'var(--fg-1)',
          border: '1px solid var(--border-default)', borderRadius: 6,
          padding: '5px 10px', fontSize: 12, fontWeight: 510,
          cursor: 'pointer', fontFamily: 'inherit',
          display: 'inline-flex', alignItems: 'center', gap: 6,
        }} onClick={onOpenPalette}>
          <i data-lucide="plus" style={{ width: 12, height: 12 }}/>
          New issue
        </button>
      </div>
    </header>
  );
}
window.TopBar = TopBar;
