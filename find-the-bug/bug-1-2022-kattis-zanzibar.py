# FIND THE BUG
# https://open.kattis.com/problems/zanzibar

def main():
    n = int(input())

    for i in range(n):
        pops = list(map(int, input().split()))[:-1] # remove the last element (the extra 0)
        imports = 0

        # work through the list, comparing consecutive elements...
        cur = pops.pop(0)
        while len(pops) > 1:
            next = pops.pop(0)
            if next > 2 * cur: imports += (next - 2 * cur)
            cur = next
        
        print(imports)

main()

