class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        par_stack = [None]
        par_dict = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in par_dict:
                if par_dict[c] != par_stack.pop():
                    return False
            else:
                par_stack.append(c)
        return par_stack.pop() is None


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("([)]"))
