nums = [-1,2,1,-4]
target = 1

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        la = []
        dis = 0
        maxxxx = 999999999
        for i in range(1, len(nums)-1):
            sol = 0
            if nums[i] + nums[i-1] + nums[i+1] == target:
                return num[i]

            else:
                sol = nums[i] + nums[i-1] + nums[i+1]
                dis = abs(target-sol)
                if dis < maxxxx:
                    maxxxx = dis
                else:
                    pass
                return nums[i]








