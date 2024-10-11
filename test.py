def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


numbers = [10, 20, 30, 40, 50]
print("Average:", calculate_average(numbers))