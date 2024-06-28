# UVa 12650 Dangerous Dive
# https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=4379

from sys import stdin

def main():
    for line in stdin:
        N, R = list(map(int, line.split()))
        ids = list(map(int, input().split()))

        if N == R:
            print("*")
        else:
            rtd = [ False for _ in range(N) ]
            for i in ids:
                rtd[i-1] = True
            missing = []
            for i in range(1,N-1):
                if not rtd[i]: missing.append(i+1)
            print( " ".join(map(str,missing)) + " " )


main()

