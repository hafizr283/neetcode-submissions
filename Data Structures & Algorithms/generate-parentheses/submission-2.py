class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        nums=['(']*n+[')']*n
        print(nums)
        def isok(brackets):
            stack=deque()
            for x in brackets:
                if x=='(':
                    stack.append(x)
                else:
                    if stack:
                        stack.pop()
                    else:
                        return False
            return not stack
        fans=[]
        def permutation(nums,i,opening_brac,closing_brac):
            if i==len(nums):
                if opening_brac==closing_brac:
                    fans.append(''.join(nums))
                return
            if closing_brac>opening_brac:
                return
            vis =[]
            for x in range(i,len(nums)):
                if nums[x] in vis:
                    continue
                vis.append(nums[x])
                if nums[x]==')':
                    closing_brac+=1
                else:
                    opening_brac+=1
                nums[i],nums[x]=nums[x],nums[i]
                permutation(nums,i+1,opening_brac,closing_brac)
                nums[i],nums[x]=nums[x],nums[i]
                if nums[x]==')':
                    closing_brac-=1
                else:
                    opening_brac-=1
                
        permutation(nums,0,0,0)
        return list(set(fans))
                



        

