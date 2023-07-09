# https://www.codewars.com/kata/576bb71bbbcf0951d5000044
def count_positives_sum_negatives(arr):
    positives = []
    negatives = []
    for number in arr:
        if number > 0: positives.append(number)
        else: negatives.append(number)
    return [len(positives)+1, sum(negatives)]