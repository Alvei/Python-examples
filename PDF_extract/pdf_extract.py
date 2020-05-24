import PyPDF2
#import textract
import pandas as pd
import os
import logging
#from nltk.tokenize import word_tokenize
#from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
nltk.download('stopwords')

def _is_pdf(file_name=None) -> bool:
    # TODO: Must be a more detailed check
    if file_name[-3:].lower() != 'pdf':
        return False
    return True

def pdf2txt(filename: str) -> str:
    """ Extract the text from PDF. """
    # Open pdf as a binary
    if _is_pdf(filename) is None:
        logging.warning('Input file is not PDF.')
        return None

    pdf_obj = open(filename, 'rb')

    # pdfReader variable is a readable object that will be parsed
    pdfReader = PyPDF2.PdfFileReader(pdf_obj)

    # Determine the no. of pages
    num_pages = pdfReader.numPages
    print(f"Number of pages:{num_pages}")
    count = 0
    text = ""

    # Loop over all the pages
    while count < 2:
        page_obj = pdfReader.getPage(count)
        count += 1
        page_text = page_obj.extractText()
        print(f"\nPage {count}: {page_text}")
        text += page_text
    """
    if text !="":
        text = text
    else:
        text = textract.process(fileurl, method='tesseract', language='eng')

        """

    return text

users = input("Enter your Name: ")
path = "C:\\Users\\" + users.strip() + "\\Documents\\"
name = 'lease_ex.pdf'
filename = path + name
text = pdf2txt(filename)
# Break our text into individual words or sentences.
tokens = nltk.word_tokenize(text)
token_sentences = nltk.sent_tokenize(text)

# Punctuation we wish to clean.
punctuations = ['(',')',';',':','[',']',',', '~', "'"]

# Initialize the stopwords variable, which is a list of words like "The," "I," "and," etc. that don't hold much value as keywords.
stop_words = nltk.corpus.stopwords.words('english')

# List comprehension that only returns a list of words that are NOT IN stop_words and NOT IN punctuations.
keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
#print(f"\nkeywords:{keywords}")

print("\nRead the list:")
#for s in token_sentences:
#    print(f"{s}\n")