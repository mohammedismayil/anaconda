from itertools import permutations
 

# if __name__ == '__main__':
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())
    # fruits = ["apple","orange","strawberry","pineapple"]
    # newlist = [a  if a != "apple" else "salad" for a in fruits]
    
    # Get all permutations of [1, 2, 3]
# perm = permutations([0,x, y, z])
# print(list(perm))
# Print the obtained permutations
arr = []
perm = permutations([1,1,2])
# print(list(perm))
for i in list(perm):
    sum = 0
    # print(i)
    for j in i:
        print(j)
        sum = sum + j 
        if sum < 10000:
         arr.append(i)
            
   
print(arr)



