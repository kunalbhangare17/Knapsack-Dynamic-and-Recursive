# Returns the maximum value that can be stored by the bag
def knapSack(W, wt, val, n):
    # initial conditions
    if n == 0 or W == 0:
        return 0
    # If weight is higher than capacity then it is not included
    if wt[n - 1] > W:
        return knapSack(W, wt, val, n - 1)
    # return either nth item being included or not
    else:
        return max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
                   knapSack(W, wt, val, n - 1))


# To test above function
num = int(input("Enter total number of elements(Vals and Wt): "))
val = []
wt = []

for i in range(num):
    a = int(input(f"Enter the {i}th value: "))
    b = int(input(f"Enter the {i}th weight: "))
    val.append(a)
    wt.append(b)

W = int(input("Enter the total weight of the bag: "))
n = len(val)
print(knapSack(W, wt, val, n))
