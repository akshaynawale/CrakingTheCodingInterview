# Write a function to find put one string is a permutation of another

s1=raw_input("string 1 :")
s2=raw_input("String 2 :")
array1=[0]*256
array2=[0]*256
Permitation=True
if len(s1) != len(s2):
    Permitation=False
else:
    for c in s1:
        key=ord(c)
        array1[key]=array1[key]+1
    for c in s2:
        key=ord(c)
        array2[key]=array2[key]+1
    if array1 != array2 :
        Permitation=False

if Permitation:
    print("strings are permitation of each other")
else:
    print("strings are not permitations of each other")

