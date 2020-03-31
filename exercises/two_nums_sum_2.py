# gets a list and int x, return all the pairs that their sum == x
def print_pairs(arr, n):    # O(n)
    s = set()   # Create an empty hash set

    for i in range(len(arr)):
        temp = n - arr[i]
        if temp in s:
            print str(arr[i]), str(temp)
        s.add(arr[i])


A = [1, 4, 45, 6, 10, 6]
x = 16
print_pairs(A, x)
