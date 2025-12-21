#21. Write a Python program to sort a list of dictionaries by the age key in ascending and descending order. Then filter out dictionaries where the age is below 18.

stud=[{"name":'aditya',"age":22},{"name":"mayur","age":16},{"name":"sham","age":33},{"name":"Ravi","age":43}]

print("Ascending order:",sorted(stud,key=lambda x :x["age"]))

print("Descending:",sorted(stud,key=lambda x :x["age"],reverse=True))


x=[x for x in stud if x["age"]>=18]
print("Filter Based on age:",x)