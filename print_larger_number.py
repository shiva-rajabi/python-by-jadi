num1 = int(input('Please Enter Your Number1 : '))
num2 = int(input('Please Enter Your Number2 : '))
if num1 <= 0 or num2 <= 0:
    print('Your number must be positive number')
elif num1 > num2:
    print('The number 1 is larger than number 2')
elif num1 < num2:
    print('The number 2 is larger than number 1')
else:
    print('The number 1 and number 2 are equal')