import os
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="views")

@router.get("/")
async def Root(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})