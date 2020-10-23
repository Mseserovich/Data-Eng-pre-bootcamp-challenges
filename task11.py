def common_letters(str1, str2):
    temp = []
    
    for i in str1:
        if str2.count(i):
            temp.append(i)

    return temp

print('common letters: ' + " ".join(common_letters('computers', 'house')))
