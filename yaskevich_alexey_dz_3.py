''' Понял и успел сделать только эти задания'''

# задание №5
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
number_of_jokes = int(input("Сколько шуток Вы хотите получить:"))
flag = input("Если  хотите только оригинальные шутки, то введите '1', если нет, то введите любое числоо:")


def get_jokes():
    for i in range(number_of_jokes):
        if flag == 1:
            from random import choice
            word_1 = choice(nouns)
            word_3 = choice(adjectives)
            word_2 = choice(adverbs)
            print(f'Ваша шутка:{word_1} {word_2} {word_3}')
        else:
            from random import choice
            word_1 = choice(nouns)
            nouns.remove(word_1)
            word_3 = choice(adjectives)
            adjectives.remove(word_3)
            word_2 = choice(adverbs)
            adverbs.remove(word_2)
            print(f'Ваша шутка:{word_1} {word_2} {word_3}')


get_jokes()

# задание № 3

names = {}


def thesaurus(*args):
    for i in range(len(args)):
        word = args[i]
        if word[0] in names.keys():
            names[word[0]] = names[word[0]] + [word]
        else:
            names[word[0]] = [word]
    print(names)


thesaurus("Иван", "Мария", "Петр", "Илья")


# задание № 1

words = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
         'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate():
    word = input("Введите слово от one до ten, чтобы перевести на русский язык:")
    word.lower()
    print(f'Переводом слова: {word}, будет: {words.get(word)}')


num_translate()


# задание № 2


words = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
         'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate_adv():
    word = input("Введите слово от one до ten, чтобы перевести его на русский язык:")
    word_test = str(word)
    word = word.lower()
    if word_test.istitle():
        b = str(words.get(word))
        print(f'Переводом слова: {word.title()}, будет: {b.title()}')
    else:
        print(f'Переводом слова: {word}, будет: {words.get(word)}')


num_translate_adv()