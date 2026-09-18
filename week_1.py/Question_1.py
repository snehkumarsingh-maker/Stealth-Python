#print prime number upto 100
n = 100
num = 2

while num <= n:
    is_prime = True
    i = 2
    while i <num:
        if num % i == 0:
            is_prime = False
            break
        i +=1
    if is_prime:
        print(num)

        num += num + 1 