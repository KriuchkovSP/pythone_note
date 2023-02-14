import datetime
from pyautogui import typewrite
import format_lib.file_func, check

def list():
    print("Список заметок")
    print("Введите дату, за которую показать заметки или оставьте поле пустым для вывода всех заметок")
    data_filter_1 = ""
    data_filter_1 = check.check_date()
    print("Введите вторую дату, если нужен диапазон дат или оставьте поле пустым")
    data_filter_2 = ""
    data_filter_2 = check.check_date()
    data = format_lib.file_func.read_file('data/notes.csv')
    if (data_filter_1 == "" and data_filter_2 == ""):
        print_all(data)
    else:
        print_date_filter(data,data_filter_1,data_filter_2)

def create():
    head = input("Введите заголовок новой заметки: ")
    body = input("Введите содержимое заметки: ")
    data = format_lib.file_func.read_file('data/notes.csv')
    if (len(data)) == 1:
        id = 1
    else:
        id = int(data[len(data) - 1][0]) + 1
    format_lib.file_func.add_file('data/notes.csv',id,head,body)
    read(id)
    
def read(id):
    data = format_lib.file_func.read_file('data/notes.csv')
    if (check.check_note_id(data,id)):
        print()
        index = search_index(data,id)
        print_data(data,index)
        return True
    else:
        return False
    
def edit(id):
    print()
    print('Редактирование заметки')
    data = format_lib.file_func.read_file('data/notes.csv')
    if (check.check_note_id(data,id)):
        index = search_index(data,id)
        print_data(data,index)
        print()
        print('Измените заголовок заметки, при необходимости: ')
        typewrite(f"{data[index][3]}")
        head = input()
        print('Измените тело заметки, при необходимости: ')
        typewrite(f"{data[index][4]}")
        body = input()
        return (True, data, index, id, head, body)
    else:
        return (False, -1)
        
def edit_confirm(data, index, id, head, body):
    d_now = datetime.datetime.now().strftime('%d.%m.%Y')
    t_now = datetime.datetime.now().strftime('%H:%M')
    del data[index]
    data.insert(index,(id,d_now,t_now,head,body))
    format_lib.file_func.write_file('data/notes.csv',data)
    
def delete(id):
    data = format_lib.file_func.read_file('data/notes.csv')
    if (check.check_note_id(data,id)):
        print()
        index = search_index(data,id)
        print_data(data,index)
        del data[index]
        return (True, data)
    else:
        return (False, -1)
    
def delete_confirm(data):
    format_lib.file_func.write_file('data/notes.csv',data)
    
def print_all(data):
    for i in range(len(data)):
        print(f'{data[i][0]:4s} {data[i][1]:12s} {data[i][2]:7s} {data[i][3]}')
        
def print_date_filter(data,data_filter_1,data_filter_2):
    is_date_filter = 0
    is_df1_bigger = False
    if (data_filter_2 == ""):
        is_date_filter += 1
    if (data_filter_1 == ""):
        is_date_filter += 2
    if (is_date_filter == 0):
        if (data_filter_1 > data_filter_2):
            is_df1_bigger = True
    for i in range(len(data)):
        if (i == 0):
            print(f'{data[i][0]:4s} {data[i][1]} {data[i][2]:7s} {data[i][3]}')
        else:
            date = datetime.datetime.strptime(data[i][1], "%d.%m.%Y")
            match is_date_filter:
                case 0:
                    if (is_df1_bigger):
                        if (date >= data_filter_2 and date <= data_filter_1):
                            print(f'{data[i][0]:4s} {data[i][1]} {data[i][2]:7s} {data[i][3]}')
                    else:
                        if (date >= data_filter_1 and date <= data_filter_2):
                            print(f'{data[i][0]:4s} {data[i][1]} {data[i][2]:7s} {data[i][3]}')
                case 1:
                    if (date == data_filter_1):
                        print(f'{data[i][0]:4s} {data[i][1]} {data[i][2]:7s} {data[i][3]}')
                case 2:
                    if (date == data_filter_2):
                        print(f'{data[i][0]:4s} {data[i][1]} {data[i][2]:7s} {data[i][3]}')
                case 3:
                    print(f'{data[i][0]:4s} {data[i][1]} {data[i][2]:7s} {data[i][3]}')

def search_index(data,id):
    for i in range(1,len(data)):
        if (int(data[i][0]) == id):
            return i

def print_data(data, elem):
    print(f'ID заметки: {data[elem][0]}')
    print(f'Дата создания/изменения заметки: {data[elem][1]}')
    print(f'Время создания/изменения заметки: {data[elem][2]}')
    print(f'Заголовок заметки: {data[elem][3]}')
    print(f'Содержимое заметки: {data[elem][4]}')
