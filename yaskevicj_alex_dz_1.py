# 1 минута
one_minute = 60
# 1 час
one_hour = 3600
# 1 день
one_day = 86400
# 1 неделя
one_week = 604800


# запрос у пользователя длительности в секундах.
duration = int(input('длительность в секундах'))


# если введенные данные меньше минуты.
if duration < one_minute:
    print('{} секунд'.format(duration))


# если введенные данные меньше часа.
elif one_minute <= duration and one_hour > duration:
    minute = duration // one_minute
    second = duration % one_minute
    print('{} минут {} секунд'.format(minute, second))

# если введенные данные меньше суток.
elif duration >= one_hour and duration < one_day:
    hour = duration // one_hour
    duration = duration % one_hour
    minute = duration // one_minute
    second = duration % one_minute
    print('{} час {} минут {} секунд'.format(hour, minute, second))


# если введенные данные меньше недели.

elif duration >= one_day and duration < one_week:
    day = duration // one_day
    duration = duration % one_day
    hour = duration // one_hour
    duration = duration % one_hour
    minute = duration // one_minute
    second = duration % one_minute
    print('{} день {} час {} минуты {} секунды'.format(day, hour, minute, second))





# третье задание

for i in range(100):
    new_str=str(i+1)
    new_list = list(new_str)
    if int(new_list[-1])==1 and i+1!=11:
        print('{} процент'.format(i + 1))
    elif int(new_list[-1])>1 and int(new_list[-1])<= 4:
        if  i+1> 10 and i+1<= 14:
            print('{} процентов'.format(i + 1))
        else:
            print('{} процента'.format(i + 1))
    else:
        print('{} процентов'.format(i + 1))




# второе задание

cubes = [(x**3)+17 for x in range(100) if x%2 == 0]
print('список кубов нечётных чисел {}'.format(cubes))
my_numbers_sum = 0
my_numbers_sum_list_even_numbers =[]

for i in range(len(cubes)):
    my_str = str(cubes[i])
    my_list = list(my_str)


    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])


    for i in range(len(my_list)):
        my_numbers_sum = my_numbers_sum + my_list[i]


    if my_numbers_sum % 7 == 0:
        print('Cумму чисел, делящихся на 7 : ',my_numbers_sum)
        my_numbers_sum_list_even_numbers.append(my_numbers_sum)

print('числа делящихся на 7 : ',my_numbers_sum_list_even_numbers)
