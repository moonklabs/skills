// CommandPalette.jsx
function CommandPalette({ open, onClose }) {
  if (!open) return null;
  const groups = [
    { label: 'Actions', items: [
      { icon: 'plus', title: 'New issue', kbd: 'C' },
      { icon: 'zap', title: 'Start sprint', kbd: 'S' },
      { icon: 'git-branch', title: 'Create branch from issue', kbd: 'B' },
    ]},
    { label: 'Navigate', items: [
      { icon: 'inbox', title: 'Go to inbox', kbd: 'G I' },
      { icon: 'user', title: 'Go to my issues', kbd: 'G M' },
      { icon: 'settings', title: 'Open settings', kbd: '⌘ ,' },
    ]},
  ];
  return (
    <div onClick={onClose} style={{
      position: 'fixed', inset: 0, zIndex: 100,
      background: 'rgba(0,0,0,0.85)',
      display: 'flex', alignItems: 'flex-start', justifyContent: 'center',
      paddingTop: '12vh',
    }}>
      <div onClick={(e) => e.stopPropagation()} style={{
        width: 560, background: 'var(--bg-surface)',
        border: '1px solid var(--border-default)', borderRadius: 12,
        boxShadow: 'rgba(0,0,0,0) 0px 8px 2px, rgba(0,0,0,0.01) 0px 5px 2px, rgba(0,0,0,0.04) 0px 3px 2px, rgba(0,0,0,0.07) 0px 1px 1px, rgba(0,0,0,0.2) 0px 0px 0px 1px',
        overflow: 'hidden',
      }}>
        <div style={{
          padding: '14px 16px', display: 'flex', alignItems: 'center', gap: 10,
          borderBottom: '1px solid var(--border-subtle)',
        }}>
          <i data-lucide="search" style={{ width: 14, height: 14, color: 'var(--fg-3)' }}/>
          <input autoFocus placeholder="Type a command or search…" style={{
            all: 'unset', flex: 1, color: 'var(--fg-1)', fontSize: 15,
            fontFamily: 'inherit', fontFeatureSettings: '"cv01","ss03"',
          }}/>
          <span style={{ fontFamily: 'var(--font-mono)', fontSize: 10, color: 'var(--fg-4)',
            background: 'var(--surface-alpha-3)', border: '1px solid var(--border-subtle)',
            borderRadius: 3, padding: '1px 6px' }}>ESC</span>
        </div>
        <div style={{ padding: 6, maxHeight: 380, overflowY: 'auto' }}>
          {groups.map((g) => (
            <div key={g.label}>
              <div style={{
                padding: '10px 10px 4px', fontFamily: 'var(--font-mono)',
                fontSize: 10, color: 'var(--fg-4)', textTransform: 'uppercase', letterSpacing: 0.4,
              }}>{g.label}</div>
              {g.items.map((i, idx) => (
                <div key={i.title} style={{
                  padding: '8px 10px', borderRadius: 6,
                  display: 'flex', alignItems: 'center', gap: 10,
                  background: (g.label === 'Actions' && idx === 0) ? 'var(--surface-alpha-3)' : 'transparent',
                  color: 'var(--fg-2)', fontSize: 13, fontWeight: 510, cursor: 'pointer',
                }}>
                  <i data-lucide={i.icon} style={{ width: 14, height: 14, color: 'var(--fg-3)' }}/>
                  <span style={{ flex: 1, color: 'var(--fg-1)' }}>{i.title}</span>
                  <span style={{ fontFamily: 'var(--font-mono)', fontSize: 10, color: 'var(--fg-4)' }}>{i.kbd}</span>
                </div>
              ))}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
window.CommandPalette = CommandPalette;
