class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        left = 0
        right = 0
        s_len = len(s)
        tab = [0 for _ in range(256)]
        curr_len = 0
        last_f = 0
        
        while True:
            while right < s_len and tab[ord(s[right])] == 0:
                    curr_len += 1
                    tab[ord(s[right])] += 1
                    right += 1
            else:
                last_f = right
                max_len = max(max_len, curr_len)

            while left < s_len and last_f < s_len and s[left] != s[last_f]:
                tab[ord(s[left])] -= 1
                left += 1
                curr_len -= 1
            else:
                if s_len > 0:
                    tab[ord(s[left])] -= 1
                    left += 1
                    curr_len -= 1

            if left >= s_len or last_f >= s_len:
                break
                
        return max_len
