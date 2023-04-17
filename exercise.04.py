def get_sum():
    while True:
        try:
            num = int(input("Enter an integer: "))
            return num
        except ValueError:
            print("Invalid input: Enter an integer!")

numbers = []
for i in range(5):
    num = get_sum()
    numbers.append(num)

total = sum(numbers)

print("Your sum is ", total)