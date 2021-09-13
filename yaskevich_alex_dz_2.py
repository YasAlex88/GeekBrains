
''' Задача №1
Выяснить тип результата выражений:
15 * 3
15 / 3
15 // 2
15 ** 2
'''

print(type(15*3))
print(type(15/3))
print(type(15//2))
print(type(15**2))
print(type(15%2))


# задача №4


positions_names = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда Николай', 'директор Аэлита']

for i in positions_names:
    i=i.title()
    name = i.rpartition(' ')
    print(f'Привет, {name[-1]}!')


# задача № 5



price_list_product = [57.8, 46.51, 97, 7, 58.4, 34, 5, 1, 34.4, 89, 5.19, 69]
print(id(price_list_product))
price_list_product_format=[]
# A Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
print('Пункт A')


for i in price_list_product:

    if type(price_list_product[price_list_product.index(i)]) == float:
        meaning = str(price_list_product[price_list_product.index(i)])
        r, kk=meaning.split('.')
        r=int(r)
        kk=int(kk)
        if r <=9:
            if kk <= 9:
                price_list_product_format.append(f'«0{r} руб 0{kk} коп»')
            else:
                price_list_product_format.append(f'«0{r} руб {kk} коп»')
        else:
            if kk<=9:

                price_list_product_format.append(f'«{r} руб 0{kk} коп»')

            else:
                price_list_product_format.append (f'«{r} руб {kk} коп»')

    elif type(price_list_product[price_list_product.index(i)]) == int:
        r = price_list_product[price_list_product.index(i)]
        kk = 00
        if r <= 9:

            price_list_product_format.append(f'«0{r} руб 0{kk} коп»')
        else:

            price_list_product_format.append(f'«{r} руб 0{kk} коп»')




price_list_product = [57.8, 46.51, 97, 7]
print(price_list_product_format)
print(id(price_list_product))


# B Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
print('Пункт B')
price_list_product_format.sort()
print(price_list_product_format)
print(id(price_list_product))

# C Создать новый список, содержащий те же цены, но отсортированные по убыванию.
print(' Пункт C')
price_list_product_format = price_list_product_format[::-1]
print(price_list_product_format)
print(id(price_list_product_format))



# D Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
print(' Пункт D')
print(price_list_product_format[:5])



# Задача № 2

announced_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(announced_list))


announced_list =announced_list[::-1]

for i in announced_list:
    if announced_list[announced_list.index(i)].isdigit() == True and announced_list[announced_list.index(i)].startswith('"') == False:
        announced_list.insert(announced_list.index(i)+1, '"')
    elif announced_list[announced_list.index(i)].isdigit() == False and announced_list[announced_list.index(i)].startswith('+') == True:
        announced_list.insert(announced_list.index(i) + 1, '"')

announced_list =announced_list[::-1]

for i in announced_list:
    if announced_list[announced_list.index(i)].isdigit() == True and announced_list[announced_list.index(i)].startswith('"') == False:
        announced_list.insert(announced_list.index(i)+1, '"')
        if len(i) == 1:
            announced_list[announced_list.index(i)] = '0'+i

    elif announced_list[announced_list.index(i)].isdigit() == False and announced_list[announced_list.index(i)].startswith('+') == True:
        announced_list.insert(announced_list.index(i) + 1, '"')

message= ' '.join(announced_list)
print(message)