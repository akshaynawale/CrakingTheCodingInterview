# this is a another answer with hash table with order (n) 
# here odr is a hash function and key is the character in the string
# while we are scannng through the string we will store the value in the array
# as 1 and so when the value is already present it will store it will come to
# know as it was already present. No need of double pointers. The length of the
# array is 256 because the ascii value of all letters is from 0 to 255.


s=str(raw_input("input a string for checking:"))
match = False
i=0
array=[0]*256

for c in s:
    key=int(ord(c))
    if array[key]==0:
        array[key]=array[key]+1
    else:
        match=True
if match:
    print("this string do not have all characters identical")
else:
    print("All characters are identical")
    
