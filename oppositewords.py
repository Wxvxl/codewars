# https://www.codewars.com/kata/56dec885c54a926dcd001095

def opposite(number):
    if number < 0: return abs(number)
    if number > 0: return -abs(number)
    else: return 0