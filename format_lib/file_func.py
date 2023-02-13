import csv, datetime
from os import name
import check

delim_path = '\\' if name == 'nt' else '/'

def read_file(filename: str):
    dir = filename.split('/')
    check.check_dir(dir[0])
    check.check_file(dir[0] + delim_path + dir[1])
    result = []
    with open(dir[0] + delim_path + dir[1], 'r', encoding='utf-8') as data:
        csvreader = csv.reader(data, delimiter=';')
        for row in csvreader:
            result.append(tuple(row))
    return result

def add_file(filename: str,id: int,head: str,body: str):
    dir = filename.split('/')
    check.check_dir(dir[0])
    check.check_file(dir[0] + delim_path + dir[1])
    dt_now = datetime.datetime.now().strftime('%H:%M %m.%d.%Y')
    with open(dir[0] + delim_path + dir[1], 'a', encoding='utf-8') as data:
        csvwriter = csv.writer(data, delimiter = ";")
        csvwriter.writerow([id,dt_now,head,body])
        
def write_file(filename: str, data):
    dir = filename.split('/')
    check.check_dir(dir[0])
    check.check_file(dir[0] + delim_path + dir[1])
    dt_now = datetime.datetime.now().strftime('%H:%M %m.%d.%Y')
    with open(dir[0] + delim_path + dir[1], 'w', encoding='utf-8') as dataf:
        csvwriter = csv.writer(dataf, delimiter = ";")
        for row in data:
            csvwriter.writerow(row)