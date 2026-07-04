class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result_list = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
            l = i+1
            r = n-1
            target = -nums[i]
            while l<r:
                if nums[l]+nums[r]>target:
                    r -= 1
                elif nums[l]+nums[r]<target:
                    l += 1
                else:
                    result_list.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1

        return result_list
        