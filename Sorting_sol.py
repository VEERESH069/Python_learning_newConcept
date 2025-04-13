# Merge 2 sorted arrays
def merge(nums1, nums2):
        for i in range(n):
            nums1.pop()
        nums1.extend(nums2)
        nums1.sort()
num = list(map(int,input().split()))
num1 = list(map(int,input().split()))
merge(num, num1)

# Majority Element
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3

def majorityElement(nums):
        nums.sort()
        n = len(nums)
        return nums[n//2]
k = list(map(int,input().split()))
majorityElement(k)

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

def sortColors(nums):
        count = [0] * 3
        for num in nums:
            count[num] += 1

        index = 0
        for i in range(3):
            while count[i] > 0:
                nums[index] = i
                index += 1
                count[i] -= 1
num2 = list(map(int,input().split()))
sortColors(num2)

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6]

def mergi(intervals):
        if not intervals:
            return []

        # Sort intervals by their start time
        intervals.sort(key=lambda x: x[0])

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            last_added_interval = result[-1]
            if last_added_interval[1] >= intervals[i][0]:
                last_added_interval[1] = max(last_added_interval[1], intervals[i][1])
            else:
                result.append(intervals[i])
        return result
inte = list(map(int,input().split()))
mergi(inte)

# Insertion Sort
def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i] 
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
n = int(input())
array = list(map(int, input().split()))[:n]
insertionSort(array)
print(*array)

