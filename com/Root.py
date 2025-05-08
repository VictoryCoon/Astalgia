import os
from fastapi import APIRouter, FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse
from pydantic import BaseModel

router = APIRouter()
app = FastAPI()
templates = Jinja2Templates(directory="views")

@router.get("/")
async def Root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})