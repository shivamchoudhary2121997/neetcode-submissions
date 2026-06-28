class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l<r:
            sumval = numbers[l]+numbers[r]
            if sumval==target:
                return [l+1,r+1]
            elif sumval>target:
                r -= 1
            else:
                l += 1