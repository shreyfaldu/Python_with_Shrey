#the tuples are same as python list, but the maager difference is the tuples are not modify once it was create

#orderd
#Allow Duplicate
#Immutalbe

#creation

tup = (1,2,2,3.0,"shrey")
print(tup)
#empty Tuples

tup1 = ()
print(tup1)

print(type(tup1))



#access tuples element

lang = ("C++", "Java", "JavaScript")
print(lang[1])
print(lang[0:2])
print(lang[::-1])


#tuples are cannot be modify


#tuples lenght

cars = ("BMW", "SUV", "Oddi")
print(len(cars))


#Iterate Through a Tuple
fruits = ("banan", "orange", "strwbarry")
for fruit in fruits:
    print(fruit)
    
    
#delete Tuple
vagii = ("banana", "stryyy", "carsss")

# del vagiiprint(vagii)""

#create only one element tuples
tup3 = ("shrey",)
print(type(tup3))




#add elemrnt in tuple
tup4 = ("shrey", "faldu", "pareshkumar")

result = list(tup4)
print(tup4)

result.append(4)
result2 = tuple(result)
print(result2)
print(type(result2))