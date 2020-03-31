#   gets a list and check if there is an index that the sum of left values equals sum of right
def equals_sums(x):
    for i in range(1, len(x)):
        # print sum(x[:i]), sum(x[i+1:])
        if sum(x[:i]) == sum(x[i+1:]):
            return i
    return False


a = [1, 4, 9, 1, 2, 2]
b = [1, 1]
print equals_sums(a)
print equals_sums(b)
