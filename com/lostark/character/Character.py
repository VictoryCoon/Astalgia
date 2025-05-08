import os
from com.util.MyTypeUtil import clean_json_data, remove_double_side_pattern, clean_double_side_data, clean_without_number
import json
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
from typing import Optional
from fastapi import APIRouter, Request, Form, Query
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

load_dotenv()
HOST = os.getenv("LOSTARK_API_SERVER_HOST")
API_KEY = os.getenv("LOSTARK_API_KEY")
REQUEST_HEADER = {
    "User-Agent":"Coon",
    "Content-Type": "application/json",
    "Accept": "application/json",
    "authorization":f"bearer {API_KEY}"
}

router = APIRouter()
templates = Jinja2Templates(directory="views/lostark/character")

@router.get("/lostark/search",response_class=HTMLResponse)
async def CharacterInformation(request: Request,charName:str=Query(str)):
    print(HOST)
    equip_url      = HOST+"armories/characters/"+charName+"/equipment"
    gem_url       = HOST+"armories/characters/"+charName+"/gems"
    skill_url     = HOST + "armories/characters/" + charName + "/combat-skills"
    engraving_url = HOST + "armories/characters/" + charName + "/engravings"

    equip_info      = requests.get(equip_url,headers=REQUEST_HEADER)
    gem_info       = requests.get(gem_url, headers=REQUEST_HEADER)
    skill_info     = requests.get(skill_url, headers=REQUEST_HEADER)
    engraving_info = requests.get(engraving_url, headers=REQUEST_HEADER)
    engravings = engraving_info.json()

    # Equip Info
    armor = []
    acc = []
    bracelet = []
    stone = []
    armor_types = ["무기", "투구", "상의", "하의", "장갑", "어깨"]
    ston_type = ["어빌리티 스톤"]
    acc_types = ["목걸이", "귀걸이", "반지"]
    acc_other = ["팔찌"]
    for equips in equip_info.json():
        if equips["Type"] in armor_types:
            armor.append(equips)
        elif equips["Type"] in acc_types:
            tooltip_value = json.loads(equips["Tooltip"])
            option_value = tooltip_value["Element_005"]["value"]
            #print(option_value["Element_001"])
            pattern = r"<img.*?></img>(.*?)(?=<img|$)"
            matches = clean_double_side_data(pattern, option_value["Element_001"])
            equips["Enchant"] = clean_json_data(matches)
            """
            여기서부터는 단위 노가다를 해야한다.
            로스트아크 목걸이/귀걸이/반지의 주요 옵션들의 [상/중/하] 범주를 if문으로 구현하고, 그 값에 따라 Rank값을 맥여야함.
            val 
            """
            print(clean_without_number(matches))
            acc.append(clean_json_data(equips))
        elif equips["Type"] in acc_other:
            bracelet.append(equips)
        elif equips["Type"] in ston_type:
            stone.append(equips)

    # Gems Info
    effrects = gem_info.json()["Effects"]["Skills"]
    for effrect in effrects:
        for gem in gem_info.json()["Gems"]:
            if effrect["GemSlot"] == gem["Slot"]:
                effrect["GemIcon"] = gem["Icon"]
                effrect["GemName"] = gem["Name"]
                effrect["GemLevel"] = gem["Level"]
                effrect["GemGrade"] = gem["Grade"]

    return templates.TemplateResponse(
        "character.html"
        ,context={
            "request":request
            ,"charName":charName
            ,"armors":clean_json_data(armor)
            ,"accs":clean_json_data(acc)
            ,"bracelet":clean_json_data(bracelet)
            ,"stone":clean_json_data(stone)
            ,"gems":clean_json_data(effrects)
            ,"skills":skill_info.json()
            ,"engrave":engravings
        }
    )

