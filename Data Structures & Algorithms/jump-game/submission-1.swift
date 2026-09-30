class Solution {
    func canJump(_ nums: [Int]) -> Bool {
        var possible = Array(repeating:false,count:nums.count)
        possible[nums.count-1]=true
        for i in (0..<nums.count).reversed(){
           
            for dx in 0...nums[i]{
                 var d = i+dx
                 if(d>=nums.count) {
                    possible[i]=true
                    break
                    }else{
                        if(possible[d]==true)
                        {
                            possible[i]=true
                            break
                        }
                    }

            }
            
           

        }
        if(possible[0]==true) {return true}
        return false
    }
}
