def read_file(namefile: str):
    result = ''
    with open(namefile, 'r', encoding='utf-8') as data:
        for n, line in enumerate(data, 1):
            result += line
    return result