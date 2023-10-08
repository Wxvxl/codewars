# https://www.codewars.com/kata/55b42574ff091733d900002f
def friend(x):
    toberemoved = []
    for i in range(len(x)):
        if len(x[i]) != 4:
            toberemoved.append(i)
    for i in sorted(toberemoved,reverse = True):
        del x[i]
    return x