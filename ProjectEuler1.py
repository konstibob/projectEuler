def multiples():
    x = 0
    for i in range (1000):
        if i % 3 == 0 or i % 5 == 0:
            x = x + i
    return x
            
print(multiples())
