def find_missing(list1,list2):
    Temp=0
    if len(list1)<len(list2):
        for i in list1:
            for j in list2:
                if i is j:
                    Temp= Temp+1
            if Temp is 0:
                return i
            else:
              Temp=0
    else:
        
         for i in list2:
            for j in list1:
                if i is j:
                    Temp= Temp+1
            if Temp is 0:
                return i
            else:
              Temp=0
        
                
    

   
print(find_missing([1,2],[1,2,54]))