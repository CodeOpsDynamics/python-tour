#if - else statement
# print(10%2==0)

# val=input("Enter the number ")
# value_float=float(val)
# print(value_float)
# if (value_float>100):
#     print("The number is greater then 100")



# val=input("Enter the number ")
# value_float=float(val)
# if (value_float%2==0):
#     print("The number is even")
# else:
#     print("The number is odd")

# ## Age form
# age=float(input("Enter the Age "))
# if(age<18):
#     print("Voting Not Permitted")
# else:
#     print("Vote for the PM")

## Nested if-else statement
age=float(input("Enter the Age "))
if(age<18):
    print("Voting Not Permitted")
elif(age>18 and age<=39):
    print("Soch ke krna bhai")
elif(age>39 and age<=60):
    print("Soch ke krna bhai")
else:
    print("Aram ka time hai")