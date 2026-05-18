def palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] == s[-1]:
        return palindrome(s[1:-1])
    else:
        return Fals

text=input("enter word")
if(palindrome(text)):
  print("palindrome")
else:
    print("not palindrome")
