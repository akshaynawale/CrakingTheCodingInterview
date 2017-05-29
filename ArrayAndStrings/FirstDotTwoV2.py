# In this solution the problem is sloved by a iterative approch rather than a
# recursive apporch.

s= raw_input("enter a string")
r=""
for i in range((len(s)-1),-1, -1):
    r=r+s[i]
print(r)
