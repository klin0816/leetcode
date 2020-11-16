'''
45. Jump Game II
https://leetcode.com/problems/jump-game-ii/
Input: nums = [2,3,1,1,4]
Output: 2
Input: nums = [2,3,0,1,4]
Output: 2
'''
def jump(nums):
    if len(nums) <= 1:
        return 0
    i = 0
    jump = 0
    max_num = 0
    for n in range(len(nums)):
        if n > i:
            jump += 1
            i = max_num
        max_num = max(max_num, n+nums[n])
        
        if max_num == len(nums) - 1:
            return jump+1
    return jump


if __name__ == '__main__':
    nums = [2,3,0,1,4]
    result = jump(nums)
    print(f"nums: {nums}\nOutput: {result}")
