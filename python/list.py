#mutable
#orderd
#Allow Duplicate

ages = [12,34,34,34]
print(ages)

#list contain different datatypes

list1 = [12,3.8,"Shrey"]
print(list1)

#empty list
list2 = []
print(list2)

#conversion of list
stri = "shrey"
result = list(stri)
print(result)

#access element in list
lang = ["python", "C++" , "javaScript"]
print(lang[0])
#nagative indexing
print(lang[-1])

#slicing
print(lang[1:2])
print(lang[:])
#reverse list
print(lang[::-1])






#add element in list

#append => to add element to the end of list
lang.append("DSA")
print(lang)

#insert => add element to a specific index
lang.insert(2,"DBMS")
print(lang)

#extend =>add full list
lang.extend([1,2,4,5])
print(lang)




#change id list

list4 = ["shrey", "Faldu", "Pareshkumar", 1, 3,4.0]
list4[5] = 5.0
print(list4)





#remove elemrnt
list4.remove("shrey")
print(list4)

del list4[2]
print(list4)

del list4[0:1]
#delete entaire list
del list4

vagii = ["cucumber", "kerete", "onione"]
print(vagii.pop(1))



#lenght of the list

cars = ["BMW", "Marcidise", "Honda"]
print(len(cars))



#Iterating Through a List

fruits = ["banana", "apple", "orabge"]

for i in fruits:
    print(i)