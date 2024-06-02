# -*- coding: utf-8 -*-
"""SpamFilter.ipynb

# Treść zadania:

Tematem projektu będzie napisanie modelu filtru spamowego wykorzystując do tego celu dostępne przykładowe dane: https://www.kaggle.com/datasets/jerryanggara6/spam-filter-dataset.

Podstawowym założeniem jest korzystanie z modułów sparka do wczytywania, modyfikacji i manipulacji danymi. Filtr spamu trzeba zaimplementować za pomocą przetwarzania języka naturalnego zwanym analiza sentymentów. 

Proces tworzenia:
- oczysznienie danych i podzielenie na dwie klasy (spam i nie spam), tokenizacja danych,
- Stworzenie tzw. model worka słów czyli modyfikacja tekstu na numeryczny wektor cech,
- Zmniejszenie wagi mniej istotnym słowom,
- Przygotowanie modeli (przykładowo regresja logistyczna, naiwny klasyfikator Bayesa), 
- Podział na zbiór treningowy i testowy (kroswalidacja)
- Ocena jakości modelu 

Projekt zamiera możliwość przetestowania modelu (wpisanie własnego tekstu i sprawdzenie czy jest to spam czy nie).
"""

!pip install pyspark py4j

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.feature import Tokenizer, StopWordsRemover

import seaborn as sns
import matplotlib.pyplot as plt
import time

"""# Wczytanie danych

## Opis danych
Zbiór danych uzyty do badania filtru antyspamowego to kompleksowa kolekcja informacji, które służą do szkolenia algorytmów stosowanych w filtrach antyspamowych. W jego skład wchodzi zwykle szeroki zakres wiadomości e-mail, z których niektóre zostały oznaczone jako spam, a inne są legalnymi.


Podział danych na kategorie:
* 'ham': 87%
* 'spam1': 3%

Ilość unikalnych wartości: 5157

# Przygotowanie danych

## Tworzenie sesji
"""

spark = SparkSession.builder.appName('antyspam').getOrCreate()

"""## Wczytanie danych z pliku CSV"""

data_path = "/content/drive/MyDrive/Colab Notebooks/spam.csv"
df = spark.read.option("header", "true").csv(data_path)
df.show(10)

"""## Oczyszczanie danych"""

cleaned_df = df.select(col("Category").alias("label"), col("Message").alias("text"))

"""## Podział danych na dwie kategorię: spam i false-positive('ham')"""

cleaned_df = cleaned_df.filter((col("label") == "spam") | (col("label") == "ham"))

"""## Tokenizacja tekstu"""

tokenizer = Tokenizer(inputCol="text", outputCol="words")
words_df = tokenizer.transform(cleaned_df)

"""## Usunięcie stop words"""

remover = StopWordsRemover(inputCol="words", outputCol="filtered_words")
filtered_words_df = remover.transform(words_df)

"""## Wyświetlenie przetworzonych danych"""

filtered_words_df.show()

"""# Budowa modelu worka"""

from pyspark.ml.feature import CountVectorizer
from pyspark.ml.classification import LogisticRegression, NaiveBayes
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark.ml.feature import StringIndexer

"""## Tworzenie modelu:"""

cv = CountVectorizer(inputCol="filtered_words", outputCol="features")
cv_model = cv.fit(filtered_words_df)
vectorized_df = cv_model.transform(filtered_words_df)

"""## Podział danych na zbiór treningowy i testowy"""

(train_data, test_data) = vectorized_df.randomSplit([0.8, 0.2], seed=42)

"""# Inicjalizacja modeli klasyfikacji"""

lr = LogisticRegression(labelCol="label", featuresCol="features")
nb = NaiveBayes(labelCol="label", featuresCol="features")

"""## Trenowanie modeli"""

indexer = StringIndexer(inputCol="label", outputCol="label_index")
indexed_train_data = indexer.fit(train_data).transform(train_data)

"""## Ocena wydajności modelu regresji logistycznej

"""

lr_predictions = lr_model.transform(indexed_train_data)
lr_predictionAndLabels = lr_predictions.select("prediction", "label_index").rdd
lr_metrics = MulticlassMetrics(lr_predictionAndLabels)
print("Logistic Regression Accuracy: {:.2f}".format(lr_metrics.accuracy))

"""## Trenowanie modelu naiwnego klasyfikatora Bayesa"""

nb_model = nb.fit(indexed_train_data, {nb.labelCol: "label_index"})

"""## Ocena wydajności modelu naiwnego klasyfikatora Bayesa"""

nb_predictions = nb_model.transform(indexed_train_data)
nb_predictionAndLabels = nb_predictions.select("prediction", "label_index").rdd
nb_metrics = MulticlassMetrics(nb_predictionAndLabels)
print("Naive Bayes Accuracy: {:.2f}".format(nb_metrics.accuracy))

plt.imshow(lr_confusion_matrix, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Logistic Regression Confusion Matrix')
plt.colorbar()
tick_marks = np.arange(2)
plt.xticks(tick_marks, ['ham', 'spam'], rotation=45)
plt.yticks(tick_marks, ['ham', 'spam'])
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()

"""# Macierze pomyłek dla wybranych modeli regresji

## Tworzenie macierzy pomyłek dla modelu regresji logistycznej
"""

lr_predictionAndLabels = lr_predictions.select("prediction", "label_index").rdd
lr_metrics = MulticlassMetrics(lr_predictionAndLabels)

lr_confusion_matrix = lr_metrics.confusionMatrix().toArray()

"""## Wyświetlenie macierzy pomyłek dla modelu regresji logistycznej"""

plt.imshow(lr_confusion_matrix, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Logistic Regression Confusion Matrix')
plt.colorbar()
tick_marks = np.arange(2)
plt.xticks(tick_marks, ['ham', 'spam'], rotation=45)
plt.yticks(tick_marks, ['ham', 'spam'])
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()

"""## Tworzenie macierzy pomyłek dla modelu naiwnego klasyfikatora Bayesa"""

nb_confusion_matrix = nb_metrics.confusionMatrix().toArray()

"""## Wyświetlenie macierzy pomyłek modelu naiwnego klasyfikatora Bayesa"""

import numpy as np

plt.imshow(nb_confusion_matrix, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Naive Bayes Confusion Matrix')
plt.colorbar()
tick_marks = np.arange(2)
plt.xticks(tick_marks, ['ham', 'spam'], rotation=45)
plt.yticks(tick_marks, ['ham', 'spam'])
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()

"""# Ocena wydajności modeli"""

from pyspark.mllib.evaluation import MulticlassMetrics

# Predykcje i etykiety dla danych testowych
predictions_and_labels = lr_predictions.select("prediction", "label_index").rdd  # Dla modelu regresji logistycznej
# lub
predictions_and_labels = nb_predictions.select("prediction", "label_index").rdd  # Dla modelu naiwnego klasyfikatora Bayesa

# Tworzenie obiektu MulticlassMetrics
metrics = MulticlassMetrics(predictions_and_labels)

# Obliczanie metryk
accuracy = metrics.accuracy
precision = metrics.precision(label=1.0)  # dla etykiety "spam"
recall = metrics.recall(label=1.0)        # dla etykiety "spam"
f1_score = metrics.fMeasure(label=1.0)    # dla etykiety "spam"

# Wyświetlenie wyników
print("Accuracy: {:.2f}".format(accuracy))
print("Precision: {:.2f}".format(precision))
print("Recall: {:.2f}".format(recall))
print("F1-score: {:.2f}".format(f1_score))

"""## Funkcja do przetetstowania modelu na podstawie przykładowych zdań"""

from pyspark.ml.feature import Tokenizer
from pyspark.ml import PipelineModel

def predict_spam_or_ham(model, text):
    # Tworzenie DataFrame z wprowadzonym tekstem
    input_text_df = spark.createDataFrame([(text,)], ["text"])

    # Tokenizacja tekstu
    tokenizer = Tokenizer(inputCol="text", outputCol="words")
    input_text_df = tokenizer.transform(input_text_df)

    # Usunięcie stop words
    input_text_df = remover.transform(input_text_df)

    # Przekształcenie słów na wektor cech
    input_text_df = cv_model.transform(input_text_df)

    # Przewidywanie etykiety za pomocą wczytanego modelu
    prediction = model.transform(input_text_df)

    # Wyświetlenie wyniku predykcji
    result = prediction.select("prediction").collect()[0]
    if result.prediction == 1.0:
        print("Wprowadzony tekst jest uznany za SPAM.")
    else:
        print("Wprowadzony tekst jest uznany za nie-SPAM.")

"""### Przykładowe wywołania funkcji:"""

test_text = "500 New Mobiles from 2004, MUST GO! Txt: NOKIA to No: 89545 & collect yours today!From ONLY ÂŁ1 www.4-tc.biz 2optout 087187262701.50gbp/mtmsg18"
predict_spam_or_ham(lr_model, test_text)  # lr_model to wczytany wcześniej model regresji logistycznej

test_text = "Congratulations! You've won a $1000 gift card. Click here to claim now."
predict_spam_or_ham(lr_model, test_text)

test_text = 'Urgent! You have won a 1 week FREE membership in our £100,000 Prize Jackpot! Txt the word: CLAIM to No: 81010 T&C www.dbuk.net LCCLTD POBOX 4403LDNW1A7RW18'
predict_spam_or_ham(lr_model, test_text)

test_text = 'How wonderful you are'
predict_spam_or_ham(lr_model, test_text)