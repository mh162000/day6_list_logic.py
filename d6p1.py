numbers = [10, 5, 20, 89]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)