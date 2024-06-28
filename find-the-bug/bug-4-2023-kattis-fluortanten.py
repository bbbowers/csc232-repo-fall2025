# FIND THE BUG
# https://open.kattis.com/problems/fluortanten

# Idea: calculate without Bjorn first; then do O(n) pass backwards from the end to determine Bjorn's optimal position; 

def main():
    n = int(input())

    a = list(map(int, input().split()))
    a.remove(0)

    hap = 0
    for i in range(1, len(a)+1):
        hap = hap + i * a[i-1]

    best = hap
    alt = hap
    for i in range(1, len(a)):
        alt = alt + a[-i]       # negative index - from the end of the list
        if (alt > best): best = alt
    
    #print(hap)
    print(best)

main()


'''
Input:
7
2 -4 5 -3 0 -1 2

Output:
7

'''