class Solution {
    func isUgly(_ n: Int) -> Bool {
        if n == 1 || n % 5 == 0 {
            return true
        }else{
            var final = false
            for i in 1..<n{
                
                if n % i == 0 && i != n && ((n / i ) > 1)  {
                  final = false
                  
                }else if (i != n && n % 2 != 0){
                    final = true
                    
                }

            }
            return final
        }
    }
}