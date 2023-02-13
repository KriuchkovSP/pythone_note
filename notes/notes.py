import os
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
    format_lib.file_func.write_file('data/notes.csv',id,head,body)
    read(id)
    
def read(id):
    data = format_lib.file_func.read_file('data/notes.csv')
    if (check.check_note_id(data,id)):
        print()
        print_data(data,id)
        return True
    else:
        return False
    
def edit(id):
    print('Редактирование заметки')
    data = format_lib.file_func.read_file('data/notes.csv')
    if (check.check_note_id(data,id)):
        print()
        print_data(data,id)
        return True
    else:
        return False
        
    print("enter folder name: ")
    typewrite("Default Value")
    folder = input()
    
def delete(id):
    data = format_lib.file_func.read_file('data/notes.csv')
    if (check.check_note_id(data,id)):
        print()
        elem = print_data(data,id)
        del data[elem]
        return (True, data)
    else:
        return (False, -1)
    
def delete_confirm(data):
    format_lib.file_func.write_file('data/notes.csv',data)
    
def print_all(data):
    for i in range(len(data)):
        print(f'{data[i][0]:4s} {data[i][1]:18s} {data[i][2]}')

def print_data(data, id):
    for i in range(1,len(data)):
        if (int(data[i][0]) == id):
            print(f'ID заметки: {data[i][0]}')
            print(f'Дата создания/изменения заметки: {data[i][1]}')
            print(f'Заголовок заметки: {data[i][2]}')
            print(f'Содержимое заметки: {data[i][3]}')
            return i
            