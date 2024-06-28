# FIND THE BUG (#9)
# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=30&page=show_problem&problem=985
# 10044 - Erdos Numbers


def computeNums(nums, coauths, name, curNum):
    q = []
    nums[name] = curNum
    q.append(name)

    while len(q) > 0:
        fst = q.pop()
        for auth in coauths[fst]:
            if auth not in nums:
                nums[auth] = nums[fst] + 1
                q.append(auth)
            

def main():
    T = int(input())

    for t in range(T):
        print(f'Scenario {t+1}')
        (P, N) = map(int, input().split())

        coauths = {}  # coauths[name] = {set of coauthors}

        for _ in range(P):
            line = input().split(".:")[0]
            authors = list(map(lambda n: n + ".", line.split("., ")))
            for auth in authors:
                others = set(authors)
                others.remove(auth)
                coauths[auth] = coauths.get(auth, set()).union(others)
        
        nums = { "Erdos, P." : 0 }  # nums[auth] = erdos#
        if "Erdos, P." in coauths:
            computeNums(nums, coauths, "Erdos, P.", 0)

        #print(nums)

        for _ in range(N):
            name = input()
            if name in nums:
                print(f'{name} {nums[name]}')
            else:
                print(f'{name} infinity')


main()



'''

Input:

1
4 3
Smith, M.N., Martin, G., Erdos, P.: Newtonian forms of prime factor matrices
Erdos, P., Reisig, W.: Stuttering in petri nets
Smith, M.N., Chen, X.: First oder derivates in structured programming
Jablonski, T., Hsueh, Z.: Selfstabilizing data structures
Smith, M.N.
Hsueh, Z.
Chen, X.


Output:

Scenario 1
Smith, M.N. 1
Hsueh, Z. infinity
Chen, X. 2

'''