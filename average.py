def average_num(num):
    sum= 0
    for i in num:
        sum= sum+i
        avg= sum/len(num)
    
    if len(num)== 0:
        return None

    elif len(num)!= 0:
        return avg


print(average_num([1,2,3,4]))     

 

