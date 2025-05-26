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
trend_atk_egv_list = os.getenv("CURRENT_TREND_ATK_EGV_LIST").split("|")
trend_spt_egv_list = os.getenv("CURRENT_TREND_SPT_EGV_LIST").split("|")
trend_material_list = os.getenv("CURRENT_TREND_MATERIAL_LIST").split("|")
trend_enhance_list = os.getenv("CURRENT_TREND_ENHANCE_LIST").split("|")
trend_scroll_list = os.getenv("CURRENT_TREND_SCROLL_LIST").split("|")
trend_book_list = os.getenv("CURRENT_TREND_BOOK_LIST").split("|")
esther = os.getenv("ESTHER").split("|")
living_flower = os.getenv("FARMING_FLOW_LIST").split("|")
living_fell = os.getenv("FARMING_FELL_LIST").split("|")
living_mine = os.getenv("FARMING_MINE_LIST").split("|")
living_hunt = os.getenv("FARMING_HUNT_LIST").split("|")
living_fish = os.getenv("FARMING_FISH_LIST").split("|")
living_arch = os.getenv("FARMING_ARCH_LIST").split("|")

@app.get("/allItemList/{param}")
@app.get("/allItemList")
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

@app.get("/itemInfoById/{id}")
async def ItemInfoById(id:str):
    #print(f'검색할 아이템 ID : {id}')
    url = HOST + f"markets/items/{id}"
    item_info = requests.get(url, headers=REQUEST_HEADER)
    #print(item_info.json()[1])  # 왜 0번 index는 값이 전부 0원인지, 난 모른다.
    return item_info.json()[1]

@app.get("/itemInfoByName/{name}")
async def ItemInfoById(name:str):
    #print(f'검색할 아이템 Name : {name}')
    only_search_obj_egv = {"Sort":"CURRENT_MIN_PRICE","ItemName":name,"ItemGrade":"유물","CategoryCode":engraving_code,"PageNo":1,"SortCondition":"DESC"}
    only_search_obj_mat = {"Sort":"CURRENT_MIN_PRICE","ItemName":name,"CategoryCode":material_code,"PageNo":1,"SortCondition":"DESC"}
    only_search_obj_frm = {"Sort":"CURRENT_MIN_PRICE","ItemName":name,"CategoryCode":farming_code,"PageNo":1,"SortCondition":"DESC"}
    only_search_egv_return = requests.post(market_items,json=only_search_obj_egv,headers=REQUEST_HEADER)
    only_search_mat_return = requests.post(market_items,json=only_search_obj_mat,headers=REQUEST_HEADER)
    only_search_frm_return = requests.post(market_items,json=only_search_obj_frm,headers=REQUEST_HEADER)
    only_search_info = only_search_egv_return.json()["Items"] + only_search_mat_return.json()["Items"] + only_search_frm_return.json()["Items"]
    return only_search_info

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
                egv["Type"] = "99"
                filtered_engravings.append(egv)
    else:
        for egv in engravings:
            if egv["Name"] in trend_atk_egv_list:
                egv["Type"] = "10"
                filtered_engravings.append(egv)
            if egv["Name"] in trend_spt_egv_list:
                egv["Type"] = "20"
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
                mat["Type"] = "99"
                filtered_materials.append(mat)
    else:
        for mat in materials:
            if mat["Name"] in trend_material_list:
                mat["Type"] = "10"
                filtered_materials.append(mat)
            elif mat["Name"] in trend_enhance_list:
                mat["Type"] = "11"
                filtered_materials.append(mat)
            elif mat["Name"] in trend_scroll_list:
                mat["Type"] = "12"
                filtered_materials.append(mat)
            elif mat["Name"] in trend_book_list:
                mat["Type"] = "13"
                filtered_materials.append(mat)
            elif mat["Name"] in esther:
                mat["Type"] = "00"
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
                frm["Type"] = "99"
                filtered_farmings.append(frm)
    else:
        for frm in farmings:
            if frm["Name"] in living_flower:
                frm["Type"] = "10"
                filtered_farmings.append(frm)
            elif frm["Name"] in living_fell:
                frm["Type"] = "11"
                filtered_farmings.append(frm)
            elif frm["Name"] in living_mine:
                frm["Type"] = "12"
                filtered_farmings.append(frm)
            elif frm["Name"] in living_hunt:
                frm["Type"] = "13"
                filtered_farmings.append(frm)
            elif frm["Name"] in living_fish:
                frm["Type"] = "14"
                filtered_farmings.append(frm)
            elif frm["Name"] in living_arch:
                frm["Type"] = "15"
                filtered_farmings.append(frm)

    return filtered_farmings