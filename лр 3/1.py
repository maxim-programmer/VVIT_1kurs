import time
def fayl():
    x = input('Вывести сразу или построчно? (сразу/построчно): ')
    if x == 'сразу':
        with open('example.txt', 'r') as file:
            content = file.read()
            print(content)
    elif x == 'построчно':   
        with open('example.txt', 'r') as file:
            for line in file:
                print(line.rstrip('\n'))
                time.sleep(1)
fayl()
