def solution(text, ending):
    endlength = len(ending)
    print(endlength)
    if text[-endlength] == ending:
        return True
    else:
        return False

solution( "samurai", "ai" )