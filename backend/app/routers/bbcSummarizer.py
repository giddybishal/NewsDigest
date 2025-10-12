from fastapi import APIRouter
from pydantic import BaseModel
from starlette import status

from ..services.bbc_scrapper import bbc_scrapper

router = APIRouter(
    prefix='/bbcSummarizer',
    tags=['bbcSummarizer']
)

@router.get('/newsProvider', status_code=status.HTTP_200_OK)
def newsProvider():
    return bbc_scrapper()
    