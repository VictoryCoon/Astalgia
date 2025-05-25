import os
import re
import requests
from typing import Optional
from dotenv import load_dotenv
from fastapi import APIRouter

app = APIRouter()

load_dotenv()
HOST = os.getenv("LOSTARK_API_SERVER_HOST")
API_KEY = os.getenv("LOSTARK_API_KEY")
REQUEST_HEADER = {
    "User-Agent":"Coon",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "authorization":f"bearer {API_KEY}"
}

market_items = HOST + "markets/items/"
engraving_code = os.getenv("ENGRAVING_CODE")  # 각인서
material_code = os.getenv("MATERIAL_CODE")  # 강화재료
farming_code = os.getenv("FARMING_CODE")  # 생활재료

# Classifier
trend_engraving_list = os.getenv("CURRENT_TREND_ENGRAVING_LIST").split("|")
trend_material_list = os.getenv("CURRENT_TREND_MATERIAL_LIST").split("|")
trend_enhance_list = os.getenv("CURRENT_TREND_ENHANCE_LIST").split("|")
trend_book_list = os.getenv("CURRENT_TREND_BOOK_LIST").split("|")
living_flower = os.getenv("FARMING_FLOW_LIST").split("|")
living_fell = os.getenv("FARMING_FELL_LIST").split("|")
living_mine = os.getenv("FARMING_MINE_LIST").split("|")
living_hunt = os.getenv("FARMING_HUNT_LIST").split("|")
living_fish = os.getenv("FARMING_FISH_LIST").split("|")
living_arch = os.getenv("FARMING_ARCH_LIST").split("|")

@app.get("/allItemList/{param}")
@app.get("/allItemList/")
async def AllItemList(param:Optional[str]=None):
    if param is None:
        engravings = await EngravingList()
        materials = await MaterialList()
        farmings = await FarmingList()
    else:
        engravings = await EngravingList(param)
        materials = await MaterialList(param)
        farmings = await FarmingList(param)

    itemAll = engravings + materials + farmings
    return itemAll

@app.get("/itemInfo/{id}")
async def ItemInfo(id:str):
    print(f'검색할 아이템 ID : {id}')
    url = HOST + f"markets/items/{id}"
    item_info = requests.get(url, headers=REQUEST_HEADER)
    print(item_info.json())
    return item_info.json()

@app.get("/engravingList/{param}")
@app.get("/engravingList")
async def EngravingList(param:Optional[str]=None):
    SORT = "DESC"
    wildcard = ""
    sorting = ""
    if param is not None:
        if param.find(",") != -1:
            condition = param.split(",")
            wildcard = condition[0]
            sorting = condition[1]
            SORT = sorting
        else:
            if param.find("ASC") != -1 or param.find("DESC") != -1:
                sorting = param
                SORT = sorting
            else:
                wildcard = param
                SORT = "DESC"

    engraving_obj_1 = {"Sort":"CURRENT_MIN_PRICE","ItemGrade":"유물","CategoryCode":engraving_code,"PageNo":1,"SortCondition":SORT}
    engraving_obj_2 = {"Sort":"CURRENT_MIN_PRICE","ItemGrade":"유물","CategoryCode":engraving_code,"PageNo":2,"SortCondition":SORT}
    engraving_obj_3 = {"Sort":"CURRENT_MIN_PRICE","ItemGrade":"유물","CategoryCode":engraving_code,"PageNo":3,"SortCondition":SORT}
    engraving_obj_4 = {"Sort":"CURRENT_MIN_PRICE","ItemGrade":"유물","CategoryCode":engraving_code,"PageNo":4,"SortCondition":SORT}
    engraving_obj_5 = {"Sort":"CURRENT_MIN_PRICE","ItemGrade":"유물","CategoryCode":engraving_code,"PageNo":5,"SortCondition":SORT}
    engraving_return_1 = requests.post(market_items,json=engraving_obj_1,headers=REQUEST_HEADER)
    engraving_return_2 = requests.post(market_items,json=engraving_obj_2,headers=REQUEST_HEADER)
    engraving_return_3 = requests.post(market_items,json=engraving_obj_3,headers=REQUEST_HEADER)
    engraving_return_4 = requests.post(market_items,json=engraving_obj_4,headers=REQUEST_HEADER)
    engraving_return_5 = requests.post(market_items,json=engraving_obj_5,headers=REQUEST_HEADER)
    engravings = (engraving_return_1.json()["Items"] +
                  engraving_return_2.json()["Items"] +
                  engraving_return_3.json()["Items"] +
                  engraving_return_4.json()["Items"] +
                  engraving_return_5.json()["Items"]
    )
    filtered_engravings = []

    if wildcard != "":
        for egv in engravings:
            if egv["Name"].find(wildcard) >= 0:
                filtered_engravings.append(egv)
    else:
        for egv in engravings:
            if egv["Name"] in trend_engraving_list:
                filtered_engravings.append(egv)

    return filtered_engravings

@app.get("/materialList/{param}")
@app.get("/materialList")
async def MaterialList(param:Optional[str]=None):
    SORT = "DESC"
    wildcard = ""
    sorting = ""
    if param is not None:
        if param.find(",") != -1:
            condition = param.split(",")
            wildcard = condition[0]
            sorting = condition[1]
            SORT = sorting
        else:
            if param.find("ASC") != -1 or param.find("DESC") != -1:
                sorting = param
                SORT = sorting
            else:
                wildcard = param
                SORT = "DESC"

    material_obj_1  = {"Sort":"CURRENT_MIN_PRICE","CategoryCode":material_code,"PageNo":1,"SortCondition":SORT}
    material_obj_2  = {"Sort":"CURRENT_MIN_PRICE","CategoryCode":material_code,"PageNo":2,"SortCondition":SORT}
    material_obj_3  = {"Sort":"CURRENT_MIN_PRICE","CategoryCode":material_code,"PageNo":3,"SortCondition":SORT}
    material_obj_4  = {"Sort":"CURRENT_MIN_PRICE","CategoryCode":material_code,"PageNo":4,"SortCondition":SORT}
    material_obj_5  = {"Sort":"CURRENT_MIN_PRICE","CategoryCode":material_code,"PageNo":5,"SortCondition":SORT}
    material_obj_6  = {"Sort":"CURRENT_MIN_PRICE","CategoryCode":material_code,"PageNo":6,"SortCondition":SORT}
    material_obj_7  = {"Sort":"CURRENT_MIN_PRICE","CategoryCode":material_code,"PageNo":7,"SortCondition":SORT}
    material_obj_8  = {"Sort":"CURRENT_MIN_PRICE","CategoryCode":material_code,"PageNo":8,"SortCondition":SORT}
    material_return_1  = requests.post(market_items,json=material_obj_1,headers=REQUEST_HEADER)
    material_return_2  = requests.post(market_items,json=material_obj_2,headers=REQUEST_HEADER)
    material_return_3  = requests.post(market_items,json=material_obj_3,headers=REQUEST_HEADER)
    material_return_4  = requests.post(market_items,json=material_obj_4,headers=REQUEST_HEADER)
    material_return_5  = requests.post(market_items,json=material_obj_5,headers=REQUEST_HEADER)
    material_return_6  = requests.post(market_items,json=material_obj_6,headers=REQUEST_HEADER)
    material_return_7  = requests.post(market_items,json=material_obj_7,headers=REQUEST_HEADER)
    material_return_8  = requests.post(market_items,json=material_obj_8,headers=REQUEST_HEADER)
    materials = (
            material_return_1.json()["Items"] +
            material_return_2.json()["Items"] +
            material_return_3.json()["Items"] +
            material_return_4.json()["Items"] +
            material_return_5.json()["Items"] +
            material_return_6.json()["Items"] +
            material_return_7.json()["Items"] +
            material_return_8.json()["Items"]
    )

    filtered_materials = []
    if wildcard != "":
        for mat in materials:
            if mat["Name"].find(wildcard) >= 0:
                filtered_materials.append(mat)
    else:
        for mat in materials:
            if mat["Name"] in trend_material_list or mat["Name"] in trend_enhance_list or mat["Name"] in trend_book_list:
                filtered_materials.append(mat)

    return filtered_materials

@app.get("/farmingList/{param}")
@app.get("/farmingList")
async def FarmingList(param:Optional[str]=None):
    SORT = "DESC"
    wildcard = ""
    sorting = ""
    if param is not None:
        if param.find(",") != -1:
            condition = param.split(",")
            wildcard = condition[0]
            sorting = condition[1]
            SORT = sorting
        else:
            if param.find("ASC") != -1 or param.find("DESC") != -1:
                sorting = param
                SORT = sorting
            else:
                wildcard = param
                SORT = "DESC"

    farming_obj_1   = {"Sort":"CURRENT_MIN_PRICE","CategoryCode":farming_code,"PageNo":1,"SortCondition":SORT}
    farming_obj_2   = {"Sort":"CURRENT_MIN_PRICE","CategoryCode":farming_code,"PageNo":1,"SortCondition":SORT}
    farming_obj_3   = {"Sort":"CURRENT_MIN_PRICE","CategoryCode":farming_code,"PageNo":1,"SortCondition":SORT}
    farming_obj_4   = {"Sort":"CURRENT_MIN_PRICE","CategoryCode":farming_code,"PageNo":1,"SortCondition":SORT}

    farming_return_1   = requests.post(market_items,json=farming_obj_1,headers=REQUEST_HEADER)
    farming_return_2   = requests.post(market_items,json=farming_obj_2,headers=REQUEST_HEADER)
    farming_return_3   = requests.post(market_items,json=farming_obj_3,headers=REQUEST_HEADER)
    farming_return_4   = requests.post(market_items,json=farming_obj_4,headers=REQUEST_HEADER)

    farmings = farming_return_1.json()["Items"] + farming_return_2.json()["Items"] + farming_return_3.json()["Items"] + farming_return_4.json()["Items"]

    filtered_farmings = []
    if wildcard != "":
        for frm in farmings:
            if frm["Name"].find(wildcard) >= 0:
                filtered_farmings.append(frm)
    else:
        for frm in farmings:
            if frm["Name"] in living_flower or frm["Name"] in living_fell or frm["Name"] in living_mine or frm["Name"] in living_hunt or frm["Name"] in living_fish or frm["Name"] in living_arch:
                filtered_farmings.append(frm)

    return filtered_farmings