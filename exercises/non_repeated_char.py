#   this func prints the first non repeated char
def first_non_repeating_character(str):
    char_order = []
    counter = {}
    for char in str:
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
            char_order.append(char)
    for char in char_order:
        if counter[char] == 1:
            return char
    return None


print(first_non_repeating_character('abcdef'))
print(first_non_repeating_character('abcabcdef'))
print(first_non_repeating_character('aabbcc'))