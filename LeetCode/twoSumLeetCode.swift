// https://leetcode.com/problems/two-sum/submissions/842019511/

class Solution {
    
func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
       
    
    
    for i in 0..<nums.count{
        
     
        
        for j in 1..<nums.count - i {
            
            if nums[i]+nums[i+j] == target{
                return [i,i+j]
            }else{
                
              
            }
        }
    }
    
    return [0,1]
   }
}