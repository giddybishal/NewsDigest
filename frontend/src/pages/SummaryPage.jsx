import { useContext, useEffect, useState } from "react"
import { useLocation } from "react-router-dom"
import { GetSummaryContext } from "../contexts/GetSummaryContext"
import { GetNewsContext } from "../contexts/getNewsContext"
import Spinner from "../components/Spinner"

function SummaryPage(){
    const location = useLocation()
    const url = location.state

    const [ summary, setSummary ] = useState('')

    const { getSummary } = useContext(GetSummaryContext)
    const { isLoading, setIsLoading } = useContext(GetNewsContext)

    useEffect( () =>{
        if(!url) return

        const fetch_Summary = async()=>{
            setIsLoading(true)
            const res = await getSummary(url)
            setSummary(res)
            setIsLoading(false)
        }

        fetch_Summary()
    }, [url])

    return (
        <div className="text-white">
            { isLoading && <Spinner>Summarizing News...</Spinner>}
            { summary && <div dangerouslySetInnerHTML={{ __html: summary }} /> }
        </div>
    )
}

export default SummaryPage
