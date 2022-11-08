# my_f_fruits=["apple", "banana", "cherry", "Mango"]

# my_f_juice = ["Djino", "pineaple", "cellery", "cranbery"]
# https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/

# # creating an empty list
lst = []
# number of elements as input
n = int(input("Enter number of elements : "))

if len(lst) == 0:
    print (f"the list is empty '[]'")
else: 
# iterating till the range
    for i in range(0, n):
	    ele = int(input())

lst.append(ele) # adding the element
	
print(lst)

print (f"print the maximum of the list {max(lst)}")
