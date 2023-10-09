# https://www.codewars.com/kata/530e15517bc88ac656000716
def rot13(message):
    
    smolalphabet = {
        'a' : 1,
        'b' : 2,
        'c' : 3,
        'd' : 4,
        'e' : 5,
        'f' : 6,
        'g' : 7,
        'h' : 8,
        'i' : 9,
        'j' : 10,
        'k' : 11,
        'l' : 12,
        'm' : 13,
        'n' : 14,
        'o' : 15,
        'p' : 16,
        'q' : 17,
        'r' : 18,
        's' : 19,
        't' : 20,
        'u' : 21,
        'v' : 22,
        'w' : 23,
        'x' : 24,
        'y' : 25,
        'z' : 26,
    }

    beegalphabet = {
        'A' : 1,
        'B' : 2,
        'C' : 3,
        'D' : 4,
        'E' : 5,
        'F' : 6,
        'G' : 7,
        'H' : 8,
        'I' : 9,
        'J' : 10,
        'K' : 11,
        'L' : 12,
        'M' : 13,
        'N' : 14,
        'O' : 15,
        'P' : 16,
        'Q' : 17,
        'R' : 18,
        'S' : 19,
        'T' : 20,
        'U' : 21,
        'V' : 22,
        'W' : 23,
        'X' : 24,
        'Y' : 25,
        'Z' : 26,
    }
    
    encodedmessage = ""

    for letter in message:
        if letter in smolalphabet:
            for smolletter, smolindex in smolalphabet.items():
                if smolindex == (smolalphabet[letter] + 13) % 26:
                    encodedmessage += smolletter
                if smolindex == ((smolalphabet[letter] + 13) % 26) + 26:
                    encodedmessage += smolletter


        if letter in beegalphabet:
            for beegletter, beegindex in beegalphabet.items():
                if beegindex == (beegalphabet[letter] + 13) % 26:
                    encodedmessage += beegletter
                if beegindex == ((beegalphabet[letter] + 13) % 26) + 26:
                    encodedmessage += beegletter

        if not letter.isalpha():
            encodedmessage += letter;
                    
    return encodedmessage