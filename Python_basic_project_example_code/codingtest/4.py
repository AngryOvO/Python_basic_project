for i in range(1,101):
    for j in range(2, i+1):
        if (j == i):
            print(i)
        elif (i % j == 0):
            break
