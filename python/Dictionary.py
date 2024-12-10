#Dictionary is a collection of key-value pair
#immutable
#Keys of a dictionary must be immutable means key are not list, set 
#creation of Dictionary

country_name = {
    "Germany" : "Berline",
    "Canada" : "ottawa",
    "England" : "London"
}
print(country_name)

# valid dictionary
# integer as a key
my_dict = {1: "one", 2: "two", 3: "three"}

# valid dictionary
# tuple as a key
my_dict = {(1, 2): "one two", 3: "three"}

# invalid dictionary
# Error: using a list as a key is not allowed
# my_dict = {1: "Hello", [1, 2]: "Hello Hi"}

# valid dictionary
# string as a key, list as a value
my_dict = {"USA": ["Chicago", "California", "New York"]}









#access the element in Dictonary

country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London"
}

print(country_capitals["Canada"])
print(country_capitals["England"])



#add element in Dictionary

country_capitals["India"] = "Delhi"
print(country_capitals)


#remove element in Dictionary

country_capitals.pop("India")
print(country_capitals)




student = {
    "name" : "Shrey Faldu",
    "CGPA" : 8.05,
    "Subject" : ["JavaScript", "DSA", "DBMS", "Python"],
    "City" : "Junagadh",
    "CollageId" : "21dit018"
}


#add

student.update({"Fathename" : "Pareshkumar"})
print(student)

#update
student["CGPA"] = 9.00
print(student)

#remove
student.pop("name")
print(student)

#access
print(student["CollageId"])

print(student.get("name"))

print(student.keys())
print("")
print(student.values())
print("")
print(student.items())
