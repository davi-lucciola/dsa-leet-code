class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters_set = set(t)
        for letter in letters_set:
            if s.count(letter) != t.count(letter):
                return False
        
        return True
        