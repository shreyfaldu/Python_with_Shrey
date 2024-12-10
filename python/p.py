num = int(input("Enter the number:"))
flag = False
if num > 1:
    for i in range(2,num):
        if num%i == 0:
            flag = True
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is prime number")


num = int(input("enter the value"))
temp = num
reverce = 0
while(temp > 0):
    reminder = temp % 10
    reverce = (reverce * 10) + reminder
    temp = temp//10
if num == reverce:
    print(num, "is palingdrom numver")
else: print(num, "is not a palingdrom number")

num = int(input("enter the number: "))

temp = num
sum = 0
while(temp > 0):
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if(num == sum):
    print("che")
else:
    print("nathi")

s1 = str(input("Enter the first string: "))
s2 = str(input("enter the second String: "))

if(sorted(s1) == sorted(s2)):
    print("Given strings are anagram")
else:
    print("Given strings are not anagram")
    
p = "dcba"
print(sorted(p))