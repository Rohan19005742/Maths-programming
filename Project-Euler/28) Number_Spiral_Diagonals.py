def solve(n):
    total = 0
    count = 3
    for x in range(1,n,2): #top right
        total+= count*count
        count+=2
    
    count = 4
    prev = 1
    for x in range(1,n,2): # bottom left
        total+=count+prev
        prev+=count
        count+=8

    count = 6
    prev = 1
    for x in range(1,n,2): # top left
        total+=count+prev
        prev+=count
        count+=8

    count = 2
    c2 = 1
    for x in range(1,n,2): # bottom right
        total+=count*count-c2
        count+=2
        c2+=2
    
    print(total+1)
    

    

    

solve(1001)