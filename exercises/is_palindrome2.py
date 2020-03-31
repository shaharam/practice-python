#   Return True if the input string is palindrome using substring
def is_palindrome(x):
    if len(x) % 2 == 0:     # check if the string has even/odd characters
        return x[:len(x) / 2] == x[(len(x) / 2):][::-1]
    else:
        return x[:len(x) / 2] == x[(len(x) / 2)+1:][::-1]


print is_palindrome("abccba")    # True
print is_palindrome("abcbca")    # False
print is_palindrome("abcdcba")   # True
print is_palindrome("a")         # True
print is_palindrome("ab")        # False
print is_palindrome("aa")        # True
print is_palindrome("")          # True
