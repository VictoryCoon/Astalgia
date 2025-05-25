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
    equip_url      = HOST+"armories/characters/"+charName+"/equipment"
    gem_url       = HOST+"armories/characters/"+charName+"/gems"
    skill_url     = HOST + "armories/characters/" + charName + "/combat-skills"
    engraving_url = HOST + "armories/characters/" + charName + "/engravings"

    equip_info      = requests.get(equip_url,headers=REQUEST_HEADER)
    gem_info       = requests.get(gem_url, headers=REQUEST_HEADER)
    skill_info     = requests.get(skill_url, headers=REQUEST_HEADER)
    engraving_info = requests.get(engraving_url, headers=REQUEST_HEADER)
    engravings = engraving_info.json()

    # skill
    #print(clean_json_data(skill_info.json()))

    # Equip Info
    armor = []
    acc = []
    bracelet = []
    stone = []
    armor_types = ["무기", "투구", "상의", "하의", "장갑", "어깨"]
    ston_type = ["어빌리티 스톤"]
    acc_types = ["목걸이", "귀걸이", "반지"]
    acc_other = ["팔찌"]
    """
    acc_attacker_enchant_high    = ["적에게 주는 피해 +2.00%","추가 피해 +2.60%","치명타 피해 +4.00%","치명타 적중률 +1.55%","공격력 +390","공격력 +1.55%"]
    acc_attacker_enchant_middle  = ["적에게 주는 피해 +1.20%","추가 피해 +1.60%","치명타 피해 +2.40%","치명타 적중률 +0.95%","공격력 +195","공격력 +0.95%"]
    acc_attacker_enchant_low     = ["적에게 주는 피해 +0.55%","추가 피해 +0.70%","치명타 피해 +1.10%","치명타 적중률 +0.40%","공격력 +80", "공격력 +0.40%"]
    acc_supporter_enchant_high   = ["낙인력 +8.00%","아군 공격력 강화 효과 +5.00%","아군 피해량 강화 효과 +7.50%","세레나데, 신앙, 조화 게이지 획득량 +6.00%","파티원 보호막 효과 +3.50%"]
    acc_supporter_enchant_middle = ["낙인력 +4.80%","아군 공격력 강화 효과 +3.00%","아군 피해량 강화 효과 +4.50%","세레나데, 신앙, 조화 게이지 획득량 +3.60%","파티원 보호막 효과 +2.10%"]
    acc_supporter_enchant_low    = ["낙인력 +2.15%","아군 공격력 강화 효과 +1.35%","아군 피해량 강화 효과 +2.00%","세레나데, 신앙, 조화 게이지 획득량 +1.60%","파티원 보호막 효과 +0.95%"]
    acc_mutual_enchant_high      = ["최대 생명력 +6500","상태이상 공격 지속시간 +1.00%","전투 중 생명력 회복량 +50","최대 마나 +30","무기 공격력 +960","무기 공격력 +3.00%"]
    acc_mutual_enchant_middle    = ["최대 생명력 +3250","상태이상 공격 지속시간 +0.50%","전투 중 생명력 회복량 +25","최대 마나 +15","무기 공격력 +480","무기 공격력 +1.80%"]
    acc_mutual_enchant_low       = ["최대 생명력 +1300","상태이상 공격 지속시간 +0.20%","전투 중 생명력 회복량 +10","최대 마나 +6", "무기 공격력 +195","무기 공격력 +0.80%"]
    """
    acc_enchant_high = [
        "적에게 주는 피해 +2.00%","추가 피해 +2.60%","치명타 피해 +4.00%","치명타 적중률 +1.55%","공격력 +390","공격력 +1.55%",                                 # Attacker
        "낙인력 +8.00%", "아군 공격력 강화 효과 +5.00%", "아군 피해량 강화 효과 +7.50%", "세레나데, 신앙, 조화 게이지 획득량 +6.00%", "파티원 보호막 효과 +3.50%",    # Supporter
        "최대 생명력 +6500", "상태이상 공격 지속시간 +1.00%", "전투 중 생명력 회복량 +50", "최대 마나 +30", "무기 공격력 +960", "무기 공격력 +3.00%"                # Common
    ]

    acc_enchant_middle = [
        "적에게 주는 피해 +1.20%", "추가 피해 +1.60%", "치명타 피해 +2.40%", "치명타 적중률 +0.95%", "공격력 +195", "공격력 +0.95%",                            # Attacker
        "낙인력 +4.80%", "아군 공격력 강화 효과 +3.00%", "아군 피해량 강화 효과 +4.50%", "세레나데, 신앙, 조화 게이지 획득량 +3.60%", "파티원 보호막 효과 +2.10%",    # Supporter
        "최대 생명력 +3250", "상태이상 공격 지속시간 +0.50%", "전투 중 생명력 회복량 +25", "최대 마나 +15", "무기 공격력 +480", "무기 공격력 +1.80%"                # Common
    ]

    acc_enchant_low = [
        "적에게 주는 피해 +0.55%", "추가 피해 +0.70%", "치명타 피해 +1.10%", "치명타 적중률 +0.40%", "공격력 +80", "공격력 +0.40%",                             # Attacker
        "낙인력 +4.80%", "아군 공격력 강화 효과 +3.00%", "아군 피해량 강화 효과 +4.50%", "세레나데, 신앙, 조화 게이지 획득량 +3.60%", "파티원 보호막 효과 +2.10%",    # Supporter
        "최대 생명력 +1300", "상태이상 공격 지속시간 +0.20%", "전투 중 생명력 회복량 +10", "최대 마나 +6", "무기 공격력 +195", "무기 공격력 +0.80%"                 # Common
    ]
    for equips in equip_info.json():
        if equips["Type"] in armor_types:
            tooltip_value = json.loads(equips["Tooltip"])
            quality_value = tooltip_value["Element_001"]['value']
            equips["Quality"] = quality_value['qualityValue']
            armor.append(equips)
        elif equips["Type"] in acc_types:
            tooltip_value = json.loads(equips["Tooltip"])
            option_value = tooltip_value["Element_005"]["value"]
            quality_value = tooltip_value["Element_001"]['value']
            pattern = r"<img.*?></img>(.*?)(?=<img|$)"
            options = clean_double_side_data(pattern, option_value["Element_001"])
            equips["Enchant"] = clean_json_data(options)
            equips["Quality"] = quality_value['qualityValue']
            equips["Enchant_Rank"] = ["","",""]

            for i in range(3):
                if equips["Enchant"][i] in acc_enchant_high:
                    equips["Enchant_Rank"][i] = "H"
                elif equips["Enchant"][i] in acc_enchant_middle:
                    equips["Enchant_Rank"][i] = "M"
                elif equips["Enchant"][i] in acc_enchant_low:
                    equips["Enchant_Rank"][i] = "L"

            acc.append(clean_json_data(equips))
            print(equips)
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
                if effrect["Description"][0].find('피해') != -1:
                    effrect["Type"] = "D"
                elif effrect["Description"][0].find('재사용') != -1:
                    effrect["Type"] = "C"

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
            ,"skills":clean_json_data(skill_info.json())
            ,"engrave":engravings
        }
    )

