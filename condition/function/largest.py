def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    print(largest)

find_largest([10, 50, 20, 40])