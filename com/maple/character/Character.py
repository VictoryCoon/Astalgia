import os
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="views/maple/character")

@router.get("/maple/character")
async def Character(request: Request):
    print(request)
    return templates.TemplateResponse("character.html",context={"request":request})