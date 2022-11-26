func checkRepeating(){
    
    var values = [2,1,2,1,8]





    for i in 0..<values.count{
        
        print(values.filter({$0 == i}))
        if values.filter({$0 == values[i]}).count == 1{
            print(values[i])
            
           
        }
    }

}
print(checkRepeating())