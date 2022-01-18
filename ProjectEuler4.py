def palindrome():                       #geht ja eigentlich 
    largest_drome = 0
    for i in range(100,1000):
        for j in range(100,1000):
            num = i*j
            if num == reversee(num):
                if (num > largest_drome):
                    largest_drome = num
    return largest_drome

def reversee(num):
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num *10 + digit
        num = (num - digit)/10
    return reversed_num

print(palindrome())