from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        record = set()

        for number in nums:
            if number in record:
                return True
            else:
                record.add(number)
        return False


if __name__ == '__main__':
    print(Solution().containsDuplicate([1, 2, 3, 4]))
    print(Solution().containsDuplicate([1, 1, 4, 3, 4]))
