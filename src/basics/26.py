def main():
    sum = 0
    i = 1
    while i <= 100:
        sum += i
        i += 1
    print(sum)


# alternative
def gauss_sum(n):
    return n * (n + 1) / 2


main()
print(int(gauss_sum(100)))
