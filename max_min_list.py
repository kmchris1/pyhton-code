# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, n):
	ele = int(input())

	lst.append(ele) # adding the element
	
print(lst)

if len(lst)==0:
    print("print the list is empty of []")
else: 
    print(f"print the max  and the min of my list is: {max(lst)} {min(lst)}")
    # print(f"print the min of my list is: {min(lst)}")
