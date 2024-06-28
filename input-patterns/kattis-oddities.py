# https://open.kattis.com/problems/oddities

def main():
    n = int(input())

    for i in range(n):
        x = int(input())
        
        if (abs(x) % 2 == 0):
            print(str(x) + " is even")
        else:
            print(str(x) + " is odd")
        
main()


'''
Input:

3
10
9
-5

Output:

10 is even
9 is odd
-5 is odd

'''