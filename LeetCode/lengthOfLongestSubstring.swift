

// https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/845338926/
class Solution {
func lengthOfLongestSubstring(_ s: String) -> Int {
    
    var sArray = s.map { String($0) }
    
    var maxLength = 0
    for i in 0..<sArray.count{
        
     
        var currentElements = [String]()
        if sArray.count == 1 {
            return 1
        }
        for j in 0..<sArray.count - i{
            
            if !currentElements.contains(sArray[i+j]){
                currentElements.append(sArray[i+j])
               
            }else{
                break
            }
            
            if currentElements.count > maxLength{
                maxLength = currentElements.count
                
            }
            
        }
        
       
    }
    
    return maxLength
}

}