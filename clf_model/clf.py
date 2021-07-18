import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.linear_model import SGDClassifier

# Initial data
data = pd.read_csv(r'C:\Users\Artyom\PycharmProjects\telegram_bot\clf_model\train.txt', encoding='ISO-8859-1', sep=';',
                   names=['text', 'emotion'])
X = data['text']
y = data['emotion']

# Creating pipeline to vectorize and transform data
text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', SGDClassifier(penalty='l1', alpha=0.0001, n_iter_no_change=10, random_state=10))
])

text_clf.fit(X, y)
