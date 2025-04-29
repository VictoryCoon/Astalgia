import os
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="views/maple")

@router.get("/maple")
async def Maple(request: Request):
    print(request)
    return templates.TemplateResponse("maple.html",context={"request":request})