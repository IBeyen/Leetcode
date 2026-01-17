class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        #min, max, argmin, argmax 
        mini_maxi_left = []
        mini_maxi_right = []

        for i in range(len(nums)):
            right_i = len(nums)-i-1
            if i == 0:
                mini_maxi_left.append([nums[i], nums[i], i, i])
                mini_maxi_right.append([nums[right_i], nums[right_i], right_i, right_i])
            else:
                mini_maxi_left.append(
                    [
                        min(nums[i], mini_maxi_left[-1][0]), 
                        max(nums[i], mini_maxi_left[-1][1]),
                        i if nums[i] < mini_maxi_left[-1][0] else mini_maxi_left[-1][2],
                        i if nums[i] > mini_maxi_left[-1][1] else mini_maxi_left[-1][3],
                    ]
                )
                mini_maxi_right.append(
                    [
                        min(nums[right_i], mini_maxi_right[-1][0]), 
                        max(nums[right_i], mini_maxi_right[-1][1]),
                        right_i if nums[right_i] < mini_maxi_right[-1][0] else mini_maxi_right[-1][2],
                        right_i if nums[right_i] > mini_maxi_right[-1][1] else mini_maxi_right[-1][3],
                    ]
                )
        mini_maxi_right.reverse()

        for d in range(indexDifference, len(nums)):
            if abs(mini_maxi_right[d][1] - mini_maxi_left[d-indexDifference][0]) >= valueDifference:
                return [mini_maxi_right[d][3], mini_maxi_left[d-indexDifference][2]]
            elif abs(mini_maxi_right[d][0] - mini_maxi_left[d-indexDifference][1]) >= valueDifference:
                return [mini_maxi_right[d][2], mini_maxi_left[d-indexDifference][3]]
        return [-1, -1]

        