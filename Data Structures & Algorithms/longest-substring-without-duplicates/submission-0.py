class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Since we want to find the longest substring, we shall use a sliding window.

        However, we want to keep track of each substring's length, hence, we'll need
        a quick access hash set to memorize as we go.
        """
        char_set = set()
        l = 0
        longest = 0
        
        for r in range(len(s)):
            # Update window since its a window s[r] is a reapeating character 
            # already seen in the window, i.e. it violated the sliding window constraints.
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            # Expand the window to include new elements.
            # At this point, char_set is free of duplicates.
            char_set.add(s[r])

            # Compute longest substring by getting the max of previous
            # longest substring and current window.
            longest = max(longest, (r - l) + 1)

        return longest
