# пункт А

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

lst = []

from random import randint

while len(lst) < 3:
    x = randint(0, len(my_favorite_songs) -1)
    if x not in lst:
        lst.append(x)
print(lst)

nlst = []
for y in lst:
    nlst.append(my_favorite_songs[y])
print(nlst) 
total_sum = 0
for name , time in nlst:

    total_sum += time

    time = nlst[0][1] + nlst[1][1] + nlst[2][1] 
print(f'время звучания трех случайных песен = {time} минут')
print(f'время звучания трех случайных песен = {total_sum} минут')

# Пункт В

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

from random import choice

ran_dict = []
i = 0
while i < 3:
    key = choice(list(my_favorite_songs_dict.items()))
    ran_dict.append(key)
    i += 1
#print(ran_dict)
ran_dict_1 = dict(ran_dict)
print(ran_dict_1)
sum_time = 0
for a in ran_dict_1:
    sum_time += ran_dict_1[a]

print(f'время звучания трех случайных песен' , '-' , {sum_time})
