# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4
# This is the correct way of solving this problem.
# I wonder what I was thinking previously because that was horrible.

def reverse_words(text):
    return " ".join(s[::-1] for s in text.split(" "))