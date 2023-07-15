# https://www.codewars.com/kata/55c45be3b2079eccff00010f
import re

def order(sentence):
    new_sentence = []
    for i in range(9):
        for word in sentence.split():
            if re.search(str(i+1), word):
                new_sentence.append(word)

    return " ".join(new_sentence)

