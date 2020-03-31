#   Return True if the input string is palindrome
def is_palindrome(x):
    left = 0
    right = len(x)-1
    while right > left:
        if not x[left] == x[right]:
            return False
        left += 1
        right -= 1
    return True


print is_palindrome("abccba")    # True
print is_palindrome("abcbca")    # False
print is_palindrome("abcdcba")   # True
print is_palindrome("a")         # True
print is_palindrome("ab")        # False
print is_palindrome("aa")        # True
print is_palindrome("")          # True
