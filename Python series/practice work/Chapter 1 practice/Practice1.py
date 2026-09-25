# fruit = " banana "

# for char in fruit:
#     print(char)



# index = 0
# while index < len(fruit):
#     print(fruit[index])
#     index = index + 1

# word = "banana"
# print(word.find("an"))

# nums = [10, 20, 30]
# mixed = [1, "two", 3.0, [4, 5]]
# print(len(mixed))        # 3
# print(4,5 in mixed)      # True

# for n in nums:
#     print(n)
# for i, n in enumerate(nums):    # when you need the index too
#     print(i, "->", n)


a, b = 1, 2
a, b = b, a          # swap — no temp variable needed
print(a, b)         # 2 1

def max_min(values):
    return max(values), min(values)   # packs two values into a tuple

lo_ji_a_gye_punjabi, helo_jiiiii = max_min([4,23454234235,-54234134523456256234532452345234532452345234523452364562345234523452345,234523452345345234534523452345345234523452345234523452345342523452345234523453245234523453425232344444444444444444444444523455555555555234523452345234555555555555555555555555555555555532323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232323232,-999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999, 1, 9, 2])   # unpacks the returned tuple
print(lo_ji_a_gye_punjabi, helo_jiiiii)      # 1 9

ages = {"Riya": 21, "Sam": 19}
ages["Priya"] = 22              # add new key
print(ages.get("Zoe", 0))   # 0 — safe default instead of KeyError
for name, age in ages.items():
    print(name, "is", age)