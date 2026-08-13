class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        fina_ans=[]
        def ps(nums,ans,i):
            if i==len(nums):
                fina_ans.append(ans.copy())
                return
            ans.append(nums[i])
            ps(nums,ans,i+1)
            ans.pop()
            ps(nums,ans,i+1)
        ps(nums,ans,0)
        return fina_ans

                          
        