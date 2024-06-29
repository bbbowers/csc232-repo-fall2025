# FIND THE BUG (#13)
# https://open.kattis.com/problems/centsavings


def priceround(p):
    return int(round(p + .1, -1))    # make it round 5 upwards


# opt(prices, i, d) is the minimum cost possible
#   for the first i items of prices
#   using up to d dividers
def solve(prices, i, d):
    if i == 0: ret = 0   # using no items
    elif d == 0: ret = priceround(sum(prices[0:i]))
    else:
        # choose to use a divider right before the i'th item or not...
        noDiv  = solve(prices, i-1, d) + prices[i-1]
        useDiv = priceround(solve(prices, i-1, d-1)) + prices[i-1]

        ret = min(noDiv, useDiv)

    #print(f'solve({c}, {i}, {d}): {ret}')
    return ret


# this is the dynamic programming version of the recursive
# algorithm above
def solvedp(prices, d):
    n = len(prices)
    opt = [[0 for k in range(d+1)] for i in range(n+1)]

    for k in range(d+1): opt[0][k] = 0  # first 0 items
    for i in range(n+1): opt[i][0] = sum(prices[0:i]) # first i items; no divider
                                                      # should just be the sum of 
                                                      # the first i items
    for i in range(1, n+1):
        for k in range(d, -1, -1):
            noDiv = opt[i-1][k] + prices[i-1]
            useDiv = priceround(opt[i-1][k-1]) + prices[i-1]
            opt[i][k] = min(noDiv, useDiv)

    # print(opt)        # HINT: look at this to debug
    return opt[n][d]


def main():
    (n, d) = map(int, input().split())
    prices = list(map(int, input().split()))

    print(priceround(solve(prices, n, d)))  # will probably TLE
    #print(priceround(solvedp(prices, d)))
    



main()