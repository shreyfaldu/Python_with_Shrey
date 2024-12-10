def calAvj(a,b,c):
    sum = (a+b+c)/3
    return sum

print(calAvj(3,4,5))

# 

# def INR(n):
#     ind=n*83
#     print(ind)
# INR(10000)


def even_odd(n):
    if(n%2 == 0):
        print("EVEN")
    else:
        print("ODD")
        
n = int(input("Enter the value of n: "))
even_odd(n)



def rec(n):
    if(n==0):
        return
    print(n)
    rec(n-1)
rec(5)

def Fec(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * Fec(n-1)
print(Fec(5))

# def sum(n):
#     if(n == 1):
#         return 1
#     return n + sum(n-1)
# print(sum(5))

# def print1(list, ind = 0):
#     if(ind == len(list)):
#         return
#     print(list[ind])
#     print1(list,ind+1)
    
# fruits = ["Mango", "Licccchhii", "banana"]
# print1(fruits)

n = int(input("Enter the number:"))
fac = 1

for i in range(1,n+1):
    fac*=i
print(fac)
