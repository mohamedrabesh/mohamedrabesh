import pandas as pd
import sklearn
print("scikit-learn version:", sklearn.__version__)
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('spam.csv', encoding='latin-1')


if 'label' not in df.columns or 'message' not in df.columns:
    # For example, some versions have extra unnamed columns
    df = df[['v1', 'v2']]
    df.columns = ['label', 'message']


df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})


X = df['message']
y = df['label_num']

vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)


model = MultinomialNB()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
