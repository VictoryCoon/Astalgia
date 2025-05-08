import os
import dotenv
import requests
from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates
router = APIRouter()
templates = Jinja2Templates(directory="views/lostark")

@router.get("/lostark")
async def LostArk(request: Request):
    print(request)
    return templates.TemplateResponse("lostark.html",context={"request":request})