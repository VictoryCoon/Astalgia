import os
import json
import requests
from dotenv import load_dotenv
from fastapi import APIRouter,Request,Query

from fastapi.templating import Jinja2Templates
router = APIRouter()
templates = Jinja2Templates(directory="views/lostark")

load_dotenv()
HOST = os.getenv("LOSTARK_API_SERVER_HOST")
API_KEY = os.getenv("LOSTARK_API_KEY")
REQUEST_HEADER = {
    "User-Agent":"Coon",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "authorization":f"bearer {API_KEY}"
}

@router.get("/lostark")
async def LostArk(request: Request):
    print("로스트아크")
    return templates.TemplateResponse("lostark.html",context={"request":request})

