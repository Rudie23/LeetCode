

def palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


exam1 = palindrome(121)
print(exam1)

exam2 = palindrome(124)
print(exam2)
