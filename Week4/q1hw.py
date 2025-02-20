class SmallestElement:
    def __init__(self, nums):
        self.nums = nums

    def find_smallest(self):
        if not self.nums:
            return None
        smallest = self.nums[0]
        for num in self.nums[1:]:
            if num < smallest:
                smallest = num
        return smallest

nums = [10, 20, 4, 45, 99, 2]
element_finder = SmallestElement(nums)
smallest = element_finder.find_smallest()
print("The smallest element is:", smallest)