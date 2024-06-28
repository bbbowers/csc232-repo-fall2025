# FIND THE BUG
# https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=355
# 414 - Machined Surfaces

def main():
    while True:
        N = int(input())
        if (N == 0): break

        counts = []
        mx = 0
        for _ in range(N):
            line = input()
            xs = len(line.replace('B',''))
            mx = max(xs, mx)
            counts.append(xs)
        sp = 0
        for i in range(N):
            sp += (mx - counts[i])
        
        #print(counts)
        print(sp)

main()

'''
Input:
4
XXXXBBBBBBBBBBBBBBBBXXXXX
XXXBBBBBBBBBBBBBBBXXXXXXX
XXXXXBBBBBBBBBBBBBBBBXXXX
XXBBBBBBBBBBBBBBBBBXXXXXX
2
XXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXX
1
XXXXXXXXXBBBBBBBBBBBBBBXX
0

Output:
4
0
0

'''
