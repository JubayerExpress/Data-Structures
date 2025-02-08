def is_balanced_parentheses(s):
    stack = []
    opening = set('({[')
    closing = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack[-1] != closing[char]:
                return False
            stack.pop()
    return not stack

# Test cases
print(is_balanced_parentheses("({[]})"))  # True
print(is_balanced_parentheses("([)]"))    # False

