from pprint import pprint
bugs= []
while True:
    bug_name=input("Введите называние бага " \
    "")
    while True:
        priority = input("Введите приоритет: ")
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
        question = input("Хочешь добавить ещё баг? yes/no: ")

        if question in ["yes", "Yes", "no", "No"]:
            break
        else:
            print("Ошибка! Введите только yes или no")

    if question in ["no", "No"]:
        break

pprint(bugs, sort_dicts=False, width=30)
