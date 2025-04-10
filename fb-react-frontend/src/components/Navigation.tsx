import { Link } from 'react-router-dom'

export default function Navigation() {
  return (
    <nav className="bg-indigo-600">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <span className="text-white font-bold">Blog App</span>
            </div>
            <div className="ml-10 flex items-baseline space-x-4">
              <Link 
                to="/" 
                className="text-white hover:bg-indigo-700 px-3 py-2 rounded-md text-sm font-medium"
              >
                Home
              </Link>
              <Link 
                to="/post/1" 
                className="text-white hover:bg-indigo-700 px-3 py-2 rounded-md text-sm font-medium"
              >
                Sample Post
              </Link>
            </div>
          </div>
        </div>
      </div>
    </nav>
  )
} 