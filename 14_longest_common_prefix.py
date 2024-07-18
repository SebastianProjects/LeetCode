class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ""
        strs.sort()

        first_str = strs[0]
        last_str = strs[-1]

        min_len = min(len(first_str), len(last_str))

        for i in range(min_len):
            if first_str[i] != last_str[i]:
                return result
            result += first_str[i]
        return result