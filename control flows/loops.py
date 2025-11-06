# #for_loop & while_loop
# list=[1,2,3,4,5,6,7,8,9]
# for i in list:
#     print(i)
#     print(i**2)


# #find sum of all the elements in list
# list=[1,2,3,4,5,6,7,8,9]
# total=0
# for i in list:
#     total=total+i
# print(total)

## find the some of even and odd numbers
list=[1,2,3,4,5,6,7,8,9]
even_sum=0
odd_sum=0
for i in list:
    if(i%2==0):
        even_sum=even_sum+i
    else:
        odd_sum=odd_sum+i
print("Even Sum is {a} and Odd Sum is {b}".format(a=even_sum,b=odd_sum))