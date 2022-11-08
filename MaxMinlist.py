lst = []
# number of elements as input
n = int (input("Enter a number your grade for math:\n"))

# iterating till the range
for i in range(0, n):
	    ele = int(input())

lst.append(ele) # adding the element
	
try:
    result = max(my_list)
except ValueError:
    result = 0

print(result)  # 👉️ 0
