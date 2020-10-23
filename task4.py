def check_num(num1, num2):
    """Function that checks if either num is 3
        AND their sum contains a 3"""
    sum = num1 + num2
    print(sum)
    if (num1 == 3 or num2 == 3 and 3 in sum):
        return True
    else:
        return False

num1 = input('Enter a num: ')
num2 = input('Enter another one: ')

print(check_num(num1, num2))