num = int(input('Please Enter Your Number : '))
if 100 <= num <= 999:
    num_inverse = int(str(num)[::-1])
    print('inverse Your Number Is :', num_inverse)
else:
    print('Your Number Is Invalid!!! Your Number Must be 3-digit number')