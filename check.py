import os
import csv

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
            csvwriter.writerow(["id","Date","Header","Body"])
            
def check_note_id(data, id):
    for i in range(1, len(data)):
        if (id == int(data[i][0])):
            return True
    print("Заметки с таким id не существует")
    print()
    return False