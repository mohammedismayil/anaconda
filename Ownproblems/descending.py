arr = [1,4,6,7,2,10,22,89,5,90]

finalarr = []
# for i in range(0,len(arr)):
#      for j in range(0,len(arr)):
#          if i != len(arr) - 1 and j != len(arr) - 1:
#           if arr[i] > arr[j]:
#             tempvalue = arr[i]
            
#           else:
#             tempvalue = arr[j]


for j in range(0,len(arr) - 1):


    for i in range(0,len(arr) - 1):
      if arr[i] > arr[i + 1]:
        tempValue = arr[i]
      else:
         tempvalue = arr[i+1] 


    finalarr.append(tempvalue)       
    #  arr.remove(tempvalue)
    arr.remove(tempvalue)
    

print(arr)
print(finalarr)
             

