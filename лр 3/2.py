def fayl():
    x = input('Введите текст: ')
    file = open('user_input.txt', 'a')
    n = file.write('\n' + x)
    file.close()
    file = open('user_input.txt', 'r')
    content = file.read()
    print(content)
fayl()
