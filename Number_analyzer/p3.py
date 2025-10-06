from p1 import list_num


sum = 0
for i in list_num:
    sum = sum + i
    
avg = sum/len(list_num)
    
print("avg of list: ",  avg)