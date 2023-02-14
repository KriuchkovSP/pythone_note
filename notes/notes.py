import datetime
from pyautogui import typewrite
import format_lib.file_func, check

def list():
    print('Список заметок')
    data = format_lib.file_func.read_file('data/notes.csv')
    print_all(data)
    
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
        typewrite(f"{data[index][2]}")
        head = input()
        print('Измените тело заметки, при необходимости: ')
        typewrite(f"{data[index][3]}")
        body = input()
        return (True, data, index, id, head, body)
    else:
        return (False, -1)
        
def edit_confirm(data, index, id, head, body):
    dt_now = datetime.datetime.now().strftime('%H:%M %m.%d.%Y')
    del data[index]
    data.insert(index,(id,dt_now,head,body))
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
        print(f'{data[i][0]:4s} {data[i][1]:18s} {data[i][2]}')

def search_index(data,id):
    for i in range(1,len(data)):
        if (int(data[i][0]) == id):
            return i

def print_data(data, elem):
    print(f'ID заметки: {data[elem][0]}')
    print(f'Дата создания/изменения заметки: {data[elem][1]}')
    print(f'Заголовок заметки: {data[elem][2]}')
    print(f'Содержимое заметки: {data[elem][3]}')
