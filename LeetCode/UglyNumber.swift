
// https://leetcode.com/problems/ugly-number/submissions/846153699/
class Solution {
     func isUgly(_ num: Int) -> Bool {
        var input = num
        if input <= 0 { return false }
        while input % 5 == 0 { input /= 5 }
        while input % 3 == 0 { input /= 3 }
        while input % 2 == 0 { input /= 2 }
        return input == 1 ? true : false
    }
}