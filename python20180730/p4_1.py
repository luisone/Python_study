score = int(input('Please input a score:'))

if 100 >= score >= 90:
    print('A')
elif 90 > score >= 80:
    print('B')
elif 80 > score >= 60:
    print('C')
elif 60 > score:
    print('D')
else:
    print('please input a vaild score(0~100)')


hi = int (input('Pleas input (0-10):'))
if hi > 2:
    if (hi > 7):
        print('hi == 6')
else:
    print('hi != 6')
