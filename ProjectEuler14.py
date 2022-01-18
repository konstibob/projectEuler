def collatz_sequence():
    largest_counter = 0
    returnvalue = (0,0)             #(number,how long it actually took)
    for i in range(1,1000000):
        num = i
        counter = 1
        while(i != 1):
            if(i % 2 == 0):
                i = i // 2
            else:
                i = 3*i + 1
            counter = counter + 1
        if (counter>largest_counter):
            largest_counter = counter
            returnvalue = (num,largest_counter)
    return returnvalue

print(collatz_sequence())