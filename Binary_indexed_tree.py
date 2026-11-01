import sys

class GFG:

    def updateBIT(BITree, n, index, val):
        index += 1

        while index <= n:
            BITree[index] += val
            index += index & (-index)


    def getSum(BITree, index):
        sum = 0
        index += 1

        while index > 0:
            sum += BITree[index]
            index -= index & (-index)
        return sum

    def constructBITree(arr, n):
        BITree = [0] * (n + 1)

        for i in range(n):
            GFG.updateBIT(BITree, n, i, arr[i])

        return BITree

    

if __name__ == "__main__":
    freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(freq)

    # Build the BIT
    BITree = GFG.constructBITree(freq, n)
    print("Sum of elements in arr[0..5] is:", GFG.getSum(BITree, 5))

    delta = 6
    GFG.updateBIT(BITree, n, 3, delta)
    
    print("Sum of elements in arr[0..5] after update is:", GFG.getSum(BITree, 5))