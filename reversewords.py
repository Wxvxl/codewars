# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4
# I regret writing this block of code.
def reverse_words(text):
    whitespace_location = []

    new_word = ""
    for i in range(len(text)):
        if text[i] == " ":
            whitespace_location.append(i)
    word_list = text.split()
    for i in range(len(word_list)):
        word_list[i] = word_list[i][::-1]

    for word in word_list:
        new_word += word

    for i in range(len(new_word)+25):
        for x in whitespace_location:
            if i == x:
                new_word = new_word[:i] + " " + new_word[i:]
                whitespace_location.remove(x)

    return new_word
