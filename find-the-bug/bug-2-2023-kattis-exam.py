# FIND THE BUG
# https://open.kattis.com/problems/exam

def main():
    k = int(input())

    myAns = input()
    frAns = input()
    n = len(myAns)
    p = 0  # number of matching
    q = 0  # number not matching

    for i in range(n):
        if (myAns[i] == frAns[i]): p += 1
        else: q += 1
    
    print(max( min(k, p), min((n-k),q) ))

main()


'''
Input:
3
FTFFF
TFTTT

Output:
2


Input:
6
TTFTFFTFTF
TTTTFFTTTT

Output:
9


'''