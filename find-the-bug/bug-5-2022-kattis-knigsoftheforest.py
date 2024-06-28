# FIND THE BUG (#5)
# https://open.kattis.com/problems/knigsoftheforest

import heapq

# () -> [list Integer Integer]
# helper function to read and split lines of input
def readPair():
    return list(map(int, input().strip().split()))


# Integer -> Integer
# Because Python's heapq is a "min" queue - the smallest thing comes to the
# front. So this inverts the strength values by subtracting from the largest
# possible value. So larger strength values will produce smaller key's based
# on this function, and thus will have higher priority in the queue.
def key(x):
    return 2 ** 31 - x


def main():
    k, n = readPair()
    yK, pK = readPair()

    data = [ (yK, pK, True) ]
    for i in range(n + k - 2):
        y, p = readPair()
        data.append( (y, p, False) )
    data.sort()

    pq = []
    d = 0   # index of how much of data is used

    while len(pq) < k:
        y, p, is_k = data[d]
        d += 1
        assert y == 2011
        heapq.heappush(pq, (key(p), is_k))

    year = 2011
    while d < len(data):
        winner = heapq.heappop(pq)
        if (winner[1]): 
            print(year)
            return  # all done - quit the whole program
        else:
            y, p, is_k = data[d]
            d += 1
            heapq.heappush(pq, (key(p), is_k))
        year += 1

    print("unknown")

main()
