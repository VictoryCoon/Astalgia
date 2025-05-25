import os
import requests
from dotenv import load_dotenv
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter,FastAPI,Request,Query

router = APIRouter()
app = FastAPI()
templates = Jinja2Templates(directory="views")

load_dotenv()
HOST = os.getenv("LOSTARK_API_SERVER_HOST")
API_KEY = os.getenv("LOSTARK_API_KEY")
REQUEST_HEADER = {
    "User-Agent":"Coon",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "authorization":f"bearer {API_KEY}"
}

@router.get("/")
async def Root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/item/{itemName}")
async def getItem(itemName:str):
    print("GET?")
    print(itemName)
    market_items = HOST + "markets/items/"
    engraving_code  = os.getenv("ENGRAVING_CODE")    #각인서
    material_code   = os.getenv("MATERIAL_CODE")      #강화재료
    ingredient_code = os.getenv("INGREDIENT_CODE")  #생활재료

    engraving_obj = {"Sort": "CURRENT_MIN_PRICE", "CategoryCode": engraving_code,"PageNo": 1,"SortCondition":"DESC"}
    tier_3_material_obj = {"Sort":"CURRENT_MIN_PRICE","CategoryCode":material_code,"ItemTier":3,"PageNo":1,"SortCondition":"DESC"}
    tier_4_material_obj = {"Sort":"CURRENT_MIN_PRICE","CategoryCode":material_code,"ItemTier":4,"PageNo":1,"SortCondition":"DESC"}
    life_ingredient_obj = {"Sort":"CURRENT_MIN_PRICE","CategoryCode":ingredient_code,"PageNo":1,"SortCondition":"DESC"}

    engraving_return = requests.post(market_items,json=engraving_obj,headers=REQUEST_HEADER)
    tier_3_material_return = requests.post(market_items,json=tier_3_material_obj,headers=REQUEST_HEADER)
    tier_4_material_return = requests.post(market_items,json=tier_4_material_obj,headers=REQUEST_HEADER)
    life_ingredient_return = requests.post(market_items,json=life_ingredient_obj,headers=REQUEST_HEADER)
    engravings = engraving_return.json()
    tier_3_materials = tier_3_material_return.json()
    tier_4_materials = tier_4_material_return.json()
    life_ingredients = life_ingredient_return.json()

    #print(engravings)
    #print(tier_3_materials)
    #print(tier_4_materials)
    #print(life_ingredients)

    for item in life_ingredients["Items"]:
        if item["Name"].find(itemName) != -1:
            print(item)

    return itemName