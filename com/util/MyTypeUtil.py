import re

# Tag 및 Escape 제거 정규식
def remove_regex(value):
    clean = re.compile(r'<.*?>|\r\n')
    return re.sub(clean, '', value)

# Dictionary 혹은 Object 타입의 정규식 순회 적용을 위한 함수
def clean_json_data(data):
    if isinstance(data, str):
        return remove_regex(data)
    elif isinstance(data, dict):
        return {key: clean_json_data(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [clean_json_data(item) for item in data]
    return data

# 양쪽사이드로 감쌓여진 패턴 제거 : Ex - pattern = r"<img.*?></img>(.*?)(?=<img|$)"
def remove_double_side_pattern(pattern, object):
    return re.findall(pattern, object, re.DOTALL)

def clean_double_side_data(pattern, data):
    if isinstance(data, str):
        return remove_double_side_pattern(pattern, data)
    elif isinstance(data, dict):
        return {key: remove_double_side_pattern(pattern, value) for key, value in data.items()}
    elif isinstance(data, list):
        return [remove_double_side_pattern(pattern, item) for item in data]
    return data

def get_extract_just_number(object):
    return re.findall(r'-?\d+\.?\d*', object)

def clean_without_number(data):
    if isinstance(data, str):
        return get_extract_just_number(data)
    elif isinstance(data, dict):
        return {key: get_extract_just_number(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [get_extract_just_number(item) for item in data]
    return data