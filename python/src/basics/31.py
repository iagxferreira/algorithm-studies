def main():
    print("press 0 to exit")
    prompt = ""
    counter = 0
    while prompt != "0":
        prompt = input("write there >> ")
        if int(prompt) % 2 == 0 and int(prompt) != 0:
            counter += 1
    print(f"even provided: {counter}")


main()
