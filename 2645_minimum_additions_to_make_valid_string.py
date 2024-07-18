class Solution(object):
    def addMinimum(self, word):
        count = 0
        w_len = len(word)
        i = 0
        while i < w_len:
            if word[i] == "a":
                if i + 1 >= w_len:
                    count += 2
                elif word[i + 1] == "b":
                    i += 1
                    if i + 1 >= w_len or word[i + 1] != "c":
                        count += 1
                    else:
                        i += 1
                elif word[i + 1] == "c":
                    count += 1
                    i += 1
                else:
                    count += 2

            elif word[i] == "b":
                if i + 1 >= w_len or word[i + 1] != "c":
                    count += 1
                else:
                    i += 1
                if i - 1 <= 0 or word[i - 1] != "a":
                    count += 1
            
            elif word[i] == "c":
                count += 2

            i += 1

        return count
        