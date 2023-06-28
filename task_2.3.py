# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!


def switch_it_up(x):

    b = {0 : 'zero',
         1 :'one', 
         2 : 'two', 
         3: 'three', 
         4 :'for', 
         5 :'five', 
         6 : 'six', 
         7 :'seven', 
         8 : 'eigt', 
         9 : 'nine',
         }
    
    return b[x]
    
    
x = int(input('введите число от 0 до 9 '))
    
print(f'switch_it_up {x} - {switch_it_up(x)}')

        
    
    
               
