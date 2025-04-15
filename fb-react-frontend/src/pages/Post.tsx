import { useParams } from 'react-router-dom'
import Navigation from '../components/Navigation'

export default function Post() {
  const { id } = useParams<{ id: string }>()

  return (
    <div className="min-h-screen bg-gray-100">
      <Navigation />
      
      {/* Main content */}
      <main className="flex-1 flex justify-center items-center px-4 py-6">
        <div className="bg-white overflow-hidden shadow rounded-lg max-w-lg w-full">
          <div className="px-4 py-5 sm:p-6 flex flex-col items-center justify-center">
            <p className="text-lg text-gray-700">Post ID: {id}</p>
            <p className="text-md text-gray-500 mt-2">This is an empty post page for development.</p>
          </div>
        </div>
      </main>
    </div>
  )
} 