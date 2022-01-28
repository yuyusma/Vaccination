import pandas as pd
import random
import numpy as np
import re
import nltk
import nltk.corpus
import string
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')


# читаем csv:
df = pd.read_csv('data.csv', delimiter = ';')
df.head(10)

# переводим значения в столбце в строку:
df['Text'] = df['Text'].astype(str)

# Функция для очистки текста 
def clean_text(text):
    # приводим текст к нижнему регистру
    text = text.lower()
    # создаем регулярное выражение для удаления лишних символов
    regular = r'[\*+\#+\№\"\-+\+\=+\?+\&\^\.+\;\,+\>+\(\)\/+\:\\+]'
    # регулярное выражение для замены ссылки на "URL"
    regular_url = r'(http\S+)|(www\S+)|([\w\d]+www\S+)|([\w\d]+http\S+)'
    # удаляем лишние символы
    text = re.sub(regular, '', text)
    # заменяем ссылки на "URL"
    text = re.sub(regular_url, r'URL', text)
    # заменяем числа и цифры на ' NUM '
    text = re.sub(r'(\d+\s\d+)|(\d+)',' NUM ', text)
    # удаляем лишние пробелы
    text = re.sub(r'\s+', ' ', text)
    # возвращаем очищенные данные
    return text
 
# создаем список для хранения преобразованных данных 
processed_text = []
# загружаем стоп-слова для русского языка
stop_words = stopwords.words('russian')
# инициализируем лемматайзер 
lemmatizer = WordNetLemmatizer()
 
# для каждого сообщения text из столбца data['Text']
for text in df['Text']:
    # cleaning 
    text = clean_text(text)   
    # tokenization
    text = word_tokenize(text)       
    # удаление стоп-слов
    text = [word for word in text if word not in stop_words]     
    # лемматизация
    text = [lemmatizer.lemmatize(w) for w in text]
     
    # добавляем преобразованный текст в список processed_text
    processed_text.append(text)
 
# Сохраняем результат преобразования в новой колонке 'Processed_text'
df['Processed_text'] = processed_text

# Сохраняем таблицу с преобразованным текстом

df.to_csv('new.csv', index=False, sep=";")
df.to_excel('new3.xlsx')




