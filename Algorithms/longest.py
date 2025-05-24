class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ""
        strs.sort()
        print(strs)
        pref = strs[0]
        last = strs[-1]
        for i in range(len(pref)):
                if pref[i] == last[i]:
                    res = res + pref[i]
                else:
                    break
        return res

strs=["geeksforgeeks","geekezer","geek","geekofgod"]
s = Solution()
print(s.longestCommonPrefix(strs))
        