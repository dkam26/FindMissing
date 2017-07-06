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
              if i is list1[len(list1)-1]:
                  return list2[len(list2)-1]
    elif len(list1) is 0 and len(list2) is 0:
        return 0
    elif len(list1) is len(list2):
        count=0
        coun=0
        t=len(list1)
        t=t-1
        for i in range(t):
            if list1[i] is list1[i+1]:
                count=count+1
                print(count)
            if list2[i] is list2[i+1]:
                coun=coun+1
                print(coun)
        if coun is len(list2) or count is len(list1):
            return 'ty'


    else:
        
         for i in list2:
            for j in list1:
                if i is j:
                    Temp= Temp+1
            if Temp is 0:
                return i
            else:
              Temp=0
              if i is list2[len(list2)-1]:
                  return list1[len(list1)-1]
        
                
    

   
print(find_missing([0,0,0],[6,20,44]))