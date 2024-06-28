# FIND THE BUG (#2)
# https://onlinejudge.org/external/110/11078.pdf
# https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=2019

def main():
    cases = int(input())

    for c in range(cases):
        stus = int(input())

        mx = int(input())   # first score
        mxDiff = None
        for s in range(stus-1):
            x = int(input())  # next score
            if x > mx: mx = x
            if mxDiff == None or (mx - x) > mxDiff: mxDiff = (mx - x)
        
        print(mxDiff)

main()          
           
'''
       mx  mxDiff
7      7     0
4      -     3
9      9     -
5      -     4
1      -     8
10    10     - 
'''


