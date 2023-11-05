

def Palindrome(s):
    s == s[::-1]
    print(s)
    return s
 
s = "malayalam"
ans = Palindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")