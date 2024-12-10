num = 153

newStr = str(num)

length = len(newStr)
sum = 0
for i in newStr:
    sum += int(i)**length
    
if(num == sum):
    print("A")
else:
    print("NA")


list = [1,2,3,4,5,6,7,8,9,10]

for i in list:
    if(i%2==0):
        print(i," is Even number")
    else:
        print(i," is Odd number")

x = 0
y = 1

while(y<50):
    print(y)
    x = y
    y = x + y


x = 5
fac = 1

for i in range(1,x+1):
    fac = i * fac
print(fac)

value = input("Enter the mixvalue: ")
digit = 0
alpha = 0

for i in value:
    if(i.isdigit()):
        digit += 1
    else:
        alpha += 1
        
print("The no of alpha is: ",alpha,"& the no of digit is: ",digit)

# x = 25

# for i in range(1,x+1):
#     if(i%4 == 0):
#         print("fizz")
#     elif(i%5==0):
#         print("buzzz")
#     else:
#         print(i)


# password = input()

# the_lowerCase = False
# the_upperCase = False
# the_digit = False
# the_leght = False
# the_specialChar = False

# if(len(password)>=8 and len(password)<=16):
#     the_leght = True
    
# for i in password:
#     if(i.isdigit()):
#         the_digit = True
    
#     elif(i.isupper()):
#         the_upperCase = True
        
#     elif(i.islower()):
#         the_lowerCase = True
    
#     elif(i == '@' or i == '#' or i == '$' or i == '&'):
#         the_specialChar = True 

# if(the_digit == True and the_leght == True and the_lowerCase == True and the_specialChar == True and the_upperCase == True):
#     print("The pssword was valid")
# else:
#     print("The password was not vaild")

