def evenFib(a,b):
    tmp = 0
    sum = 0
    while(a < 4000000):
        tmp = a + b
        b = a 
        a = tmp
        if(a % 2 == 0):
            sum = sum + a
    return sum

print(evenFib(0,1))
