class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
       final_ans = []
       def ps(nums,ans,sum,i):
        if sum==target:
            final_ans.append(ans.copy())
            return
        if i==len(nums) or sum>target:
            return
        sum+=nums[i]
        ans.append(nums[i]) 
        ps(nums,ans,sum,i)
        sum-=nums[i]
        ans.pop()
        ps(nums,ans,sum,i+1)
       ps(nums,[],0,0)
       return final_ans
    