import os, csv, datetime

def input_data_menu(nums: int, text: str):
    flag_input_ok = False
    while not flag_input_ok:
        try:
            num = int(input(f'{text}: '))
            if (num > 0 and num <= nums):
                flag_input_ok = True
                return num
            else:
                raise ValueError()
        except ValueError:
            print("Введено неверное число!")

def input_data(text: str):
    flag_input_ok = False
    while not flag_input_ok:
        try:
            num = int(input(f'{text}: '))
            flag_input_ok = True
            return num
        except ValueError:
            print("Введено неверное число!")
            
def check_dir(directory: str):
    if (not os.path.exists(directory)):
        os.mkdir(directory)

def check_file(filename: str):
    if (not os.path.isfile(filename)):
        with open(filename, 'a') as data:
            csvwriter = csv.writer(data, delimiter = ";")
            csvwriter.writerow(["id","Date","Time","Header","Body"])
            
def check_note_id(data, id):
    for i in range(1, len(data)):
        if (id == int(data[i][0])):
            return True
    print("Заметки с таким id не существует")
    print()
    return False

def check_date():
    isValid=False
    while not isValid:

        userIn = input("Введите дату(в формате DD.MM.YYYY): ")
        try:
            if (not userIn == ''):
                d = datetime.datetime.strptime(userIn, "%d.%m.%Y")
                isValid=True
            else:
                d = ''
                isValid=True
        except:
            print ("Введен неверный формат даты, повторите!\n")
    return d