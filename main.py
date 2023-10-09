import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score



data = pd.read_csv('dataset.csv')

y = data[['pos']]
x = data[['val']]

vectorizer = TfidfVectorizer()
x_v = vectorizer.fit_transform(x)

classifier = MultinomialNB()
classifier.fit(x_v, y)

