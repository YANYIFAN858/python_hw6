s=input()
w=input()

count=0
start=0

while True:
    loc=S.find(W,start)
    if loc==-1:
        break
    count+=1
    
start=loc+len(W)
    
print(count)
