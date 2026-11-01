def fun1(name = 'Padma', age = 12):
    print(name, "is", age, "years old.")

name = input()
age = int(input())

fun1(name = name, age = age)

fun1(name = name, age = 16)

fun1(age = age)

fun1(name = name)

fun1()


def mysum(*num):
     c = 0
    for i in num:
        c += i
    return c



a = int(input())
b = int(input())
c = int(input())
d = int(input())


print(mysum())
print(mysum())
print(mysum(1))


