class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        ## convert both to sets, find overlap between both, take those elem from the set of shorter length. 
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        overlap = [num for num in nums1_set if num in nums2_set]

        remaining_set1 = min(len(nums1_set) - len(overlap), len(nums1) // 2)
        remaining_set2 = min(len(nums2_set) - len(overlap), len(nums2) // 2)
        overlap_set1 = min((len(nums1) // 2 - remaining_set1), len(overlap))
        overlap_set2 = min((len(nums2) // 2 - remaining_set2), len(overlap) - overlap_set1)
        return remaining_set1 + remaining_set2 + overlap_set1 + overlap_set2

      