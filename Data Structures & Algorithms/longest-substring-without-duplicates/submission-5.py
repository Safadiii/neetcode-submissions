class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        longest_so_far = 0
        left = 0
        
        for right_pos in range(len(s)):
            while s[right_pos] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[right_pos])
            longest_so_far = max(longest_so_far, right_pos - left + 1)
        return longest_so_far
            