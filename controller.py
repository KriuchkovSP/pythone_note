import ui.ui,check,notes.notes
from os import system, name  

def notes_main_menu():
    nums_menu = ui.ui.menu()
    sel_menu = check.input_data(nums_menu)
    match (sel_menu):
        case 1:
            clear()
            notes_list_menu()
        case 2:
            notes.notes.create()
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
    sel_menu = check.input_data(nums_menu)
    match (sel_menu):
        case 1:
            notes.notes.read()
        case 2:
            notes.notes.edit()
        case 3:
            notes.notes.delete()
        case 4:
            clear()
            notes_main_menu()
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
