class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beg_index = 0
        end_index = len(nums) - 1

        while beg_index <= end_index:
            midpoint = beg_index + (end_index - beg_index) // 2
            midpoint_value = nums[midpoint]
            if midpoint_value == target:
                return midpoint
            elif target < midpoint_value:
                end_index = midpoint - 1
            else:
                beg_index = midpoint + 1
        return -1
    