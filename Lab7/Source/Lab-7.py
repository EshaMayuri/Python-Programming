import nltk
from nltk.corpus import stopwords, wordnet as wn
from nltk.tokenize import RegexpTokenizer, word_tokenize, sent_tokenize
from collections import Counter
import string

# Variable initializations
text_NoStopWords = ""
text_NoPunct = ""
words_NoVerbs = []
res = []
text_res = ""

# Step 1: Reading file
data = file('file1.txt').read()
# Fetching the stop words
stop = set(stopwords.words('english'))
# Step 2: Removing the stop words from the data
for i in data.lower().split():
    if i not in stop:
        text_NoStopWords = text_NoStopWords +' ' + i
print "-----------Data with no stop words-----------"
print text_NoStopWords
# Deleting puntuation marks from the text
punct = set(string.punctuation)
text_NoPunct = ''.join(x for x in text_NoStopWords if x not in punct)
print "-----------Data with no punctuation-----------"
print text_NoPunct
# Step 3 & 4: Removing verbs from the text by applying word tokenizing and POS
words = word_tokenize(text_NoPunct)
tokes_pos = nltk.pos_tag(words)
for i in tokes_pos:
    if 'VB' not in i[1]:
        words_NoVerbs.append(i[0])
print "-----------Data with no verbs-----------"
print words_NoVerbs
# Step 5 & 6: Fetching the top 5 most occurring words
counts = Counter(words_NoVerbs).most_common(5)
print "-----------Top 5 common words-----------"
print counts
# Steps 7 to 10: Concatenating and printing the statements containing the most frequent words
for top in counts:
    for sent in sent_tokenize(data.lower()):
        if sent not in text_res:
            if top[0] in word_tokenize(sent):
                text_res = text_res + sent
print "-----------Final text-----------"
print text_res

