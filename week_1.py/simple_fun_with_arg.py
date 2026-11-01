def new (name, age):
    print( name, age)

new(name = "Sneh", age = 18)
new(age = 18, name= "Sneh")



def nageage(*, name, age):
    print(f"{name} {age}")


name = input()
age = input()

nageage(name, age)
nageage(age, name)