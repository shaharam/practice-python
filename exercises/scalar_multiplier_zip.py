#   This function gets two lists and calculate the sum of scalar multiplication using zip
def scalar_zip(x, y):
    sum = 0
    for i, j in zip(x, y):
        print i, j
        sum += i*j
    return sum


a = [0, 2, 3]
b = [4, 5, 6, 7]

print scalar_zip(a, b)