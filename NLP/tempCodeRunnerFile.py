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