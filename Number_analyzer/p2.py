from p1 import list_num

max_num = []
min_num = []
find_num = int(input("Enter number for max and min :"))

if find_num:
    
    for i in list_num:
        if i > find_num: 
            max_num.append(i)
            
        else:
            min_num.append(i)
            
print("max number: ",max_num)
print("min number: ",min_num)