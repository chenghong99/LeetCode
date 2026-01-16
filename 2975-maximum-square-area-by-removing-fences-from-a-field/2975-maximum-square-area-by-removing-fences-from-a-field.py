class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.append(1)
        hFences.append(m)
        vFences.append(1)
        vFences.append(n)
        hFences.sort()
        vFences.sort()

        h_len = []
        for i in range(len(hFences)):
            for j in range(i+1, len(hFences)):
                h_len.append(hFences[j] - hFences[i])
        
        v_len = []
        for i in range(len(vFences)):
            for j in range(i+1, len(vFences)):
                v_len.append(vFences[j] - vFences[i])

        max_edge = max(set(v_len) & set(h_len), default=0)
        return (max_edge ** 2) % (10**9 + 7) if max_edge != 0 else -1
        