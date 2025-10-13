from fastapi import APIRouter
from pydantic import BaseModel
from starlette import status

from ..services.bbc_scrapper import bbc_scrapper
from ..services.llama_summarizer import bbc_summarizer

router = APIRouter(
    prefix='/bbcSummarizer',
    tags=['bbcSummarizer']
)

class NewsURL(BaseModel):
    url: str

@router.get('/newsProvider', status_code=status.HTTP_200_OK)
def newsProvider():
    return bbc_scrapper()
    
@router.post('/newsSummarized', status_code=status.HTTP_200_OK)
def newsSummarized(url: NewsURL):
    return bbc_summarizer(url.url)
