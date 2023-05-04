from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pick midpoint, look at element at midpoint index
        # if element is lower than target, move low = mid, keep high
        # repeat until element is found or low == high
        low, high = 0, len(nums) - 1
        counter = len(nums) - 1
        while low < high and counter > 0:
            mid = low + (high - low) // 2
            print(f"low={low} mid={mid} high={high}")
            if nums[mid] == target:
                print(f"found target. mid={mid}")
                return mid
                # break
            elif nums[mid] < target:
                low = mid + 1
                print(f"moved low. low={low} mid={mid} high={high}")
                # return 'premature exit 1'
            elif nums[mid] > target:
                high = mid - 1
                print(f"moved high. low={low} mid={mid} high={high}")
            counter -= 1
        return -1

    def test(self, nums: List[int], target: int) -> int:
        while nums:
            if nums[-1] == target:
                return target
            nums = nums[: len(nums) // 2]


"""
low hi  mid         n[mid]  if/elif1/elif2
0   5   0+5//2 = 2  3       elif1
2   5   2+3//2 = 3  5       elif1
3   5   3+2//1 = 4  4       if

"""

if __name__ == "__main__":
    cases = [
        ([-1, 0, 3, 5, 9, 12], 9),
        ([-1, 0, 3, 5, 9, 12], 2),
        ([-1, 0, 3, 5, 9, 12], 3),
    ]
    s = Solution()
    print([s.search(*case) for case in cases])
    print([s.test(*case) for case in cases])
