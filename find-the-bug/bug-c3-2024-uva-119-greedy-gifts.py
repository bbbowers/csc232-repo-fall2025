# https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=55#google_vignette

from sys import stdin

def main():
    
    firstOne = True
    for line in stdin:   # reads the # of ppl
        n = int(line)
        names = input().split()

        # create a dictionary with each name
        # mapped to zero, initially
        tots = { name : 0  for  name in names }

        # tots = {}   # alternate way
        # for name in names: tots[name] = 0
        
        for i in range(n):
            giveLine = input().split()
            person = giveLine[0]
            amt = int(giveLine[1])
            recips = giveLine[3:]

            # print( person, amt, recips ) # debug

            tots[person] -= amt
            if len(recips) > 0:
                quotient = amt // len(recips)
                leftover = amt % len(recips)

                tots[person] += leftover
                for r in recips:
                    tots[r] += quotient
                

        if firstOne: firstOne = False
        else: print()   # separate line between
        for name in names:
            print(name, tots[name])
        
main()



'''
5
dave laura owen vick amr
dave 200 3 laura owen vick
owen 500 1 dave
amr 150 2 vick owen
laura 0 2 amr vick
vick 0 0
3
liz steve dave
liz 30 1 steve
steve 55 2 liz dave
dave 0 2 steve liz
'''