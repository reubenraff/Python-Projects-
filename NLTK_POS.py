import nltk
from nltk import pos_tag
from collections import Counter
string = "I Think therefore I am"
toks = string.split()
Parts_speech = pos_tag(toks)
#print(Parts_speech)
counter = Counter(tag for word, tag in Parts_speech)
print(counter)
