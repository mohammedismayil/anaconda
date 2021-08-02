testCase = 4

testCase = input()
numberOfElements,numberOfSkips =input().split()
numbersArr = input()
numberArray = list(map(int,numbersArr.split(' ')))
newArr = []
for i in range(len(numberArray)):
    if i <= (len(numberArray) - 1) :
     newArr.append(numberArray[i - int(numberOfSkips)])  
for i in newArr:
    print(i, end=" ")












