# https://open.kattis.com/problems/statistics

import sys

def main():
    case = 1

    for line in sys.stdin:
        nums = map(int, line.split()[1:])
        min = None
        max = None
        for n in nums:
            if min == None or n < min:
                min = n
            if max == None or n > max:
                max = n
        print(f"Case {case}: {min} {max} {max - min}")
        case = case + 1

main()

'''
Input:

2 4 10
9 2 5 6 4 5 9 2 1 4
7 6 10 1 2 5 10 9
1 9

Output:

Case 1: 4 10 6
Case 2: 1 9 8
Case 3: 1 10 9
Case 4: 9 9 0

'''