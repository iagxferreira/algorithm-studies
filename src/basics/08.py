def main():
    sum = 0
    values = []
    times = int(input("how much notes you want to insert? "))
    for i in range(times):
        number = float(input(f"provide your {i + 1} note: "))
        sum += number
        values.append(number)
    average = sum / len(values)
    print(f"average: {average:.2f}")

main()
