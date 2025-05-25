import os
import requests
from dotenv import load_dotenv
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter,FastAPI,Request

router = APIRouter()
app = FastAPI()
templates = Jinja2Templates(directory="views")

@router.get("/")
async def Root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})