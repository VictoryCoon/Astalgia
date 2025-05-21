import uvicorn
import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from com import Root

from com.dnf import Dnf
from com.maple import Maple
from com.lostark import LostArk
from com.dnf.character import Character as DnfCharacter
from com.maple.character import Character as MapleCharacter
from com.lostark.character import Character as LostArkCharacter

app = FastAPI()
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

app.include_router(Root.router)

app.include_router(Dnf.router)
app.include_router(DnfCharacter.router)

app.include_router(LostArk.router)
app.include_router(LostArkCharacter.router)

app.include_router(Maple.router)
app.include_router(MapleCharacter.router)

port = int(os.environ.get("PORT", 10000))

if __name__ == "__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=port,reload=True)
