def smallestdividor():
    smallestdiv = 0
    for i in range(1,21):
        smallestdiv = ggv(i,smallestdiv)
    return smallestdiv

def ggv(a,b):
    if (b == 0):
        return 1
    real_a = a 
    real_b = b
    while (a != b):
        if (a < b):
            a = a + real_a
        elif (a > b):
            b = b + real_b
    return a

print(smallestdividor())
