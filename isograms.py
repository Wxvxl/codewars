# https://www.codewars.com/kata/54ba84be607a92aa900000f1
def is_isogram(string):
    for letter in string.lower():
        if string.lower().count(letter) != 1:
            return False
    return True