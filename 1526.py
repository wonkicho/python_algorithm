N = int(input())

while True:
    ret = True
    
    for i in str(N,0,1):
        if i != "4" and i != "7":
            ret = False
            
    if ret:
        print(N)
        break