""" BOW.py Bag of Words. """
import pandas as pd
import numpy as np
import string
import pprint
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer

documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?']

# Convert to lowercase and remove punctuation before tokenizing
lower_case_docs = [doc.lower() for doc in documents]
print(f'\nConverted to lowercase: {lower_case_docs}')

# str.translate() maps one set of characters to another. It uses the mapping function str.maketrans()
# Use the version of .maketrans() with 3 arguments to map the 3rd argument to None
no_punctuation_docs = [i.translate(str.maketrans('', '', string.punctuation)) for i in lower_case_docs]
print(f'Removed punctuations: {no_punctuation_docs}')

# Tokenize. Splits to whitespace by default
preprocessed_docs = [doc.split() for doc in no_punctuation_docs]
print(f'Tokenize: {preprocessed_docs}\n')

# Frequency analysis
freq_list = [Counter(word) for word in preprocessed_docs]
pprint.pprint(freq_list)

# Do the same with Scikit-learn
######################################
count_vector = CountVectorizer(documents)
#print(count_vector)
#
# Fit the with documents
count_vector.fit(documents)
#print(count_vector.get_feature_names())
print(f'\n Mapping of words to feature indices: {count_vector.vocabulary_}\n')
''' Solution. https://machinelearningmastery.com/prepare-text-data-machine-learning-scikit-learn/
'''
doc_array = count_vector.transform(documents).toarray()
print(doc_array)

df = pd.DataFrame(doc_array, columns=count_vector.get_feature_names())
print("\n", df.head())