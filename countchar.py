# https://www.codewars.com/kata/52efefcbcdf57161d4000091
def count(s):
    output = {}
    if s != '':
        for letter in s:
            if letter not in output:
                output[letter] = 1
            else:
                output[letter] += 1
    return output