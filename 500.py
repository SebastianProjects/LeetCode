class Solution(object):
    def findWords(words):
        result = []
        is_in_row = [False] * 3 
        for word in words:
            for ch in word:
                if ch.lower() in "qwertyuiop":
                    is_in_row[0] = True
                elif ch.lower() in "asdfghjkl":
                    is_in_row[1] = True
                else:
                    is_in_row[2] = True
            if is_in_row.count(True) == 1:
                result.append(word)
            is_in_row = [False] * 3 
        return result