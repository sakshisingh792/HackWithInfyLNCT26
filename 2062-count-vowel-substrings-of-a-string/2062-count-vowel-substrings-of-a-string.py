class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        n = len(word)
        count = 0
            
        for i in range(n):
            for j in range(i+1, n+1):
                sub = word[i:j]
                if  set(sub) ==vowels:
                    count += 1
        return count