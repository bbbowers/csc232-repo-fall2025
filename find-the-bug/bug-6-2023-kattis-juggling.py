# FIND THE BUG (#6)
# https://open.kattis.com/problems/jugglingpatterns

from sys import stdin
from heapq import *

def rotate(nums):
    ''' Takes the first thing in the list and moves it to the end
    > rotate([3, 4, 5, 7])
    [4, 5, 7, 3]
    '''
    return [ nums[ (i + 1) % len(nums) ] for i in range(len(nums)) ]


def main():
    for line in stdin:
        line = line.strip()
        nums = list(map(int,list(line)))

        msg = "invalid pattern"
        if (sum(nums) % len(nums)) != 0:
            msg = "invalid # of balls"
        else:
            numBalls = sum(nums) // len(nums)

            unusedBalls = numBalls
            t = 0   # time = current beat
            pq = []
            valid = True
            for _ in range(len(nums) * numBalls):
                #print(pq)
                if len(pq) > 0 and pq[0] == t:
                    heappop(pq)
                    if (len(pq) and pq[0] == t):  # another ball landing at the same time!
                        valid = False
                        break
                    heappush(pq, t + nums[0])
                    nums = rotate(nums)    

                # either pq is empty or the thing on it is not landing at the current time
                elif unusedBalls > 0 and nums[0] > 0:
                    unusedBalls -= 1
                    heappush(pq, t + nums[0])
                    nums = rotate(nums)
                elif nums[0] == 0 and (len(pq) > 0 and pq[0] != t):
                    nums = rotate(nums)
                else:
                    valid = False
                    break
                t += 1

            if valid:
                msg = f"valid with {numBalls} balls"

        print(f"{line}: {msg}")

main()

