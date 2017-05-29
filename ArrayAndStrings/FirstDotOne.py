s=str(raw_input("input a string for checking:"))
match = False
i=0
RepeatedChar=""
while i < (len(s)-1):
    j=i+1
    while j < len(s):
        if s[i] == s[j]:
            match = True
            RepeatedChar=RepeatedChar+"--"+s[i]
        j=j+1
    i=i+1

if match :
    print("this string do not have all characters identical")
    print("Repeated Characters are"+RepeatedChar)
else:
    print("All characters are identical")
    
