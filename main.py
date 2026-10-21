bug_name=input("Введите называние бага")
while True:
    priority = input("Введите приоритет: ")
    if priority in ["Low","low","Medium","medium","High","high"]:
        break
    else:   
        print('Wrong priority,please input Low,Medium or High')
Bug_id=1
status = 'Open'
print("Баг успешно создан!")
print("Название:", bug_name)
print("Приоритет:", priority)
print("ID:",Bug_id)
print('Статус:', status)