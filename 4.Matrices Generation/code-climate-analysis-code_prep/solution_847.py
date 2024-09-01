import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :return type: int
        """
        count_ele=collections.Counter(nums)
        return count_ele.most_common()[0][0]

result = Solution().majorityElement([10,10,20,30,40,10,20,10])
print(result)
