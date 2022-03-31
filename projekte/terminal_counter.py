n = 0
while n <= 300:
    if n < 10:
        print("0",n,"|", end = '', sep='')
        n = n + 1
    else:
        print(n,"|", end = '', sep='')
        n = n + 1