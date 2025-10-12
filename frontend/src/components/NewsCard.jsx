function NewsCard({news}){
    const { title, url, img_path } = news

    return (
        <div className="text-white">
            <img src={img_path}/>
            <p>{title}</p>
            <a href={url} target="_blank">Link to the News </a>
        </div>
    )
}

export default NewsCard
