class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        count1 = [0] * 26
        count2 = [0] * 26
        for i in ransomNote:
            count1[ord(i) - ord('a')] += 1
        for i in magazine:
            count2[ord(i) - ord('a')] += 1
        for i in range(26):
            if count1[i] > count2[i]:
                return False
        return True
