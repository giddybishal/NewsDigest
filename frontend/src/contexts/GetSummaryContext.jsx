import { createContext, useContext } from "react";

export const GetSummaryContext = createContext()

export function SummaryProvider({children}){
    const BACKEND_URL = 'http://127.0.0.1:8000'

    async function getSummary(url){
        try{
            const res = await fetch(`${BACKEND_URL}/bbcSummarizer/newsSummarized`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({url})
            });
            if (res.ok){
                const data = await res.json()
                return data.summary
            }else{
                const errData = await res.json()
                alert(errData.detail || 'Failed to Summarize')
                return null
            }
        }catch(err){
            console.error('Error summarizing news:', err)
        }
    }

    return (
        <GetSummaryContext.Provider value={{ getSummary }}>
            {children}
        </GetSummaryContext.Provider>
    )
}
