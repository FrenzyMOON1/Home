print("Если вы хотите завершить программу, то напишите команду - stop")
d = 0
h = 0


def my_func(a):
    d = a
    if d == "stop":
        return "END"
    else:
        c = [int(x) for x in a.split()]
        b = sum(c)
        global h
        h = h + b
        return h


while d != "stop":
    print('Введите элементы через пробел: ', my_func(input()))
