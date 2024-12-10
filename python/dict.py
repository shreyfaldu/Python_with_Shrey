student = {
    "name" : "shrey",
    "age" : 21,
    "cource" : ["python", "SQL", "OOPs"],
    "collageId" : "21dit018",
    "CGPA" : 8.05
}

print(student)
print(type(student))

emptyDict = {}
print(emptyDict)

student.update({"SGPA" : "8.99"})
print(student)

print(student["name"])
student.pop("name")
print(student)

student["age"] = 34
print(student)

print(student.get("age"))

print(student.keys())
print(student.values())
print(student.items())
