import { useState } from 'react'
import Navigation from '../components/Navigation'

export default function Home() {
  const [status, setStatus] = useState<string>('')
  const [loading, setLoading] = useState<boolean>(false)

  const createAuthor = async () => {
    try {
      setLoading(true)
      setStatus('Creating author...')
      
      const response = await fetch(`${import.meta.env.VITE_API_URL}/authors/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: 'John Doe',
        }),
      })

      if (response.ok) {
        const data = await response.json()
        setStatus(`Author created successfully! ID: ${data.id}`)
      } else {
        setStatus('Failed to create author')
      }
    } catch (error: unknown) {
      setStatus(`Error: ${error instanceof Error ? error.message : 'Unknown error'}`)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gray-100">
      <Navigation />
      {/* Main content */}
      <main className="flex-1 flex justify-center items-center px-4 py-6">
        <div className="bg-white overflow-hidden shadow rounded-lg max-w-lg w-full">
          <div className="px-4 py-5 sm:p-6 flex flex-col items-center justify-center">
            {/* Create Author Button */}
            <div className="text-center mb-5">
              <button 
                onClick={createAuthor}
                disabled={loading}
                className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:bg-gray-300 disabled:cursor-not-allowed"
              >
                {loading ? 'Creating...' : 'Create Author'}
              </button>
            </div>
            
            {/* Status message */}
            {status && (
              <div className="mt-4 p-4 border rounded-md bg-gray-50 font-mono text-sm w-full">
                {status}
              </div>
            )}
          </div>
        </div>
      </main>
    </div>
  )
} 