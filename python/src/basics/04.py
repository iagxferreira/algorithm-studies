def sum_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    return a / b

def main():
    numbers = []
    for i in range(2):
        number = int(input(f"provide number index {i+1}: "))
        numbers.append(number)
    print(f"sum: {sum_numbers(*numbers)}")
    print(f"subtraction: {subtract_numbers(*numbers)}")
    print(f"multiplication: {multiply_numbers(*numbers)}")
    print(f"division: {divide_numbers(*numbers)}")

main()
