def find(num):
    # initializing 
    numtype = "odd"
    if num%2 == 0:
        numtype="even"
    return numtype

num = int(input('Enter the number: '))      # take your input
numtype = find(num)                         # call the  find function
print('Given number is',numtype)            # print if the number is even or odd