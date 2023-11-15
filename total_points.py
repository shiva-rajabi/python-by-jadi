count_win = 0
count_equal = 0
count_loss = 0
sum = 0
for i in range(1,31):
    points = int(input('please enter your point : '))
    if points == 0:
        count_loss = count_loss+ 1
    if points == 1:
            count_equal = count_equal + 1
            sum = points + sum
    if points == 3:
        count_win = count_win +1
        sum = points + sum
print('The total points is:',sum,'///','The number of team wins is:', count_win)

