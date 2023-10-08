# https://www.codewars.com/kata/5264d2b162488dc400000001
def spin_words(sentence):
    listSentence = sentence.split()
    for i in range(len(listSentence)):
        if len(listSentence[i]) >= 5:
            listSentence[i] = listSentence[i][::-1]
    
    return " ".join(listSentence)