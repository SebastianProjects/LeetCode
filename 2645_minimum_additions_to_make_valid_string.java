class Solution {
    public int addMinimum(String word) {
        int count = 0;
        int w_len = word.length();
        int i = 0;
        while (i < w_len) {
            if (word.charAt(i) == 'a') {
                if (i + 1 >= w_len) {
                    count += 2;
                } else if (word.charAt(i + 1) == 'b') {
                    ++i;
                    if (i + 1 >= w_len || word.charAt(i + 1) != 'c') {
                        ++count;
                    } else {
                        ++i;
                    }
                } else if (word.charAt(i + 1) == 'c') {
                    ++count;
                    ++i;
                } else {
                    count += 2;
                }
            } else if (word.charAt(i) == 'b') {
                if (i + 1 >= w_len || word.charAt(i + 1) != 'c') {
                    ++count;
                } else {
                    ++i;
                }
                if (i - 1 < 0 || word.charAt(i - 1) != 'a') {
                    ++count;
                }
            } else {
                count += 2;
            }
            ++i;
        }
        return count;
    }
}