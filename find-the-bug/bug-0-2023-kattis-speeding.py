# FIND THE BUG
# https://open.kattis.com/problems/speeding

import math

def main():
    n = int(input())

    (lastt, lastd) = map(int, input().split())  # the first 0 0
    maxSpeed = 0

    for i in range(n):
        (nextt, nextd) = map(int, input().split())  # read the next input line and break it up
        difft = (nextt - lastt)  # figure out the differences between the last values and the current ones
        diffd = (nextd - lastd)
        curSpeed = math.floor(diffd/difft) # the speed on this segment
        maxSpeed = max(maxSpeed, curSpeed) # update the max speed
        lastt = nextt # the current values become the 'last' ones for the next round of the loop
        lastd = nextd

    print(maxSpeed)

main()

