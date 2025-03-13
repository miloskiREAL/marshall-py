# Lesson 42
def posSum(nums, target):
    found = False
    if len(nums) == 1:
        if nums[0] == target:
            return True
        else:
            return False
    else:
        for n in nums:
            for u in nums:
                if n != u and u + n == target:
                    return True
        return False
inpNum = int(input("enter the number of terms: "))
nums = []
for n2 in range(inpNum):
    nums.append(int(input("enter a Number: ")))
target = int(input("enter the target "))
print(posSum(nums, target))



    