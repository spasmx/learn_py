class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in bracket_pairs.values():
                stack.append(char)
            elif char in bracket_pairs.keys():
                if not stack or stack.pop() != bracket_pairs[char]:
                    return False

        return len(stack) == 0

s = Solution()
print(s.isValid("[()()]]["))

