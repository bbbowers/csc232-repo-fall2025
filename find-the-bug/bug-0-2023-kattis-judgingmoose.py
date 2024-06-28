# FIND THE BUG
#https://open.kattis.com/problems/judgingmoose

def main():
    line = input()
    (a, b) = map(int, line.split())

    if a >= 0 and b >= 0: 
        if a == b:
            print("Even", (2 * b))
        elif a > b:
            print("Odd", (2 * a))
        else:
            print("Odd" ,(2 * b))
    else: 
        print("Not a moose")

main()
