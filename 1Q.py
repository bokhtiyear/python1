def bitiwsmaker(n):
    count =0
    while(n):
        count+=1
        n>>= 1
        
    return count
    
number = int(input("enter a number:"))   
print("Total bit:",bitiwsmaker(number))
    
    
