class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        fwd_prod = [1] * size
        bwd_prod = [1] * size

        curr_prod = 1
        for i in range(0,size):
            fwd_prod[i] = curr_prod
            curr_prod = curr_prod*nums[i]

        curr_prod = 1
        for i in range(size-1,-1,-1):
            bwd_prod[i] = curr_prod
            curr_prod =curr_prod*nums[i]

        res = [1]*size
        for i in range(0,size):
            res[i] = bwd_prod[i]*fwd_prod[i]
        return res


            


        