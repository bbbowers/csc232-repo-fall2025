# FIND THE BUG (#7)
# https://open.kattis.com/problems/abc

def main():
    abc = ['A', 'B', 'C']
    numbers = list(map(int, input().split()))
    order = list(input())
    numbers.sort()
    sortedNumbers = map(str, numbers)
    dct = dict(zip(order, sortedNumbers))
    answer = " ".join([dct[x] for x in order])
    print(answer)

main()
