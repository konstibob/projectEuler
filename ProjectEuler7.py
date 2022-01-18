import math 

#all prime numbers satisfy condition 6n+1 or 6n-1 (after 3)
def prime_numbers(num):
    i = 0
    #bounary = upper_bound(num)
    currentprime = 3
    primecounter = 2
    currentsolution = 0 
    while(primecounter != num):  
        i = i + 1
        currentprime = 6*i - 1
        if(isprime(currentprime)):
            currentsolution = currentprime 
            primecounter = primecounter + 1
            if(primecounter == num):
                return currentsolution
        
        currentprime = 6*i + 1
        if(isprime(currentprime)):
            currentsolution = currentprime 
            primecounter = primecounter + 1

    return currentsolution


#def upper_bound(n):
#    if(n<6):
#        return 13
#    return int(round(n * (math.log(n) + math.log(math.log(n))))) 


def isprime(x):  
    for i in range(2, round(math.sqrt(x))+1):
        if (x % i == 0):
            return False
    return True


print(prime_numbers(10001))


