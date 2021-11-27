arr = [112,189,1,4,6,7,2,10,22,223,89,5,90]

finalarr = []
tempvalue = 0
# for j in range(0,len(arr) - 1):


#     for i in range(0,len(arr) - 1):
#       if i <= len(arr) - 1 and j <= len(arr) - 1:
#        if arr[i] > arr[j+1]:
#         tempValue = arr[i]
#         # arr.remove(arr[j])
#         # finalarr.append(tempvalue)
#        else:
#          tempvalue = arr[j+1] 
#         #  arr.remove(arr[i])
#         #  finalarr.append(tempvalue)


#       print(tempvalue)
    
    
#     # finalarr.remove(tempvalue)    
      
#     #  arr.remove(tempvalue)
#     # arr.remove(tempvalue)
    
for k in range(0,len(arr) - 1):
 for i in range(0,len(arr) - 1):
    for j in range(0,len(arr) - 1):
      if i <= len(arr) - 1 and j <= len(arr) - 1 :
       print('iteration',i,j,k)
       if arr[i] > arr[j+1] and arr[i] > tempvalue:
        tempValue = arr[i]
        # print(tempvalue)
        # arr.remove(arr[j])
        # finalarr.append(tempvalue)
       elif arr[j+1] > tempvalue:
         tempvalue = arr[j+1] 
        #  print(tempvalue)
    arr.remove(tempvalue)
 
 finalarr.append(tempvalue)


print(tempvalue)
print(finalarr)
             

