import ui.ui,check,notes.notes
from os import system, name  

def notes_main_menu():
    nums_menu = ui.ui.menu()
    sel_menu = check.input_data_menu(nums_menu, f'Введите пункт меню от 1 до {nums_menu}')
    match (sel_menu):
        case 1:
            clear()
            notes_list_menu()
        case 2:
            notes.notes.create()
            notes_main_menu()
        case 3:
            clear()
            print('Работа с приложением "Заметки" заврешена корректно. До свидания!')
            exit(0)
        case _:
            clear()
            print('Работа с приложением "Заметки" заврешена не корректно. До свидания!')
            exit(1)

def notes_list_menu():
    notes.notes.list()
    nums_menu = ui.ui.menu_list_notes()
    sel_menu = check.input_data_menu(nums_menu, f'Введите пункт меню от 1 до {nums_menu}')
    match (sel_menu):
        case 1:
            id = check.input_data('Введите id заметки')
            if (notes.notes.read(id)):
                notes_open_menu(id)
            else:
                notes_list_menu()
        case 2:
            id = check.input_data('Введите id заметки')
            if (notes.notes.edit(id)):
                notes_edit_menu(id)
            else:
                notes_list_menu()
        case 3:
            id = check.input_data('Введите id заметки')
            res = notes.notes.delete(id)
            if (res[0]):
                notes_delete_menu(res[1])
            else:
                notes_list_menu()
        case 4:
            clear()
            notes_main_menu()
        case _:
            exit(1)

def notes_open_menu(id: int):
    nums_menu = ui.ui.menu_open_notes()
    sel_menu = check.input_data_menu(nums_menu, f'Введите пункт меню от 1 до {nums_menu}')
    match (sel_menu):
        case 1:
            notes.notes.edit(id)
        case 2:
            notes.notes.delete(id)
        case 3:
            clear()
            notes_list_menu()
        case _:
            exit(1)
            
def notes_edit_menu(id: int):
    notes.notes.edit()
    nums_menu = ui.ui.menu_edit_notes()
    sel_menu = check.input_data_menu(nums_menu, f'Введите пункт меню от 1 до {nums_menu}')
    match (sel_menu):
        case 1:
            notes.notes.edit(id)
        case 2:
            notes.notes.delete(id)
        case 3:
            clear()
            notes_list_menu()
        case _:
            exit(1)
    
def notes_delete_menu(data):
    nums_menu = ui.ui.menu_delete_notes()
    sel_menu = check.input_data_menu(nums_menu, f'Введите пункт меню от 1 до {nums_menu}')
    match (sel_menu):
        case 1:
            notes.notes.delete_confirm(data)
            clear()
            print('Заметка удалена')
            notes_list_menu()
        case 2:
            clear()
            notes_list_menu()
        case _:
            exit(1)
 
# define the clear function  
def clear():  
     # for windows  
    if name == 'nt':  
        _ = system('cls')  

    # for mac and linux(here, os.name is 'posix')  
    else:  
        _ = system('clear')

