from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, ngrams
import numpy as np
from collections import defaultdict
import random
import string
## Internal Imports
from csvImport import parseCSVColumnToNumpyArray
from saveModel import save_model
from saveModel import load_model

MODEL_FILENAME = 'ngram_model.pkl'

def tag(word: str) -> str:
    tag = pos_tag([word])[0][1]
    map = {
        "JJ": wordnet.ADJ,
        "NN": wordnet.NOUN,
        "RB": wordnet.ADV,
        "VB": wordnet.VERB,
    }
    return map.get(tag, wordnet.NOUN)

def preprocess(text: str) -> str:
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    tokens = [t for t in tokens if t not in string.punctuation]
    tokens = [t.replace("'", "") for t in tokens] 
    tokens = [t.replace("...", "") for t in tokens] 
    tokens = [t.replace("\"", "") for t in tokens] 
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word, tag(word)) for word in tokens]
    return tokens

def build_ngram_model(model, tokens: str, size: int)-> None:
    for ngram in ngrams(tokens, size):
        model[ngram[:-1]].append(ngram[-1])

def generate_text(model: dict, length: int) -> str:
    seed = random.choice(list(model.keys()))
    text = list(seed)
    next_key = seed
    for _ in range(length):
        if next_key not in model:
            break
        next_word = random.choice(model[next_key])
        text.append(next_word)
        next_key = next_key[1:] + (next_word,)
        # print(next_key)
        
    return ' '.join(text)

def generate_tweet(text, length, ngram_size):

    model = load_model(MODEL_FILENAME)

    if not model:  # If model is empty, build it
        model = defaultdict(list)
        for sentence in text:
            tokens = preprocess(sentence)
            build_ngram_model(model, tokens, ngram_size)
    save_model(model, MODEL_FILENAME)  # Save the trained model
    
    print(generate_text(model, length))

if __name__ == "__main__":
    print("Hello World!")
    array = parseCSVColumnToNumpyArray("../Fake.csv", "text")
    generate_tweet(array, 15, 3)
