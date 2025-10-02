import { useEffect, useState } from 'react'

const API_BASE = import.meta.env.VITE_API_BASE || '/api'

export default function App() {
  const [status, setStatus] = useState<string>('checking...')
  const [progress, setProgress] = useState<any>(null)

  useEffect(() => {
    fetch(`${API_BASE}/health`).then(r => r.json()).then(d => setStatus(d.status)).catch(() => setStatus('offline'))
    fetch(`${API_BASE}/progress/demo`).then(r => r.json()).then(setProgress).catch(() => setProgress(null))
  }, [])

  return (
    <div style={{ fontFamily: 'sans-serif', padding: 16 }}>
      <h1>NanoSkool Dashboard</h1>
      <p>Backend: {status}</p>
      <h2>Demo Progress</h2>
      <pre>{progress ? JSON.stringify(progress, null, 2) : 'No data'}</pre>
    </div>
  )
}
