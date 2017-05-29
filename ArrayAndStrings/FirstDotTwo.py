#Implement a function void reverse(char* str)  which will revers ea null
#terminated string
# this is sloved with a recusrsive program 
# Things to remember Strings are immutable objects in python. You can not do
# s[i]=s[j] --> you have to create a new string everytime you make a change in
# a string, This recursive function is able to make changes in the string
# becasue it is returning new string everytime, when it is called recusrsively.

s=str(raw_input("Enter a String:"))

def rev_str(s):
    if len(s)  == 1 :
        return s
    elif len(s) == 2:
        return (s[1]+s[0])
    else:
        return s[len(s)-1]+rev_str(s[1:((len(s))-1)])+s[0]

print(rev_str(s))
