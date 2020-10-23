def check_num(num1, num2):
    """Function that checks if either num is 65
        or if their sum is 65"""
    if ((num1 == 65 or num2 == 65) or num1 + num2 == 65):
        return True
    else:
        return False


num1 = int(input('Enter a number: '))
num2 = int(input('Enter another one: '))

print(check_num(num1, num2))

