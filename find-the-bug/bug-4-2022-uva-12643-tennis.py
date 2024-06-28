# FIND THE BUG (#4)
# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4391

import sys
import math

def main():
    for line in sys.stdin:
        N, i, j = map(int, line.split())
        matchround = None
        for r in range(1, N+1):
            ihalf = math.ceil(i/2)
            jhalf = math.ceil(j/2)
            if ihalf == jhalf: 
                matchround = r
            i = ihalf
            j = jhalf
        print(matchround)

main()


'''
3 2 5
3 5 7
2 1 2
2 2 1
'''

