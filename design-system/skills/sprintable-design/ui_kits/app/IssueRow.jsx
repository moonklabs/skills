// IssueRow.jsx
function IssueRow({ id, title, status, statusColor, priority, assignee, date, selected }) {
  return (
    <div style={{
      display: 'grid',
      gridTemplateColumns: '16px 84px 1fr 90px 28px 56px 60px',
      alignItems: 'center', gap: 12,
      padding: '8px 16px',
      borderBottom: '1px solid var(--border-subtle)',
      background: selected ? 'var(--surface-alpha-2)' : 'transparent',
      fontSize: 13, cursor: 'pointer',
    }}>
      <span style={{
        width: 12, height: 12, borderRadius: 6,
        border: `1.5px solid ${statusColor}`, position: 'relative',
        background: status === 'Done' ? statusColor : 'transparent',
      }}>
        {status === 'In progress' && (
          <span style={{ position: 'absolute', inset: 2, borderRadius: 4, background: statusColor, clipPath: 'polygon(0 0, 50% 0, 50% 100%, 0 100%)' }}/>
        )}
      </span>
      <span style={{ fontFamily: 'var(--font-mono)', fontSize: 11, color: 'var(--fg-4)' }}>{id}</span>
      <span style={{ color: 'var(--fg-1)', fontWeight: 510, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{title}</span>
      <span style={{
        display: 'inline-flex', alignItems: 'center', gap: 6,
        border: '1px solid var(--border-solid-1)', borderRadius: 9999, padding: '1px 8px',
        fontSize: 11, color: 'var(--fg-2)', fontWeight: 510, width: 'fit-content',
      }}>
        <span style={{ width: 6, height: 6, borderRadius: 3, background: statusColor }}/>
        {status}
      </span>
      <span title={`Priority ${priority}`} style={{ display: 'inline-flex', gap: 2 }}>
        {[0, 1, 2].map(i => (
          <span key={i} style={{
            width: 3, height: 8 + i * 3, borderRadius: 1,
            background: i < priority ? 'var(--fg-2)' : 'var(--border-default)',
          }}/>
        ))}
      </span>
      <span style={{ fontSize: 11, color: 'var(--fg-3)', fontFamily: 'var(--font-mono)' }}>{assignee}</span>
      <span style={{ fontSize: 11, color: 'var(--fg-4)', fontFamily: 'var(--font-mono)', textAlign: 'right' }}>{date}</span>
    </div>
  );
}
window.IssueRow = IssueRow;
