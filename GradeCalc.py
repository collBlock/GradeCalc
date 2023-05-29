from termcolor import colored
import time

# Выводим стартовое сообщение с красивым форматированием
print(colored("""
  ______                            __             ______             __                                
 /      \                          |  \           /      \           |  \                               
|  $$$$$$\  ______   ______    ____| $$  ______  |  $$$$$$\  ______  | $$  _______                      
| $$ __\$$ /      \ |      \  /      $$ /      \ | $$   \$$ |      \ | $$ /       \                     
| $$|    \|  $$$$$$\ \$$$$$$\|  $$$$$$$|  $$$$$$\| $$        \$$$$$$\| $$|  $$$$$$$                     
| $$ \$$$$| $$   \$$/      $$| $$  | $$| $$    $$| $$   __  /      $$| $$| $$                           
| $$__| $$| $$     |  $$$$$$$| $$__| $$| $$$$$$$$| $$__/  \|  $$$$$$$| $$| $$_____                      
 \$$    $$| $$      \$$    $$ \$$    $$ \$$     \ \$$    $$ \$$    $$| $$ \$$     \                     
  \$$$$$$  \$$       \$$$$$$$  \$$$$$$$  \$$$$$$$  \$$$$$$   \$$$$$$$ \$$  \$$$$$$$                     
                                                         
                                                                script by collBlock                                                                                                                                                                                       

Добро пожаловать в приложение для расчета необходимого количества оценок для достижения желаемого среднего балла! 
""", 'magenta'))

# Запрашиваем у пользователя оценку и ее степень
numbers, count = input(colored('Введите оценку и ее степень: ', 'blue')).split()
count = int(count)

# Задаем переменные для всех оценок
two, three, four, five = 0, 0, 0, 0

# Определяем функцию для расчета среднего балла
def medium(two, three, four, five):
    return round(float((2*two + 3*three + 4*four + 5*five) / (two+three+four+five)), 4)

# Создаем цикл для ввода оценок и их количества
while numbers != 'end':
    if numbers == '2':
        two += count
    elif numbers == '3':
        three += count
    elif numbers == '4':
        four += count
    elif numbers == '5':
        five += count
    else:
        print(colored('Не знаю таких оценок', 'red'))
    
    # Запрашиваем у пользователя, хочет ли он закончить ввод
    numbers, count = input(colored('Продолжай ввод, чтобы закончить ввод напишите "end 1": ', 'blue')).split()
    count = int(count)

print('******************')
# Рассчитываем и выводим текущий средний балл пользователя
current_medium = medium(two, three, four, five)
print(colored(f'Запомнил, сейчас у тебя средний балл {current_medium}', 'yellow'))

# Запрашиваем желаемый средний бал пользователся
hmm = float(input(colored('Введите желаемый средний балл: ', 'blue')))

# Задаем временные переменные для каждой оценки
two_dream_temp, three_dream_temp, four_dream_temp, five_dream_temp = two, three, four, five
two_dream, three_dream, four_dream, five_dream = two, three, four, five

# Создаем циклы для расчета количества оценок, которое нужно получить пользователю для достижения желаемого среднего балла
while (medium(two_dream_temp, three_dream, four_dream_temp, five_dream_temp) <= hmm) and (three_dream <= 15):
    if current_medium > 3:
        three_dream = 0
        break
    three_dream += 1

while (medium(two_dream_temp, three_dream_temp, four_dream, five_dream_temp) <= hmm) and (four_dream <= 20):
    if current_medium > 4:
        four_dream = 0
        break
    four_dream += 1

while (medium(two_dream_temp, three_dream_temp, four_dream_temp, five_dream) <= hmm) and (five_dream <= 40) and (medium(two, three, four, five) != hmm):
    five_dream += 1

# Создаем словари с текущими и желаемыми количествами оценок
now = {'Двоек': two, 'Троек': three, 'Четверток': four, 'Пятёрок': five}
dream = {'Троек': max(three_dream-three, 0), 'Четверток': max(four_dream-four, 0), 'Пятёрок': max(five_dream-five, 0)}

# Выводим итоговую информацию
print(colored('\nИТОГИ', 'yellow', attrs=['underline', 'bold']))
print(colored(f'Сейчас у тебя средний балл: {current_medium}', 'yellow'))
for key, value in now.items():
    print(colored("{0}: {1}".format(key, value), 'white'))

print(colored(f'\nНужно получить до {hmm}:', 'yellow'))
for key, value in dream.items():
    print(colored("{0}: {1}".format(key, value), 'white'))


time.sleep(30)  