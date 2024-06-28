# https://open.kattis.com/problems/cd

from sys import stdin, stdout

def main():
    while True:

        (N, M) = map(int, stdin.readline().strip().split())
        if N+M == 0: break

        common = 0
        collect = set([])
        for _ in range(N):
            collect.add(int(stdin.readline()))
        for _ in range(M):
            if int(stdin.readline()) in collect:
                common = common + 1
        print(common)

main()


'''
TLE:  
(note: bug without the while True loop...)

def main():
    while True:
        (N, M) = map(int, input().split())
        if N+M == 0: break

        common = 0
        collect = set([])
        for _ in range(N):
            collect.add(int(input()))
        for _ in range(M):
            if int(input()) in collect:
                common = common + 1
        print(common)

main()
'''

'''
3 3
1
2
3
1
2
4
0 0
'''