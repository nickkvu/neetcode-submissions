class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : 
            return False

        word1 = defaultdict(int)
        word2 = defaultdict(int)

        for letter in s :
            word1[letter] += 1

        for letter in t :
            word2[letter] += 1
        
        return word1 == word2