# i = 1
# while i<=100:
#     print(i)
#     i+=1

# i = 100
# while i>=1:
#     print(i)
#     i-=1

# i = int(input("Enter value: "))
# j = 1
# while j<=10:
#     print(i, "*" ,j, "=" ,i*j)
#     j+=1
 
# i = 1
# while i <= 10:
#     print(i**2)
#     i+=1

# list = [1,4,9,16,25,36,49,64,81,100]
 
# ind = 0
# while ind < len(list):
#     print(list[ind])
#     ind+=1 

list = (1,4,9,16,25,36,49,64,81,100)

i = 0
x = int(input("Enter the element which u want to find: "))

while i < len(list):
    if(list[i] == x):
        print("Found")
    else:
        print("Not Found")
    i+=1
    
        
