import { useContext } from "react"
import { GetNewsContext } from "../contexts/getNewsContext"
import NewsCard from "../components/NewsCard"
import Spinner from "../components/Spinner"

function Main(){
    const { news, isLoading } = useContext(GetNewsContext)
    return (
        <div>
            {isLoading && <Spinner>Loading News...</Spinner>}
            <div className="grid grid-cols-2 md:grid-cols-3 gap-x-3 gap-y-5 text-left w-[90%] mx-auto mt-5 mb-7">
                {  (!isLoading && news) && news.map((item, index) => <NewsCard key={item.title || index} news={item}/>)}
            </div>
        </div>
        
    )
}

export default Main
