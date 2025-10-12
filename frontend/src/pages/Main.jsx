import { useContext } from "react"
import { GetNewsContext } from "../contexts/getNewsContext"
import NewsCard from "../components/NewsCard"

function Main(){
    const { news } = useContext(GetNewsContext)
    return (
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 text-left">
            { news && news.map((item, index) => <NewsCard key={item.title || index} news={item}/>)}
        </div>
    )
}

export default Main
