# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
a = [4,6,2,1,9,63,-134,566]         #-> max = 566, min = -134
a_1 = [-52, 56, 30, 29, -54, 0, -110] #-> min = -110, max = 56
a_2 = [42, 54, 65, 87, 0]             #-> min = 0, max = 87
a_3 = [5]                             #-> min = 5, max = 5


def minimum(data):
    i = 0
    l = len(data)
    while i < l - 1:
        x = i
        y = i + 1
        while y < l:
            if data[y] < data[x]:
                x = y
            y +=1
        data[i], data[x] = data[x], data[i]
        i += 1
    print(data)   
    print(f'min = {data[0]} , max = {data[-1]}')

minimum(a_1)





