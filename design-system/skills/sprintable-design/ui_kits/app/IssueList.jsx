// IssueList.jsx
function IssueList() {
  const groups = [
    { title: 'In progress', color: '#27a644', count: 3, items: [
      { id: 'PLT-428', title: 'Ship deploy preview API', status: 'In progress', statusColor: '#27a644', priority: 3, assignee: 'aria', date: 'Apr 22' },
      { id: 'PLT-431', title: 'Webhook retry cap bug — 5xx chain exceeds budget', status: 'In progress', statusColor: '#27a644', priority: 2, assignee: 'kenji', date: 'Apr 22' },
      { id: 'PLT-437', title: 'Split billing event firehose into typed streams', status: 'In progress', statusColor: '#27a644', priority: 2, assignee: 'max', date: 'Apr 23' },
    ]},
    { title: 'Todo', color: '#8a8f98', count: 4, items: [
      { id: 'PLT-433', title: 'Audit logs export — CSV + JSON schema', status: 'Todo', statusColor: '#8a8f98', priority: 1, assignee: 'jean', date: 'Apr 24' },
      { id: 'PLT-440', title: 'Idle-connection killer for long-poll gateway', status: 'Todo', statusColor: '#8a8f98', priority: 2, assignee: 'aria', date: 'Apr 25' },
      { id: 'PLT-442', title: 'SCIM provisioning: soft-delete on group removal', status: 'Todo', statusColor: '#8a8f98', priority: 1, assignee: 'kenji', date: 'Apr 26' },
      { id: 'PLT-446', title: 'Migrate internal metrics to OTLP', status: 'Todo', statusColor: '#8a8f98', priority: 0, assignee: 'max', date: 'Apr 28' },
    ]},
    { title: 'Done', color: '#10b981', count: 2, items: [
      { id: 'PLT-420', title: 'Retire legacy `/issues` v1 endpoint', status: 'Done', statusColor: '#10b981', priority: 2, assignee: 'jean', date: 'Apr 19' },
      { id: 'PLT-415', title: 'Nightly seed refresh — dedupe workspace fixtures', status: 'Done', statusColor: '#10b981', priority: 1, assignee: 'aria', date: 'Apr 18' },
    ]},
  ];
  const [selectedId, setSelected] = React.useState('PLT-431');
  return (
    <div style={{ flex: 1, overflow: 'auto', background: 'var(--bg-marketing)' }}>
      {groups.map((g) => (
        <section key={g.title}>
          <div style={{
            display: 'flex', alignItems: 'center', gap: 8,
            padding: '10px 16px', background: 'var(--bg-panel)',
            borderBottom: '1px solid var(--border-subtle)',
            borderTop: '1px solid var(--border-subtle)',
          }}>
            <span style={{ width: 8, height: 8, borderRadius: 4, background: g.color }}/>
            <span style={{ color: 'var(--fg-1)', fontSize: 13, fontWeight: 510 }}>{g.title}</span>
            <span style={{ color: 'var(--fg-4)', fontSize: 11, fontFamily: 'var(--font-mono)' }}>{g.count}</span>
          </div>
          <div onClick={() => {}}>
            {g.items.map((i) => (
              <div key={i.id} onClick={() => setSelected(i.id)}>
                <IssueRow {...i} selected={selectedId === i.id}/>
              </div>
            ))}
          </div>
        </section>
      ))}
    </div>
  );
}
window.IssueList = IssueList;
