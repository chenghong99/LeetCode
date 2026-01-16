class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        ## each horizontal + vertical to be square. sort the bars in individually 
        ## get the maximum sub sequence for each array. 
        ## note that the sticks at the coners will not get removed
        hBars.sort()
        vBars.sort()
        h_max_seq, h_curr_seq = 1, 1
        v_max_seq, v_curr_seq = 1, 1

        for h in range(1, len(hBars)):
            if hBars[h] == hBars[h - 1] + 1:
                h_curr_seq += 1
            else:
                h_curr_seq = 1
            h_max_seq = max(h_curr_seq, h_max_seq)

        for v in range(1, len(vBars)):
            if vBars[v] == vBars[v - 1] + 1:
                v_curr_seq += 1
            else:
                v_curr_seq = 1
            v_max_seq = max(v_curr_seq, v_max_seq)
        return (min(h_max_seq, v_max_seq) + 1) ** 2