# FIND THE BUG (#10)
# https://open.kattis.com/problems/grass

import sys
import math

def main():

    for line in sys.stdin:

        n, l, w = list(map(int, line.split()))
        sps = []             # list of sprinkler intervals
        for _ in range(n):   # read the  n   sprinklers
            x, r = list(map(int, input().split()))

            offset = math.sqrt( r*r - w*w/4 )
            sps.append( ((x - offset), (x + offset)) )
        

        covered = 0    # will change as we choose sprinklers to cover area
        end = l      # will not change
        sps.sort()   
        #print(sps)

        chosenCount = 0
        failed = False

        while covered < end:

            # choose the next interval that starts earlier or at `covered`
            # and extends the farthest
            furthestExtent = None  
            while (len(sps) > 0) and (sps[0][0] <= covered):
                p = sps.pop(0)   # take the first one off
                if not furthestExtent or p[1] > furthestExtent:
                    furthestExtent = p[1]

            if not furthestExtent:  # never found such an interval
                failed = True
                break
            else:                   # there was an interval that covered up to `furthestExtent`
                chosenCount += 1
                covered = furthestExtent

        if failed:
            print(-1)
        else:
            print(chosenCount)





main()
