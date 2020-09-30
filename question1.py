

def f(a):
    num1 = 0
    num2 = 1
    series = 0
    even_nros = []
    while 1:
        num1 = num2
        num2 = series

        if (series % 2 == 0):
            even_nros.append(series)

        series = num1 + num2

        if (len(even_nros) == a):
            break
    for i in range(len(even_nros)):
        print(even_nros[i], end=' ')

f(4)
    


