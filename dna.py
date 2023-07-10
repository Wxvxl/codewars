# https://www.codewars.com/kata/554e4a2f232cdd87d9000038
def DNA_strand(dna):
    dna = dna.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G','c')
    return dna.upper()