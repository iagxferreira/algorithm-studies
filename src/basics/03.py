def sum_numbers(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    return sum

def main():
    numbers = []
    for i in range(2):
        number = int(input(f"provide number index {i+1}: "))
        numbers.append(number)
    print(sum_numbers(numbers))

main()
