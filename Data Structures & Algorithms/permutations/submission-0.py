class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        idx_map={}
        arr= [1]*len(nums)
        for x in range(len(nums)):
            idx_map[nums[x]]=x
        fans = []
        def ps(ans,arr):
            f=True
            for x in nums:
                if arr[idx_map[x]]:
                    f=False
                    break
            if f:
                fans.append(ans.copy())
                return


            for x in nums:
                if arr[idx_map[x]]:
                    arr[idx_map[x]]=0
                    ans.append(x)
                    ps(ans,arr)
                    arr[idx_map[x]]=1
                    ans.pop()
        ps([],arr)
        return fans

