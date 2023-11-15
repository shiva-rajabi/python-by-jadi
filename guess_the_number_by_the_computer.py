import random
guess = random.randint(1,99)
print(guess)
new_min = 0
new_max = 0
while True:
    answer = input('user idea :')
    if answer == 'b':
        new_min = guess
        guess = random.randint(new_min,99)
        print(guess)
    elif answer == 'k':
        new_max = guess
        guess = random.randint(1,new_max)
        print(guess)
    elif answer == 'd':
        print('Wooow the computer did it. the number is ', guess)
        break