class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # print(nums)
        # [-1, 0, 1, 2, -1, -4]
        nums.sort()
        # print(nums)
        sum_nums = 0
        for i in range(len(nums)-2):

            left, right = i + 1, len(nums)-1
            while left < right:
                sum_nums = nums[i] + nums[left] + nums[right]
                if sum_nums == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    right = right - 1
                    left = left + 1
                elif sum_nums > 0:
                    right = right - 1
                elif sum_nums < 0:
                    left = left + 1

        return list(set(list(map(tuple,result))))