def squaredsum():
    sum = 0
    squaresum = 0
    for i in range (1,101):
        sum = i * i + sum
    for i in range(1,101):
        squaresum = squaresum + i
    squaresum = squaresum * squaresum
    return squaresum - sum

print(squaredsum())