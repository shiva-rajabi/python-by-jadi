ages = []
while (True):
    age = int(input('please enter you age: '))
    if(age == -1):
        break
    if(age >= 10 and age <=90 ):
        if age in ages:
           print("This age has already been entered")
           ages.remove(age)
        ages.append(age)
    else:
        print('Invalid age! please enter a number between 10 to 90')

max_age = max(ages)
print("The max_age is: ",max_age)
