import os
from fastapi import APIRouter, FastAPI, Form,Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

router = APIRouter()
app = FastAPI()
templates = Jinja2Templates(directory="views")

@router.get("/")
async def Root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/search",response_class=HTMLResponse)
async def questionAndAnswer(request: Request, question:str=Form(...)):
    print(question)
    return templates.TemplateResponse("./index.html", {"request": request,"answer":question})