class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        from heapq import heappush, heappop
        heap = [(nums1[0] + nums1[0], (0, 0))]
        ans = []
        visited = set()

        while len(ans) < k:
            val, (pos1, pos2) = heappop(heap)
            ans.append([nums1[pos1], nums2[pos2]])

            if pos1 + 1 < len(nums1) and (pos1 + 1, pos2) not in visited:
                visited.add((pos1 + 1, pos2))
                heappush(heap, (nums1[pos1 + 1] + nums2[pos2], (pos1 + 1, pos2)))

            if pos2 + 1 < len(nums2) and (pos1, pos2 + 1) not in visited:
                visited.add((pos1, pos2 + 1))
                heappush(heap, (nums1[pos1] + nums2[pos2 + 1], (pos1, pos2 + 1)))

        return ans


        