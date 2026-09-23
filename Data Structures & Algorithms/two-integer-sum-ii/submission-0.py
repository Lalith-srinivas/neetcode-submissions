class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start=0
        end=len(numbers)-1
        while start<end:
            need=numbers[start]+numbers[end]
            if need==target:
                return [start+1,end+1]
                break
            elif need<target:
                start+=1
            else:
                end-=1