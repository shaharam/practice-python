#   This function gets two lists and calculate the sum of scalar multiplication
def scalar_multi(x, y):
    sum = 0
    for i in range(len(x)):
        sum += x[i] * y[i]
    return sum


a = [0, 2, 3]
b = [4, 5, 6]

print scalar_multi(a, b)
