def divisor(num):
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
    return counter
number = int(input("Please Enter your number: "))
for i in range(1,2):
    count = divisor(number)
    if count <= 2:
        print("Your number is prime.")
    else:
        print("Your number is not prime.")


