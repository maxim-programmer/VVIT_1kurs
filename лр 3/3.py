import time
def fayl():
    y = input('Напишите имя файла, который хотите открыть: ')
    x = input('Вывести сразу или построчно? (сразу/построчно): ')
    try:
        if x == 'сразу':
            with open(f'{y}.txt', 'r') as file:
                content = file.read()
                print(content)
        elif x == 'построчно':   
            with open(f'{y}.txt', 'r') as file:
                for line in file:
                    print(line.rstrip('\n'))
                    time.sleep(1)
    except FileNotFoundError:
        print(f'Файл под именем "{y}" не найден.')
fayl()
