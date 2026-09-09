class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        current_length=0
        longest_length=0
        for num in s:
            if num-1 not in s:
                current_length=1
                current_num=num
                longest_length=max(current_length,longest_length)
                while current_num+1 in s:
                    current_num+=1
                    current_length+=1
                    longest_length=max(current_length,longest_length)
        return longest_length