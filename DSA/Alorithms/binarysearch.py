def search(arr,x):
  left=0
  right=len(arr)-1
  while left<=right:
    mid=(left+right)//2
    if arr[mid]==x:
      return mid
    elif x<arr[mid]:
      right=mid-1
    else:
      left=mid+1
  return -1
arr=[1,2,3,4,5,6,7,8,9,10]
print("Search and return index of 8 index is",search(arr,8))