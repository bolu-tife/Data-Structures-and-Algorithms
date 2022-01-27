# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        l = len(a)-1
        r = len(b)-1
        output = []
        while l >= 0 or r >= 0:
            tot = 0
            if l >= 0:
                tot += int(a[l])
                l -= 1
            if r >= 0:
                tot += int(b[r])
                r -= 1
            tot += carry
            
            output.append(str(tot%2))
            carry = tot // 2
            
        if carry:
            output.append(str(carry))
        output.reverse()
        return "".join(output)
                
           