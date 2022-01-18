import math


def pythagorean_triple():
    number = 1000
    for i in range (1,100):
        for j in range(1,100):
            if (number == i*i + j*j):
                return (i,j)

print (pythagorean_triple())