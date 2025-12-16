def infinite_chai ():
    count = 1
    while True:
        yield f"Refil # {count}"
        count +=1
    
refill = infinite_chai()
for i in range(5):
    print(next(refill))