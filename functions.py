 
def swap_case(s,endresult):

    for i in range(0,str(s).count(s)):
    
     if str(s[i]).isupper:
         endresult = (endresult + str(s[i].lower))
     else:
         endresult = (endresult + str(s[i].upper))
     print(str(endresult))    
     return str(endresult)
     

if __name__ == '__main__':
    s = input()
    endresult = ''
    result = swap_case(s,endresult)
    print(result)
     
        