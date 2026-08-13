class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final_ans=[]
        def ps(nums,i,ans):
            if i==len(nums):
                final_ans.append(ans.copy())
                return
            ans.append(nums[i])
            ps(nums,i+1,ans)
            ans.pop()
            j=i
            while j<len(nums) and nums[j]==nums[i]:
                j+=1
            ps(nums,j,ans)
        ps(nums,0,[])
        return final_ans