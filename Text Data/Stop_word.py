#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

sentence = "Your shoes are cool!"

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(sentence)

filtered_sentence = [w for w in word_tokens if not w in stop_words]
print(filtered_sentence)