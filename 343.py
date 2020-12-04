'''
343. Integer Break
https://leetcode.com/problems/integer-break/submissions/
Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1
Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

note: 2 <= n <= 58
'''
# def function():
def integerBreak(n):
    if n == 2: return 1
    result = 0
    for i in range(2, n):
        _list = [n//i] * i

        for i in range(n%i):
            _list[i] += 1

        _result = _list[0]
        for i in range(1, len(_list)):
            _result *= _list[i]
        if _result <= result:
            return result
        result = _result

    return result

if __name__ == '__main__':
    Input = 2
    Output = integerBreak(Input)
    print(f"Input: {Input}\nOutput: {Output}")
