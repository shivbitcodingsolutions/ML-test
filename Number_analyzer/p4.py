from p1 import list_num


even = []
count_even = 0
odd = []
count_odd = 0


for i in list_num:
    
    if i%2==0:
        even.append(i)
        
    else:
        odd.append(i)
        

print("even num : ", even)

print("odd num : ", odd)


for i in even:
    count_even+=1
    
for i in odd:
    count_odd+=1
        
print("count of even : ", count_even)
print("count of odd : ", count_odd)

