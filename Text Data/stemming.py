
from nltk.stem import PorterStemmer
ps = PorterStemmer()


sentence = "My mom is making eggs while dad is picking me up from volleyball training"

for word in sentence.split():
  print(ps.stem(word))