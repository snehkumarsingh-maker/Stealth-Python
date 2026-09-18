
#count even number present in 1 to 50
cout = 1
for i in range (1,50):
    if i % 2 == 0:
        cout += 1
print(cout)

# count odd number present in 1 to 50 
odd = 0
for i in range(1,50):
    if i % 2 != 0:
        odd += 1
print(odd)        