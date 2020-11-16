'''
32. Longest Valid Parentheses
https://leetcode.com/problems/longest-valid-parentheses/
Input: s = "(()"
Output: 2
Input: s = ")()())"
Output: 4
'''
def longestValidParentheses(s):
    if len(s) < 2:
        return 0
    i = 0
    stack = [-1]
    max_paired = 0
    
    while i < len(s):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not len(stack):
                stack.append(i)
            else:
                max_paired = max(max_paired, i-stack[-1])
        i += 1
    return max_paired


if __name__ == '__main__':
    s = "(()"
    output = longestValidParentheses(s)
    print(f"Input: {s}\nOutput: {output}")
