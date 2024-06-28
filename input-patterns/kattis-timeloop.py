# https://open.kattis.com/problems/timeloop

def main():
    n = int( input() )

    for i in range(n):      #  for i in range(1, n+1):
        print(f'{i+1} Abracadabra')

main()


'''
Input:

5

Output:

1 Abracadabra
2 Abracadabra
3 Abracadabra
4 Abracadabra
5 Abracadabra

'''
