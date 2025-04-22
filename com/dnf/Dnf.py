import os
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="views/dnf")

@router.get("/dnf")
async def Dnf(request: Request):
    print(request)
    return templates.TemplateResponse("dnf.html",context={"request":request})