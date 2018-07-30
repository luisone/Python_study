for i in range(10):
    if i % 2 != 0:
        print(i)
        continue
    i += 4
    print('i+2 = ' + str(i))
print(i)
