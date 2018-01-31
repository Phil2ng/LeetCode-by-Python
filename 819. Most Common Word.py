import string

from matplotlib import collections


class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        counter = collections.defaultdict(int)
        max_record = (0, "")
        for word in paragraph.split():
            # Notice the usage of translate function
            translator = str.maketrans("", "", string.punctuation)
            word = word.lower()
            word = word.translate(translator)
            if word not in banned:
                counter[word] += 1
                max_record = max(max_record, (counter[word], word))
        return max_record[1]
