import uvicorn
from com import Root
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from com import Root
from com.lostark import LostArk

app = FastAPI()
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

app.include_router(Root.router)
app.include_router(LostArk.router)

if __name__ == "__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=10000,reload=True)