# FIND THE BUG (#3)
# https://open.kattis.com/problems/bitsequalizer

def main():
    N = int(input())
    for c in range(1, N+1):
        S = input()
        T = input()
        ones_misplaced = 0
        zeros_misplaced = 0
        ques_zeros = 0
        ques_ones = 0
        
        for i in range(len(S)):
            if S[i] == T[i]: continue  # go to next letter
            elif S[i] == '1': ones_misplaced += 1
            elif S[i] == '0': zeros_misplaced += 1
            elif S[i] == '?' and T[i] == '0': ques_zeros += 1
            elif S[i] == '?' and T[i] == '1': ques_ones += 1

        #print(ones_misplaced, zeros_misplaced, ques_ones, ques_zeros)
        
        # swap as many 0/1s as can
        moves = min(ones_misplaced, zeros_misplaced)
        ones_misplaced -= moves
        zeros_misplaced -= moves
        
        # may be still leftover 1s misplaced
        # - try to swap with ques_ones (and change those ?s to 0s)
        if ones_misplaced > 0:
            swaps = min(ones_misplaced, ques_ones)
            moves += swaps  # swap these ones into place
            moves += swaps  # and change those ? to 0
            ones_misplaced -= swaps   # should now be 0 !
            if ones_misplaced > 0:
                print(f"Case {c}: -1")
                continue
        
        moves += zeros_misplaced # change 0s to 1s
        moves += ques_zeros # make question marks 0s
        moves += ques_ones # make question marks 1s
        print(f"Case {c}: {moves}")

main()




'''
4
01??00
001010
01
10
110001
000000
0111000??110?0?
001100011000100
'''

