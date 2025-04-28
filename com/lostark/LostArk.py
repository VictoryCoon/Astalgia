import os
import dotenv
import requests
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

HOST = os.getenv("LOSTARK_API_SERVER_HOST")
API_KEY = os.getenv("LOSTARK_API_KEY")
REQUEST_HEADER = {
    "User-Agent":"Coon",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "authorization":f"bearer {API_KEY}"
}

router = APIRouter()
templates = Jinja2Templates(directory="views")

@router.get("/lostark")
async def LostArk(request: Request):
    print(request)
    return templates.TemplateResponse("lostark/lostark.html",context={"request":request})