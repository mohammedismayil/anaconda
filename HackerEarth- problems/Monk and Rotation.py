testCase = 4

numberOfElements = 5

numberOfSkips = 3

numberArray = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
newArr = []
indexArr = []
for i in range(len(numberArray)):
    # print(numberArray)
    indexArr.append(i)
    if i <= (len(numberArray) - 1) :
     newArr.append(numberArray[i - 10])
 
print(indexArr) 
print(newArr)    
    











