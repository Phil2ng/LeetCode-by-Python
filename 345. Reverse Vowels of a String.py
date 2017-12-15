class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a': True, 'o': True, 'e': True, 'i': True, 'u': True, 'A': True, 'O': True, 'E': True, 'I': True,
                  'U': True}
        res = list(s)
        pos = []
        for i in range(len(res)):
            if res[i] in vowels:
                pos.append((i, res[i]))
        for j in range(int(len(pos) / 2)):
            res[pos[j][0]] = pos[len(pos) - j - 1][1]
            res[pos[len(pos) - j - 1][0]] = pos[j][1]
        return ''.join(res)
