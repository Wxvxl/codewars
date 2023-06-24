# https://www.codewars.com/kata/5656b6906de340bd1b0000ac
def longest(a1, a2):
    letter_list = []
    output = ""
    for letter in a1 + a2:
        if letter not in letter_list: letter_list.append(letter)
    for letter in sorted(letter_list):
        output += letter
    return output