def high_and_low(numbers):
    numbers = numbers.split(" ")
    numbers = [int(x) for x in numbers]
    numbers = f"{max(numbers)} {min(numbers)}"
    return numbers

