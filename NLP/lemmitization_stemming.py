import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download resources
nltk.download('punkt')
nltk.download('punkt_tab')   # Important fix
nltk.download('wordnet')

text = "Players were playing football and studying strategies"

# Tokenization
tokens = word_tokenize(text)

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

lemmatized_words = []

for word in tokens:
    lemma = lemmatizer.lemmatize(word)
    lemmatized_words.append(lemma)

print("Original Tokens:", tokens)
print("Lemmatized Words:", lemmatized_words)