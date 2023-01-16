class Solution(object):
    ### any-order pattern recogonizing seems to be really hard to achieve
    ### Solution time:
    def wordSubsets(self, A, B):
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans
        ### Pretty much all solutions need such counter function to count the occurance of each letter.
        bmax = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in A:
            ls = count(a)
            for i in range(26):
                if ls[i] < bmax[i]:
                    break
            else: # execute if the for-loop ends without break
                ans.append(a)
        return ans
            
