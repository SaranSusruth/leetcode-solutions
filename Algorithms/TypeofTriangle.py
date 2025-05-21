class Solution(object):
    def triangleType(self, nums):
        nums.sort()
        if nums[0]+nums[1] <= nums[2]:
            return "none"
        elif nums[0] == nums[2]:
            return "equilateral"
        elif (nums[0] == nums[1] or nums[1] == nums[2]):
            return "isosceles"
        else:
            return "scalene"
sides = list(map(int,input("enter sides of a triangle seperated by coma: ").split(",")))
s= Solution()
print(s.triangleType(sides))