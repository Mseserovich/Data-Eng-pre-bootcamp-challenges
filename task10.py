def spit_vowel(str1):
    res = []
    list1 = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    i = 0
    while i < len(list1):
        if list1[i] in str1:
            res += list1[i]
        i += 1
    return " ".join(res)

print(spit_vowel('msEase'))