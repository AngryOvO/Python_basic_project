i , k = 0,0
guguline = ""

for i in range(2,10):
    guguline = guguline + ("#    %d단    #  " %i)

print(guguline)

guguline = ""

for i in range(1,10,1):
    for k in range(2,10,1):
        guguline = guguline + ("%2d X %2d = %2d "%(k,i,k*i))
    print(guguline)
        
