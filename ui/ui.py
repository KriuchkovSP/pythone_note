def menu():
    print('Здравствуйте. Вы в приложении "Заметки",\r\n\
для работы с приложением введите пункт меню и нажмите Enter:')
    print()
    print('1. Вывести список заметок')
    print('2. Создать заметку')
    print('3. Выход')
    return 3
    
def menu_list_notes():
    print()
    print('1. Прочитать заметку')
    print('2. Редактировать заметку')
    print('3. Удалить заметку')
    print('4. Создать заметку')
    print('5. Назад')
    return 5

def menu_open_notes():
    print()
    print('1. Редактировать заметку')
    print('2. Удалить заметку')
    print('3. Назад')
    return 3

def menu_delete_notes():
    print()
    print('1. Удалить заметку')
    print('2. Отмена')
    return 2

def menu_edit_notes():
    print()
    print('1. Сохранить изменения в заметке')
    print('2. Отмена')
    return 2