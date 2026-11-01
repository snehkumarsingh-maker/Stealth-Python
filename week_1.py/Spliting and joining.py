import re
a = "Hello, how are you?"

b = re.split(r'\s+', a) # Split by spaces
c = "-".join(b) # Join with a hyphen

print(b)
print(c)

# yha pr hmne isko re.split ka function ka use krne solve kiya h ye or bhe methord se solve kra ja sakta tha but hmne isse kra h solve 