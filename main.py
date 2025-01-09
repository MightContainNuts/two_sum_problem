from typing import Tuple

from typing import List, Tuple, Optional

def find_indices(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    seen = {}  # Dictionary to store numbers we've already seen and their indices
    for index, num in enumerate(nums):
        complimentary_num = target - num
        print(index, num, seen)
        if complimentary_num in seen:
            return (seen[complimentary_num], index)
        seen[num] = index

    return None  # Return None if no pair is found



if __name__ == '__main__':
    idx = find_indices([1,3,5], 8)
    print(idx)
