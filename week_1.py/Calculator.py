i = int(input("Enter the 1st value: "))
j = int(input("Enter the 2nd value: "))

Op = input("Operator: ")

if Op == '+':
    print("Answer= ", i +j)
elif  Op == '-':
    print("Answer= ", i - j)
elif  Op == '*':
    print("Answer= ", i *j)
elif  Op == '/':
    print("Answer= ", i /j)
else:
    print("Galat operator")