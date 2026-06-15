class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numset={}
        for i in range(len(numbers)):
            if numbers[i] not in numset:
                numset[numbers[i]]= i
                if target-numbers[i] in numset:
                    res=[i+1, numset[target-numbers[i]]+1]
        return sorted(res)
