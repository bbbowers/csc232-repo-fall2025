# https://open.kattis.com/problems/leftbeehind


def main():
    while True:
        (x, y) = map(int, input().split())
        if x+y == 0: break

        if x+y == 13: print("Never speak again.")
        elif x > y: print("To the convention.")
        elif x < y: print("Left beehind.")
        else: print("Undecided.")


main()


'''
Input:

17 3
13 14
8 5
44 44
0 0

Output:

To the convention.
Left beehind.
Never speak again.
Undecided.

'''
