class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numset={}
        for i in range(len(numbers)):
            if target-numbers[i] in numset:
                return [numset[target-numbers[i]], i+1]
            numset[numbers[i]]=i+1
