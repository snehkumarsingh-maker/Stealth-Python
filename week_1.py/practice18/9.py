#print a number from 1 to 10 using for loop

for i in range (1,11):
    print(i)

#write a program to print numbers form 10 to 1 using a for loop

for i in range (1,11):
    print(11-i)

#write a program to print all even numbers from 2 to 20 using a for loop

for i in range (2,20):
    if i % 2 == 0:
        print(i)

#write a program to print all odd numbers from 1 to 20 using a for loop

for i in range (1,20):
    if i % 2 != 0:
        print(i)

#write a program to print sum of all odd numbers from 1 to 100 using a for loop

sum = 0
for i in range (1,100,2):
    sum += i
print(sum)

#write a program to print all even numbers from 2 to 100 using a for loop

even = 0
for j in range (2,101,2):
    even += j
print(even)
