from typing import final


def gennum(n):
    num = 1
    i = 0
    while(i != n):
        num = num * 2
        i = i + 1
    return num

def addnum(n):
    num = gennum(n)
    finalnum = 0
    while(num > 0):
        finalnum = finalnum + num % 10
        num = num // 10                                           #(num-num % 10)/10 warum ist das faslch?
    return finalnum

print(addnum(1000))