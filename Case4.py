"""Case-study #3 Text analysis
Developers:
Dokukina K. (%), Nazirova E. (%), Egorov E. (%).

"""
from translate import Translator
text = input("Введите текст:")
from textblob import TextBlob #чтобы установить TextBlob вставите в терминал (он находится если что внизу пайчарма) это "pip install -U textblob" и (после того как он загрузится) это потом "python -m textblob.download_corpora"
b = TextBlob(text)
language = b.detect_language()   # если язык русский - ru, английский - en
count_sentens = text.count('.')
count_words = text.count(' ') + 1  #думаю, количество слов по пробелам можно посчитать (могу ошибаться), но вроде работает все
if language == 'ru':
    gl_ru = list('уеыаоэяиёю')
    count_syllables = 0
    for i in text.lower():
        if i in gl_ru:
            count_syllables += 1     # подсчет гласных я сделала через цикл, думаю так можно, надеюсь, никто не будет против
else:
    gl_en = list('aeiouy')
    count_syllables = 0
    for i in text.lower():
        if i in gl_en:
            count_syllables += 1
ASL = count_words/count_sentens
ASW = count_syllables/count_words
if language == 'ru':
    FRE = 206.835 - (1.3 * ASL) - (60.1 * ASW)
else:
    FRE = 206.835 - (1.015 * ASL) - (84.6 * ASW)
sentiment, subjectivity = b.sentiment if language == "en" else b.translate(to="en").sentiment                           #calculating sentiment and subjectivity
if b.sentiment.polarity > 0.5:
    sentiment = 'положительный'
elif b.sentiment.polarity < -0.5:
    sentiment = 'отрицательный'
else:
    sentiment = 'нейтральный'
subjectivity = subjectivity * 100                                                                                       #subjectivity to percents
# сюда напишите свою часть работы
# сначала про удобночитаемость потом про тональность. Ниже добавите print, следуя последовательности работы
print ('Предложений:',count_sentens)
print ('Слов:',count_words)
print ('Слогов:',count_syllables)
print ('Средняя длина предложения в словах:',ASL)
print ('Средняя длина слова в слогах:',ASW)
print ('Индекс удобочитаемости Флеша:',FRE)
print('Тональность текста: ', sentiment)
print('Объективность: ', "%.1f" % subjectivity, '%', sep='')
 # В общем, осталось дописать, чтобы после выявления индекса удобночитаемости Флеша, он выводил че за текст
 #  (легко читается, средне, трудно). Это есть в примере работы у Минака. Индекс расположен в диапазоне 0 - 100
 # Минак делит на 4 части диапазон, текста, какие нужно писать, есть в "описании предметной области"
 # Насчет английского текста хз, вроде диапазон сохраняется
 # В общем, это нужно все красиво оформить

 # Теперь про тональность. Штука, которая ее считывает есть в тексблобе. Я, честно, не смотрела ее и не разбиралась даже че с ней делать

 # Про удобночитаемость может сделать Ева, про тональность Ефим

 # Проверьте плиз чтобы все работало, и ваша программа, и моя. Как сделаете - напишите
 # не забывайте коммитить на англ. Сохраняйте все в своей ветке