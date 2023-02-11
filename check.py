def input_data(nums_menu: int):
    flag_input_ok = False
    while not flag_input_ok:
        try:
            num = int(input(f'Введите пункт меню от 1 до {nums_menu}: '))
            if (num > 0 and num <= nums_menu):
                flag_input_ok = True
                return num
            else:
                raise ValueError()
        except ValueError:
            print("Введите целое число из указанного диапазона!")