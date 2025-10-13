import { useNavigate } from "react-router-dom"

function NewsCard({news}){
    const { title, url, img_path } = news
    const navigate = useNavigate()

    return (
        <div className="bg-blue-950 text-white p-1 rounded-md flex flex-col">
            <img src={img_path}/>
            <p className="font-bold mt-1 mb-3 mx-2">{title}</p>
            <div className="flex mb-2 mx-2 mt-auto">
                <span className="text-yellow-400 cursor-pointer"
                onClick = {
                    () => navigate('/summary', { state: url})
                }
                >Summarize</span>
                <a href={url} target="_blank" className="text-green-400 cursor-pointer ml-auto">Read</a>
            </div>       
        </div>
    )
}

export default NewsCard
