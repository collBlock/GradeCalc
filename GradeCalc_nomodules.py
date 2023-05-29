import math

numbers, count = input('Введите оценку и ее степень ').split()
count = int(count)

two, three, four, five = 0,0,0,0

def medium(two, three, four, five):
    return round(float((2*two + 3*three + 4*four + 5*five) / (two+three+four+five)), 4)

while numbers != 'end':
    if numbers ==   '2': two += count
    elif numbers == '3': three += count
    elif numbers == '4': four += count
    elif numbers == '5': five += count
    else: print('не знаю таких чисел')
    
    print('/'*5+'чтобы закончить ввод напишите end 1')
    numbers, count = map(str, input('Введите оценку и ее степень ').split())
    count = int(count)


print(f'\nЗапомнил, сейчас у тебя средний балл {medium(two, three, four, five)}')
hmm = float(input('Введите желаемый средний балл: '))

two_dream_temp, three_dream_temp, four_dream_temp, five_dream_temp = two, three, four, five
two_dream, three_dream, four_dream, five_dream = two, three, four, five


while medium(two_dream_temp, three_dream, four_dream_temp, five_dream_temp) <= hmm:
    three_dream += 1
    if three_dream > 15:
        three_dream = 0
        break
while medium(two_dream_temp, three_dream_temp, four_dream, five_dream_temp) <= hmm:
    four_dream += 1
    if four_dream > 20:
        four_dream = 0
        break
while medium(two_dream_temp, three_dream_temp, four_dream_temp, five_dream) <= hmm:
    if medium(two, three, four, five) == hmm: 
        break
    five_dream += 1
    if five_dream > 40:
        five_dream = 0
        break
    
    

now = {
    'Двоек': two,
    'Троек': three,
    'Четверток': four,
    'Пятёрок': five
    }
dream = {
    'Троек': max(three_dream-three,0),
    'Четверток': max(four_dream-four,0),
    'Пятёрок': max(five_dream-five,0)
}
print('\nИТОГИ')
print(f'\nСейчас {medium(two, three, four, five)}')
for key, value in now.items():
  print("{0}: {1}".format(key,value))

print(f'\nНужно до {hmm}')
for key, value in dream.items():
  print("{0}: {1}".format(key,value))