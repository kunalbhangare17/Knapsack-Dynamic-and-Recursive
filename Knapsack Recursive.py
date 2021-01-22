# a dynamic approach
# Returns the maximum value that can be stored by the bag
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    # Table in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    return K[n][W]


# Main
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
