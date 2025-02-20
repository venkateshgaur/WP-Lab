class BubbleSort:
    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        n = len(self.nums)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.nums[j] > self.nums[j+1]:
                    self.nums[j], self.nums[j+1] = self.nums[j+1], self.nums[j]
        return self.nums

nums = [64, 34, 25, 12, 22, 11, 90]
sorter = BubbleSort(nums)
sorted_nums = sorter.sort()
print("Sorted array is:", sorted_nums)