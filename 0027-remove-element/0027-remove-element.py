class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ## get a tail reference to do swap 
        ## iterate through the array while curr != tail continue 
        ## if curr == val swap with tail 
        ## tail -= 1 and head stay 
        ## else head move 
        
        head = 0
        tail = len(nums) - 1
        
        if len(nums) == 0:
            return 0
        
        while head <= tail:
            if nums[head] == val:
                nums[head], nums[tail] = nums[tail], nums[head]
                tail -= 1
                
            else:
                head += 1
                
        return head
        