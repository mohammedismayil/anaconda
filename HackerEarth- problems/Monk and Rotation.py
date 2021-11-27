testCase = input()
for _ in range(len(testCase)):
    numberOfElements,numberOfSkips =input().split()
    # numbersArr = input()
    numberArray = list(map(int,input().split(' ')))
    newArr = []
    for i in range(len(numberArray)):
     if i <= (len(numberArray)) :
         if int(numberOfSkips) >  (len(numberArray)) :
          newArr.append(numberArray[i + int(numberOfSkips)])
         else:
              newArr.append(numberArray[i - int(numberOfSkips)])
    for i in newArr:
      print(i, end=" ")

# testCase  = int(input())
# for _ in range(testCase):
#     n,k = map(int,input().split())
#     l = list(map(int,input().split()))
#     x = k%n
#     print(*(l[n-x:]+l[:n-x]))