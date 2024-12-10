# val = int(input("Enter the value: "))
# temp = val
# sum = 0

# while(val>0):
#     rev = temp % 10
#     sum = sum*10 + rev
#     val = val // 10
# if(temp == sum): print("YESH")
# else: print("NOH")



# num = 152
# num2 = str(num)
# lent = len(num2)
# sum = 0
# for i in num2:
#     sum+=int(i)**lent
    
# if(sum == num):print("Y")
# else: print("N")

# list = [1,2,3,4,5,6,7,8,9,10,11]
# countE = 0
# countO = 0

# for i in list:
#     if(i%2==0):
#         countE+=1
#     else:
#         countO+=1
# print(countO)
# print(countE)


# startRange = int(input("Enter the startrange: "))
# endRange = int(input("Enter endRange: "))

# for num in range(startRange, endRange+1):
#     if num > 1:
#         for i in range(2,num):
#             if(num % i) == 0:
#                 break
#         else:
#             print(num)



# num = int(input("Enter the range: "))
# num1 = 0
# num2 = 1
# print(num1,num2,end=" ")
# for i in range(2,num):
#     num3 = num1 + num2
#     num1 = num2
#     num2 = num3
#     print(num3,end=" ")
# print()


# fac = int(input("Enter number u want to find Fec: "))
# sum = 1
# for i in range(1,fac+1):
#     sum*=i
# print(sum)

# stri = str(input("Enter the String: "))
# a = 0
# n = 0
# for i in stri:
#     if(i.isalpha()):
#         a+=1
#     elif(i.isdigit()):
#         n+=1
# print(a)
# print(n)

# num = int(input("Enter the Number: "))

# for i in range(1,num+1):
#     if(i%4==0):
#         print("fizz")
#     elif(i%5==0):
#         print("buzz")
#     else:
#         print(i)


num = int(input("Enter the nu: "))
num1 = 0
num2 = 1
print(num1, num2,end=" ")
for i in range(2,num):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3,end=" ")