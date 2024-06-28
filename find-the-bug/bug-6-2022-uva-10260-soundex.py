# FIND THE BUG (#6)
# https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1201
# Online Judge 10260 - Soundex

import sys

soundexGroups = [ "BFPV", "CGJKSXZ", "DT", "L", "MN", "R" ]
soundex = {}

def buildSoundex():
    for i in range(len(soundexGroups)):
        for ltr in soundexGroups[i]:
            soundex[ltr] = i+1
    

def main():
    buildSoundex()

    last = ''
    for line in sys.stdin:
        for ltr in line:
            if ltr not in soundex:
                last = ''
            elif soundex[ltr] != last:
                print(soundex[ltr], end='')
                last = soundex[ltr]

        print()


main()

