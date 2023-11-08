age = int(input('Please Enter Your Age :'))
if 0 < age < 6:
    print('You are baby!')
elif 6 <= age < 10:
    print('You are child!')
elif 10 <= age < 14:
    print('You are teenage!')
elif 14 <= age < 24:
    print('You are young!')
elif 24 <= age < 40:
    print('You are adult!')
elif age >= 40:
    print('You are middle-aged!')