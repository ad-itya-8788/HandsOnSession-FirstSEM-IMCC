nums = [1,2,3,1,1,3]
count=1
n=len(nums)
for i in range(n):
  for j in range (i+1,n):
    if nums[i]==nums[j]:
      count+=1
print("Total Good pair is",count)
