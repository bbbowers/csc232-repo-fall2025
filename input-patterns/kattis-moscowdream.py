# https://open.kattis.com/problems/moscowdream

def main():
    line = input()
    pcs = line.split()
    #print(pcs)

    #print(list(map(int, pcs)))

    a, b, c, n = map(int, pcs)
    if ( a >= 1 and b >= 1 and c >= 1 and a+b+c >= n and n >=3 ):
        print("YES")
    else:
        print("NO")

main()

'''
0 3 3 5

NO


4 10 6 13

YES

'''