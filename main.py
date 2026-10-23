from pathlib import Path
from pprint import pprint
import json
import os


DATA_FILE = Path(__file__).resolve().parent / "bugs.json"

if DATA_FILE.exists():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        bugs = json.load(file)
else:
    bugs = []

print("Файл с багами:", DATA_FILE)
print("Загружено багов:", len(bugs))

while True:
    bug_name=input("Введите называние бага " \
    "")
    while True:
        priority = input("Введите приоритет: ").strip().lower()
        if priority in ["Low","low","Medium","medium","High","high"]:
            break
        else:   
            print('Wrong priority,please input Low,Medium or High')
    Bug_id = len(bugs) + 1
    status = 'Open'
    bug={
    "id": Bug_id,
    "name":bug_name,
    "priority": priority,
    "status": status
     }   
    bugs.append(bug)
    
    while True:
        question = input("Хочешь добавить ещё баг? yes/no: ").strip().lower()

        if question in ["yes", "y", "no", "n"]:
    
            break
        else:
            print("Ошибка! Введите только yes или no")

    if question in ["no","n"]:
        break

pprint(bugs, sort_dicts=False, width=30)

with open(DATA_FILE, "w", encoding="utf-8") as file:
    json.dump(bugs, file, ensure_ascii=False, indent=4)

search_id = int(input("Введите ID бага: "))
print("В поисках бага ...")
for item in bugs:
    
    if item["id"] == search_id:
        pprint(item,sort_dicts=False, width=30)
        question = input("Хотите изменить баг? yes/no: ").strip().lower()
        if question in ["yes","Yes","y"]:
            print("Переходим к редактированию")
            field = input("Какое поле изменить? name/priority/status: ").strip().lower()
            if field =="name":
                item["name"]=input("Введите новое имя ").strip()
            elif field =="priority":
                while True :
                 new_priority=input("Введите новый приоритет: ").strip().lower()
                 if new_priority in ["Low","low","Medium","medium","High","high"]:
                    item["priority"]= new_priority.title()
                    break
                 else:   
                    print('Wrong priority,please input Low,Medium or High')
            elif field =="status":
                while True:
                    new_status= input("Введите новый статус: ").strip().lower()
                    if new_status in ["open","in progress","closed"]:
                        item["status"]= new_status.title()
                        break
                    else:   
                        print('Wrong status, please pick only "Open","pass","in progress","close","error"  ')
            print("Результат редактирования:")
            pprint(item, sort_dicts=False, width=30)
            with open(DATA_FILE, "w", encoding="utf-8") as file:
                json.dump(bugs, file, ensure_ascii=False, indent=4)
        else:
            print("Баг оставлен без изменений")
        break
else:
    print("Баг не найден")