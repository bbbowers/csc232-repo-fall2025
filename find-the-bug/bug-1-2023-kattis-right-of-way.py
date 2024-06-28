# FIND THE BUG
# https://open.kattis.com/problems/vajningsplikt

def main():
    a, b, c = input().split()

    DIRS = [ "North", "West", "South", "East" ]

    iA = DIRS.index(a)

    iRgt = (iA+1) % 4
    iOpp = (iA+2) % 4
    iLft = (iA+3) % 4

    if ( DIRS[iOpp] == b    # straight through
        and DIRS[iRgt] == c ):   # from right
        print("Yes")
    elif ( DIRS[iLft] == b
        and DIRS[iOpp] == c or DIRS[iRgt] == c):
        print("Yes")
    else:
        print("No")

main()

'''
South West East
Yes

South North North
No
'''
