# https://www.codewars.com/kata/517abf86da9663f1d2000003
def to_camel_case(text):
    text = text.replace("-"," ")
    text = text.replace("_"," ")
    split_text = text.split()
    
    for i in range(1,len(split_text)):
        split_text[i] = split_text[i].title()

    return "".join(split_text)
