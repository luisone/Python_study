""" --------阶乘---------"""

def recursion(n):
    result = n
    for i in range(1,n):
        result *= i
    return result

number = int(input('请输入一个整数：'))
result = recursion(number)
print("%d 的阶乘是：%d" % (number, result))




""" ------递归--------"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

number = int(input('请输入一个整数：'))
result = factorial(number)
print("%d 的阶乘是：%d" % (number, result))



""" ---------汉诺塔---------"""

def hanuota(n, x, y, z):
    if n == 1:
        print(x, '-->',z)
    else:
        hanuota(n-1, x,z,y)
        print(x, '-->',z)
        hanuota(n-1,y,x,z)

n = int(input('请输入汉诺塔的层数：'))
hanuota(n, 'X', 'Y', 'Z')
