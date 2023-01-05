class Solution {
    func findMinArrowShots(_ points: [[Int]]) -> Int {
     
        
        let sorted = points.sorted(by: {$0[0] < $1[0] })
        var count = 1
        
        var currentEnd = sorted[0][1]
        
        for i in 1..<sorted.count{
            
            
            if sorted[i][0] >= currentEnd {
                currentEnd = sorted[i][1]
                
                count += 1
            }
        }
        
        return count
        
    }
}
let sol = Solution()

sol.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]])


