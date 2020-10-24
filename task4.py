def check_num(num1, num2):
    """Function that checks if either num is 3
        AND their sum contains a 3 then returns true"""
        
    sum = int(num1) + int(num2)
    if (num1 == '3' or num2 == '3' and '3' in str(sum)):
        return True
    else:
        return False

num1 = input('Enter a num: ')
num2 = input('Enter another one: ')

print(check_num(num1, num2))