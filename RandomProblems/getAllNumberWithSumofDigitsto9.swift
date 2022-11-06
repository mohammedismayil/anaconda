

func addSumOfDigits(digits:Int)->Int{
    
    var sum = 0
    
    var totalDigits = digits.description.compactMap({$0.wholeNumberValue})
    
    
    for i in 0..<totalDigits.count{
       
        sum = sum + totalDigits[i]
    }

    
    return sum
    
}
func checkAscending(digits:Int)->Bool{
    
   
    
    var totalDigits = digits.description.compactMap({$0.wholeNumberValue})
    
    var current = totalDigits[0]
    
    var isAscending = true
    for i in 0..<totalDigits.count{
       
        if i + 1 < totalDigits.count {
            if current < totalDigits[i+1]{
                current = totalDigits[i]
                isAscending = true
            }else{
                isAscending = false
            }
        }
       
    }

    
    return isAscending
    
}


func main(){
    for i in 0..<999{
    
    
    if addSumOfDigits(digits:i) == 9 && checkAscending(digits:i) {
//        print(addSumOfDigits(digits:i))
        print(i)
    }
   
}

}