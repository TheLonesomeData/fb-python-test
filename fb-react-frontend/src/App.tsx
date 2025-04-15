import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import Home from './pages/Home'
import Post from './pages/Post'

const router = createBrowserRouter([
  {
    path: '/',
    element: <Home />
  },
  {
    path: '/post/:id',
    element: <Post />
  }
])

function App() {
  return <RouterProvider router={router} />
}

export default App
