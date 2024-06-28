# FIND THE BUG (#9) -- Courtesy of Bernny V.
# https://open.kattis.com/problems/shoppinglist

def main():
    n, m = input().split()
    groceryDict = {item: 1 for item in input().split()}   # counts the number of lists that each item is on

    for i in range(int(n) - 1):
        curGroceryList = list(input().split())

        for item in curGroceryList:
            if item in groceryDict and groceryDict[item] == i + 1: 
                    # increment the item value if the item is in the original dictionary and the count is the same which list we are currently on
                    groceryDict[item] += 1 
            elif item in groceryDict:   # and its count is not == i + 1
                    # remove the item in the dictionary because it means that there was at least one list that didn't have that item
                    groceryDict.pop(item) 

    # there may be items in the first list that are not in any other list so we need to remove those
    for item in dict(groceryDict):
        if not (groceryDict[item] == int(n)):
            groceryDict.pop(item)

    # sorts and prints the output
    sorted_keys = sorted(groceryDict.keys())
    print(len(sorted_keys))

    for key in sorted_keys:
        print(key)


main()

