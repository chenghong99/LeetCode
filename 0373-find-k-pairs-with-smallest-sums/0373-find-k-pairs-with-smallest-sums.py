import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        ans = []
        heapq.heapify(ans)
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                pairs = [nums1[i],nums2[j]]
                if len(ans)<k:
                    heapq.heappush(ans,[-(nums1[i]+nums2[j]),pairs])
                elif nums1[i]+nums2[j]<-ans[0][0]:
                        heapq.heappop(ans)
                        heapq.heappush(ans,[-(nums1[i]+nums2[j]),pairs])
                else:
                    break
        
        res = []
        for i in range(len(ans)):
            res.append(ans[i][1])
        
        return res
        