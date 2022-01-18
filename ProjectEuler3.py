def primefact(num):
    largest = 2
    while num > 2:
        smallprime = smallestprime(num)
        if(smallprime > largest):
            largest = smallprime
            num = num // smallprime
    return largest

def smallestprime(x):  
    for n in range(2, x+1):
        if (x % n == 0):
            return n

print(smallestprime(100))      #geht nicht mit geraden zahlen??    
