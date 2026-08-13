class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        final_ans=[]
        def ps(ans,nums,i,sum):
            if sum==target:
                final_ans.append(ans.copy())
                return
            if i==len(nums) or sum>target:
                return
            ans.append(nums[i])
            ps(ans,nums,i+1,sum+nums[i])
            ans.pop()
            j=i
            while j<len(nums) and nums[j]==nums[i]:
                j+=1
            ps(ans,nums,j,sum)
        ps([],candidates,0,0)
        return final_ans
            


        