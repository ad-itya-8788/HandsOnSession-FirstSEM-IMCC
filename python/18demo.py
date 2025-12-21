#18. Using for loop demonstrate usage of continue, break and else 
for i in range(1, 6):
    if i == 2:
        continue
    if i == 5:
        break
    print(i)
else:
    print("loop completed")
