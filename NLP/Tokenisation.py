
#1. Custom Word Tokenizer (Medium)

import re
import spacy

nlp = spacy.load("en_core_web_sm")

def custom_tokenizer(text):

    text = text.lower()


    text = re.sub(r"[.,!?:;]", "", text)

    doc = nlp(text)

    tokens = [token.text for token in doc]

    return tokens


text = "Hello, World! NLP is amazing."

print(custom_tokenizer(text))

#2.Subword Tokenization – WordPiece (Medium–Hard)

vocab = ["play","##ing","##er","work","##er","##ing"]
def wordpiece_tokenize(word, vocab):

    tokens = []

    while len(word) > 0:

        match = None

        for i in range(len(word),0,-1):

            sub = word[:i]

            if tokens:
                sub = "##" + sub

            if sub in vocab:
                tokens.append(sub)
                word = word[i:]
                match = True
                break

        if not match:
            return ["[UNK]"]

    return tokens
print(wordpiece_tokenize("playing", vocab))

#3. Byte Pair Encoding (BPE) Merge Step (Hard)
from collections import Counter

corpus = ["low","lower","newest","widest"]

split_words = [list(word) for word in corpus]

print("Character Split Corpus:")
print(split_words)

pairs = Counter()

for word in split_words:
    for i in range(len(word)-1):
        pair = (word[i],word[i+1])
        pairs[pair] += 1

print("\nPair Frequencies:")
print(pairs)

best_pair = pairs.most_common(1)[0][0]

print("\nMost Frequent Pair:", best_pair)

new_corpus = []

for word in split_words:

    i = 0
    new_word = []

    while i < len(word):

        if i < len(word)-1 and (word[i],word[i+1]) == best_pair:
            new_word.append(word[i] + word[i+1])
            i += 2
        else:
            new_word.append(word[i])
            i += 1

    new_corpus.append(new_word)

print("\nUpdated Corpus:")
print(new_corpus)

#4. SentencePiece Style Tokenization (Hard)
vocab = ["■deep", "■learning", "■is", "fun"]

def sentencepiece_tokenize(sentence):

    words = sentence.split()

    tokens = []

    for word in words:

        token = "■" + word

        if token in vocab:
            tokens.append(token)

        elif word in vocab:
            tokens.append(word)

        else:
            tokens.append("[UNK]")

    return tokens
text = "deep learning is fun"
print(sentencepiece_tokenize(text))

#5. Tokenizer With Position Tracking (Hard)
import spacy

nlp = spacy.load("en_core_web_sm")

text = "I love NLP"

doc = nlp(text)

for token in doc:
    print((token.text, token.idx, token.idx + len(token.text)))

#6. Mini BERT Tokenizer (Hard)

vocab = ["play","##ing","football"]

def wordpiece(word):

    tokens = []

    while len(word) > 0:

        match = None

        for i in range(len(word),0,-1):

            sub = word[:i]

            if tokens:
                sub = "##" + sub

            if sub in vocab:
                tokens.append(sub)
                word = word[i:]
                match = True
                break

        if not match:
            return ["[UNK]"]

    return tokens


def bert_tokenizer(sentence):

    sentence = sentence.lower()

    words = sentence.split()

    tokens = ["[CLS]"]

    for word in words:
        tokens.extend(wordpiece(word))

    tokens.append("[SEP]")
    return tokens
print(bert_tokenizer("Playing football"))