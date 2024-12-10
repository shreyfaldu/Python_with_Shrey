x = int(input("Enter the value of age: "))

if(x<13):
    print("Child")
elif(x>13 and x<19):
    print("Teenager")
elif(x>20 and x<59):
    print("Adult")
else:
    print("Senior")


age = 26
day = "Wednesdsay"

if(age>=18):
    price = 12
else:
    price = 8
    
if(day=="Wednesdsay"):
    price-=2
print("The price of ticket is: ",price)


marks = int(input("Enter the marks: "))

if(marks>=90 and marks<=100):
    print("The Gread was A")
elif(marks>=80 and marks<=89):
    print("The gread is B")
elif(marks>=70 and marks<=79):
    print("The gread is C")
elif(marks>=60 and marks<=69):
    print("The gread is D")
else:
    print("The gread is F")

fruit = "banana"
color = "yellow"

if fruit == "banana":
    if color == "yellow":
        print("ripe")
    elif color == "green":
        print("unripe")
    elif color == "Brown":
        print("Overripe")

# weather = str(input("Enter the mood of weather: "))

# if weather == "sunny":
#     print("Go for walk")
# elif weather == "rain":
#     print("Read book")
# elif weather == "snow":
#     print("Build a snowman")

# dis = int(input("Enter the Distance: "))

# if dis < 3:
#     print("Walk")
# elif dis > 3 and dis <= 15:
#     print("Bile")
# else:
#     print("Car")


# passord = str(input("Enter the password"))

# len = len(passord)
# print(len)
# if len < 6:
#     print("Weak")
# elif len > 6 and len < 10:
#     print("Medium")
# elif len > 10:
#     print("Strong")


# year = int(input("Enter the year: "))

# if year%4 == 0 or year%400 == 0:
#     print("This year is leap year")
# else:
#     print("This is not a leap year")


# pet = str(input("Enter the type of pet: "))
# age = int(input("Enter the age of pet: "))
# if(pet == "Dog" and age < 2):
#     print("Puppy food")
# elif pet == "Cat" and age > 5:
#     print("Senior cat food")



