import { createContext, useEffect, useState } from "react";

export const GetNewsContext = createContext()

export function NewsProvider({children}){
    const [ news, setNews ] = useState([])

    const BACKEND_URL = 'http://127.0.0.1:8000'

    async function getNews(){
        try{
            const res = await fetch(`${BACKEND_URL}/bbcSummarizer/newsProvider`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
            });
            if (res.status === 200){
                const data = await res.json()
                setNews(data)
                console.log(data)
            }else{
                const errData = await res.json()
                alert(errData.detail || 'Failed to fetch News')
            }
        }catch(err){
            console.error('Error fetching news:', err)
        }
    }

    useEffect(()=>{
        getNews();
    }, [])

    return (
        <GetNewsContext.Provider value={{ news, getNews}}>
            {children}
        </GetNewsContext.Provider>
    )
}
