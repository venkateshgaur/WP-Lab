
class ParenthesesValidator:
    def __init__(self, s):
        self.s = s

    def is_valid(self):
        stack = []
        matching_brackets = {')': '(', '}': '{', ']': '['}
        for char in self.s:
            if char in matching_brackets.values():
                stack.append(char)
            elif char in matching_brackets:
                if stack and stack[-1] == matching_brackets[char]:
                    stack.pop()
                else:
                    return False
        return not stack

s = "({[()]})"
validator = ParenthesesValidator(s)
result = validator.is_valid()
print("Is the string valid?", result)

s = "({[)]}"
validator = ParenthesesValidator(s)
result = validator.is_valid()
print("Is the string valid?", result)
