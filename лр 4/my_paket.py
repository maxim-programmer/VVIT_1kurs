def qwerty(a,b):
    return a + b
def chisla(x,y,z):
    if z == '+':
        return x + y
    elif z == '-':
        return x - y
    elif z == '*':
        return x * y
    elif z == '/':
        return x / y
    else:
        return 'Неизвестная операция'
def info():
    print('''В данном пакете представлены такие модули:
    1) qwerty - конкатенация двух строк
    2) chisla - операции(+,-,*,/) с двумя числами''')