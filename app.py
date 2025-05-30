import uvicorn
import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from com import Root
from com.lostark import LostArk
from com.lostark.character import Character as LostArkCharacter

app = FastAPI()
@app.get("/favicon.ico")
async def get_favicon():
    return FileResponse("assets/favicon.ico", media_type="image/x-icon")

app.mount("/assets", StaticFiles(directory="assets"), name="assets")

app.include_router(Root.router)

app.include_router(LostArk.app)
app.include_router(LostArkCharacter.router)

port = int(os.environ.get("PORT", 10000))


if __name__ == "__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=port,reload=True)
