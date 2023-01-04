
//https://leetcode.com/problems/delete-columns-to-make-sorted/submissions/871330126/

class Solution {
    func minDeletionSize(_ strs: [String]) -> Int {
     
        
        var arr = strs.map({Array($0)})
        
        print(arr)
        var count = 0
        for i in 0..<arr[0].count{
            
            
            for j in 1..<arr.count{

                
                if arr[j][i] < arr[j-1][i]{
                    count += 1
                    
                    break
                }
                
                

            }
            
        }
       
        
        
        
        
        return count
        
    }
}
