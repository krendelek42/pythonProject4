"""Case-study #3 Text analysis
Developers:
Dokukina K. (40%), Nazirova E. (30%), Egorov E. (30%).

"""
from translate import Translator
text = input("Введите текст:")
from textblob import TextBlob
b = TextBlob(text)
language = b.detect_language()   
count_sentens = text.count('.')
count_words = text.count(' ') + 1  
if language == 'ru':
    gl_ru = list('уеыаоэяиёю')
    count_syllables = 0
    for i in text.lower():
        if i in gl_ru:
            count_syllables += 1     
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

if FRE> 80:
    print('Текст очень легко читается (для младших школьников).')
if FRE>50 and FRE< 80:
    print('Простой текст (для школьников).')
if FRE>25 and FRE< 50:
    print('Текст немного трудно читать (для студентов).')
if FRE<25 :
    print('Текст трудно читается (для выпускников ВУЗов).')

sentiment, subjectivity = b.sentiment if language == "en" else b.translate(to="en").sentiment                          
if b.sentiment.polarity > 0.5:
    sentiment = 'положительный'
elif b.sentiment.polarity < -0.5:
    sentiment = 'отрицательный'
else:
    sentiment = 'нейтральный'
subjectivity = subjectivity * 100                                                                                       

print ('Предложений:',count_sentens)
print ('Слов:',count_words)
print ('Слогов:',count_syllables)
print ('Средняя длина предложения в словах:',ASL)
print ('Средняя длина слова в слогах:',ASW)
print ('Индекс удобочитаемости Флеша:',FRE)
print('Тональность текста: ', sentiment)
print('Объективность: ', "%.1f" % subjectivity, '%', sep='')
