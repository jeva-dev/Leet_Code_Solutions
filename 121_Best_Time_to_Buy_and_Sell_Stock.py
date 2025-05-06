prices = [7,1,5,3,6,4]
out = 0
for i in range(0, len(prices)):
    for j in range(i+1, len(prices)):
        if i<j:
            out = i
        else:
            continue
print(out)