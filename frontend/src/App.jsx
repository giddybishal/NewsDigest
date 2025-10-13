import { BrowserRouter, Routes, Route } from 'react-router-dom'

import Main from "./pages/Main"
import SummaryPage from './pages/SummaryPage'
import { NewsProvider  } from "./contexts/getNewsContext"
import { SummaryProvider } from './contexts/GetSummaryContext'

function App() {
  return (
      <BrowserRouter>
        <NewsProvider>
          <SummaryProvider>
            <Routes>
             <Route path='/' element={<Main />} />
             <Route path='/summary' element={<SummaryPage />}/>
            </Routes>
          </SummaryProvider>
        </NewsProvider>
      </BrowserRouter>
      
  )
}

export default App
