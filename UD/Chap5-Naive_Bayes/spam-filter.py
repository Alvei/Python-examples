""" Spam-filter.py
    https://towardsdatascience.com/machine-learning-nlp-text-classification-using-scikit-learn-python-and-nltk-c52b92a7c73a
    https://medium.com/@awantikdas/a-comprehensive-naive-bayes-tutorial-using-scikit-learn-f6b71ae84431
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

filename = 'SMSSpamCollection'
cols =  ['label', 'sms_message']
df = pd.read_table(filename, header=None, names=cols)
print(f"\nLoading and pre-process the training set {filename}")

# Preprocess
###############################################
labels_to_binary =  {'ham':0, 'spam':1}
df['label'] = df.label.map(labels_to_binary)

X_train, X_test, y_train, y_test = train_test_split(df['sms_message'],
                                                    df['label'],
                                                    random_state=1)

print(f'Number of rows in the total set: {df.shape[0]}')
print(f'Number of rows in the training set: {X_train.shape[0]}')
print(f'Number of rows in the test set: {X_test.shape[0]}')

# Create the model
##########################################

# Instantiate the CountVectorizer method
count_vector = CountVectorizer()

# Fit the training data and then return the matrix. fit_transform() is simply chaining .fit() and .transform()
training_data = count_vector.fit_transform(X_train)

# Transform testing data and return the matrix. Note we are not fitting the testing data into the CountVectorizer()
testing_data = count_vector.transform(X_test)

# Train the spam filter using naive_bayes
naive_bayes = MultinomialNB()
naive_bayes.fit(training_data, y_train)

# Check for accuracy
######################
predictions = naive_bayes.predict(testing_data)
print(f"\nCreating the spam model - Naive Bayes")
print(f'Accuracy score: {accuracy_score(y_test, predictions):.3f}')
print(f'Precision score: {precision_score(y_test, predictions):.3f}')
print(f'Recall score: {recall_score(y_test, predictions):.3f}')
print(f'F1 score: {f1_score(y_test, predictions):.3f}\n')

# Use the model
################
emails = ['Get some viagra money quick discount fast WINNER!! URGENT!',
          'Hi it has been a long time',
          'URGENT!!!']

email_transforms = count_vector.transform(emails)
spam_predictions = naive_bayes.predict(email_transforms)

label_predictions = ['ham' if x==0 else 'spam' for x in spam_predictions ]

for email, pred in zip(emails, label_predictions):
    print(f"{email} is => {pred}")

