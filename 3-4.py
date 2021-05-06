# question 1
#def func1(num):
#    """
#    returns:num ** 2.
#    :param num: int.
#    :return:int num ** 2.
#    """
    
#    return num ** 2

#x = int(input('Please enter a number'))
#result = func1(x)

#print(result)


# question 2
#def func2(val='brink182'):
#    """
#    returns: return string
#    :param val: str.
#    :return: str.
#    """
#    print(val)

#func2()


# question3
#def func3(x, y, z, val1='OK', val2='NO'):
#    """
#    returns: none
#    :param x: int.
#    :param y: int.
#    :param z: int.
#    :param val1: str.
#    :param val2: str.
#    :return: none.
#    """
#    print(x, y, z, val1, val2)

#func3(1, 2, 3, val1='YHEAAA')


# question4
#def func4_1(x):
#    """
#    returns: xを2で割った値を返します。
#    :param x: int
#    :return: x // 2
#    """
#    return x // 2

#def func4_2(y):
#    """
#    returns: yに4をかけた値を返します。
#    :param y: int
#    :return: y * 4
#    """
#    return y * 4

#z = int(input('Please enter a number:'))

#result = func4_1(z)
#result2 = func4_2(result)

#print(result2)


# question5
def func5():
    """
    returns: 入力された値をfloat型に変換します。
    :param: none.
    :return: float(input)
    """
    try:
        val3 = input('Please enter a number:')
        fl_val = float(val3)
        return fl_val
    except ValueError:
        print('val3が不正な値です。')

result = func5()

print(result)

