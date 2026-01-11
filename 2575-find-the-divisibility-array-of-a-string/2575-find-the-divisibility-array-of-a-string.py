class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        curr_div = 0 ## div at each iteration 
        output = []

        for i in word:
            num = int(i) ## convert string to num
            curr_div = (curr_div * 10 + num) % m ## get divisor at each iteration 
            if curr_div == 0: ## append according to req
                output.append(1)
            else:
                output.append(0)
        return output 
        