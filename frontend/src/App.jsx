import { BrowserRouter, Routes, Route } from 'react-router-dom'

import Main from "./pages/Main"
import { NewsProvider  } from "./contexts/getNewsContext"

function App() {
  return (
      <BrowserRouter>
        <NewsProvider>
          <Routes>
            <Route path='/' element={<Main />} />
          </Routes>
        </NewsProvider>
      </BrowserRouter>
      
  )
}

export default App
