
import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.util import ngrams
from collections import Counter
from nltk import pos_tag, ne_chunk
import numpy

#word_tokenize, wordpunct_tokenize,

words = file('tesst.txt').read()
print words

print "---------wordnet--------------"
for syns in wn.synsets('Computer'):
    for l in syns.lemmas():
        print l.name()

print "--------Sentence Tokenization-------------"
# nltk.download('punkt')
test_text = sent_tokenize(words)
print test_text

print "--------Word Tokenization-------------"
tokens = nltk.word_tokenize(words)
print tokens

print  "----POS-----"
print pos_tag(tokens)

print "------Steming----"
stemmer = PorterStemmer()
print(stemmer.stem('Programming'))

print "------Lemmatization----"
lemmatize = WordNetLemmatizer()
print lemmatize.lemmatize('Programming', pos='v')


print "------Trigrams----"
token = nltk.word_tokenize(words)
trigrams = ngrams(token,3)
print Counter(trigrams)

print "------Named Entity----"
# nltk.download('all')
print ne_chunk(pos_tag(wordpunct_tokenize(words)))