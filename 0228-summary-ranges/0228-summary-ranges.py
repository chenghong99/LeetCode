class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ## iterate store the head. once range broken update head
        output = []
        if len(nums) == 0:
            return output

        head = nums[0]
        tail = nums[0]

        for i in nums[1:]:
            if i == tail + 1:
                tail = i
            else:
                if head == tail:
                    output.append(str(head))
                else:
                    output.append(str(head) + "->" + str(tail))
                head, tail = i, i
        if head == tail:
            output.append(str(head))
        else:
            output.append(str(head) + "->" + str(tail))
        return output

        


        