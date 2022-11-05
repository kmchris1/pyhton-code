# try block to handle the exception
print ("Enter a number:\n")
try:
	my_list = []

	while True:
		my_list.append(int(input()))	
# if the input is not-integer, just print the list
except:
	print(my_list)
print("print the max of my list is: {my_list}")
