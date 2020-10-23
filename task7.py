def convert(tmp):
    """converts temp from celcius to fahrenheit"""
    
    fah = (tmp / 5) * 9 + 32
    return fah

def convert2(fah):
    """converts temperature from fahrenheit to celcius"""

    tmp = (fah - 32) / 9 * 5
    return round(tmp, 2)

print(convert(23))
print(convert2(73.4))