import nltk

text = "This is Sofia's phone, isn't it?"

print(text)

#tockenizing by white space
tokenizer = nltk.tokenize.WhitespaceTokenizer()
print("By white space ", tokenizer.tokenize(text))

#By punctuation

tokenizer = nltk.tokenize.WordPunctTokenizer()
print("By Punctuation ", tokenizer.tokenize(text))


#By set of rules
tokenizer = nltk.tokenize.TreebankWordTokenizer()
print("By Rules ", tokenizer.tokenize(text))


