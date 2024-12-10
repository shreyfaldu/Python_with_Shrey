#string is a sequnce of caharacter
#Immutable
#creating of string

str1 = "sherwy"
str2 = 'shery'

name = "python"
print(name)

message = "I Love U"
print(message)

#Access String Characters in Python

greet = "Hello"
print(greet[1])

#nagative indexing
print(greet[-2])

#slicing
surname = "Faldu"
print(surname[0:3])
print(surname[-4:-1])
print(surname[::-1])


#string are Immutable but we aasinge new string to same name variable

fullname = "Shrey Faldu"

fullname = "Faldu Shrey"

print(fullname)


#Compare Two Strings
str1 = "Hello, world!"
str2 = "I love Swift."
str3 = "Hello, world!"

# compare str1 and str2
print(str1 == str2)

# compare str1 and str3
print(str1 == str3)







#Join Two or More Strings
greet = "Hello, "
name = "Jack"

# using + operator
result = greet + name
print(result)





#Iterate Through a Python String

namename = "shreyfaldu"

for i in namename:
    print(i)

#Python String Length
print(len(namename))


#upper

name = "shrey"
print(name.upper())

#lower

print(name.lower())

print(name.partition)

sen = "I love banana"
x = sen.replace("banan", "orange")
print(x)