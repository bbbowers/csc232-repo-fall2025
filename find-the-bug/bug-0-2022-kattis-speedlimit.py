# FIND THE BUG
# https://open.kattis.com/problems/speedlimit

def main():
    n = int(input())
    
    last_time = 0
    dist = 0
    while (n != -1):
        for leg in range(n):
            (spd, tot_time) = map(int, input().split())
            cur_time = tot_time - last_time
            dist += spd * cur_time
            last_time = tot_time
        print(f"{dist} miles")
        
        n = int(input())

main()

