print("Hi, How are you doing? let's calculate the final price for your product after discount.")
print(" Please tell me the price of the product.")
b = input()

print("So the amount is" , b)
d = int(b)
discount = d * 0.6789
print("the discounted amount is", discount)
final_price = d - discount
print("the final price is", final_price)
print("Thank you , and come again ")