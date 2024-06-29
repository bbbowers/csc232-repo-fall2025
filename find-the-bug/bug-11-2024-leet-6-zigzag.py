# FIND THE BUG (#11)
# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [ "" for i in range(numRows)]
        goingDown = True

        r = 0  # current row
        for c in s:
            rows[r] += c
            if goingDown:
                if r < numRows-1: r += 1
                else:
                    goingDown = not goingDown
                    r -= 1
            else:
                if r > 1: r -= 1
                else:
                    goingDown = not goingDown
                    r += 1
        
        return "".join(rows)


#print(Solution().convert("PAYPALISHIRING", 4))
#print("PINALSIGYAHRPI")
