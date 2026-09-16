i = int(input("Enter the 1st value: "))
j = int(input("Enter the 2nd value: "))

Op = input("Operator: ")

match Op:
    case " < ":
        print(i < j)
    case " > ":
        print(i > j)
    case " = ":
        print(i == j)
    case " != ":
        print(i != j)
    case " & ":
        print( i & j)
    case " % ":
        print(i % j)
    case " / ":
        print(i / j)
    case " // ":
        print(i // j)
    case " | ":
        print(i | j)
    case " * ":
        print(i * j)
    case " ** ":
        print(i ** j)
    case _:
        print("Invalid operator, pagla wagla gya h kya be pagal h tu sale operator to dhang se likh le agar likhna nhi ata to engineering chord or majdoor bnja bhadwe")