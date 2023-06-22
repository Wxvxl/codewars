# https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d
def solution(text, ending):
    endlength = len(ending)
    print(endlength)
    if text[-endlength] == ending:
        return True
    else:
        return False