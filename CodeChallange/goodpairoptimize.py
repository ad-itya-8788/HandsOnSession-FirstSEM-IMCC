nums = [1,2,3,1,1,3]
d={}
pair=0
for x in nums:
  pair+=d.get(x,0)
  d[x]=d.get(x,0)+1
print(pair)

