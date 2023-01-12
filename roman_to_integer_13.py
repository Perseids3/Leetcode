class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        out = 0
        for i in range(len(s)):
            if s[i] == 'I':
                if i == len(s)-1:
                    out +=1
                    pass
                elif s[i+1] =='V':
                    out -=1
                   
                elif s[i+1] =='X':
                    out -=1
                    
                else:
                    out +=1
            elif s[i] == 'V':
                out +=5
            elif s[i] == 'X':
                if i == len(s)-1:
                    out +=10
                    pass
                elif s[i+1] =='L':
                    out -=10
                
                elif s[i+1] =='C':
                    out -=10
                    
                else:
                    out +=10
            elif s[i] == 'L':
                out +=50
            elif s[i] == 'C':
                if i == len(s)-1:
                    out +=100
                    pass
                elif s[i+1] =='D':
                    out -=100
                    
                elif s[i+1] =='M':
                    out -=100
                    
                else:
                    out +=100
            elif s[i] == 'D':
                out +=500
            elif s[i] == 'M':
                out +=1000

        return out


### This is my ugly solution. We can have solutions like:
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         translations = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         number = 0
#         s = s.replace("IV", "IIII").replace("IX", "VIIII")
#         s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#         s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
#         for char in s:
#             number += translations[char]
#         return number

### OR:

# values = {
#     "I": 1,
#     "V": 5,
#     "X": 10,
#     "L": 50,
#     "C": 100,
#     "D": 500,
#     "M": 1000,
# }

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         total = 0
#         i = 0
#         while i < len(s):
#             # If this is the subtractive case.
#             if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
#                 total += values[s[i + 1]] - values[s[i]]
#                 i += 2
#             # Else this is NOT the subtractive case.
#             else:
#                 total += values[s[i]]
#                 i += 1
#         return total