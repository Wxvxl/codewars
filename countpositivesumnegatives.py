def count_positives_sum_negatives(arr):
    positives = []
    negatives = []
    for number in arr:
        if number > 0: positives.append(number)
        else: negatives.append(number)
    return [len(positives), sum(negatives)]