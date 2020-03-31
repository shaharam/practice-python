#   this func prints the first non repeated char
def non_repeated_char(string):
    for i in range(len(string)):
        if not string[i] == string[i+1]:
            return string[i]
        i += 1


res = non_repeated_char("aabcdd")
print res
