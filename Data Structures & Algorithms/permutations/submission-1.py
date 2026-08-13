class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        fans = []
        def ps(nums,i):
            if i==len(nums)-1:
                fans.append(nums.copy())
                return
            for x in range(i,len(nums)):
                nums[i],nums[x]=nums[x],nums[i]
                ps(nums,i+1)
                nums[i],nums[x]=nums[x],nums[i]
        ps(nums,0)
        return fans
        


