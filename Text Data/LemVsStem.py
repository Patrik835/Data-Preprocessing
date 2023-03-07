import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
#nltk.download('wordnet')
ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

e_words= ["wait", "waiting", "waited", "waits"]

print("Stemming")
for w in e_words:
    rootWord=ps.stem(w)
    print(rootWord)

print("Lemmatization")
for w in e_words:
    rootWord = lemmatizer.lemmatize(w)
    print(rootWord)

print(lemmatizer.lemmatize("caring", pos='n'))
print(lemmatizer.lemmatize("running", pos='v'))
print(lemmatizer.lemmatize("ate", pos='v'))

