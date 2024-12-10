f = open("demo.txt", "r")
f.write("abcd")
f.read()
print(f.read())
f.close()

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# import os
# os.remove("s.txt")

# with open("pretical.txt","w") as f:
#     f.write("Hi everyOne")
#     f.write("\nwe are learning file I/O\nusing Java\nI like Programing in Java")

# with open("pretical.txt","r") as f:
#     data = f.read()

# newData = data.replace("Java","Python")
# print(newData)

# with open("pretical.txt","w") as f:
#     f.write(newData)


# word = "learning"
# with open("pretical.txt","r") as f:
#     data = f.read()
#     if(data.find(word) != -1):
#         print("Found")
#     else:
#         print("Not Found")    
def check_lineNo():
    word = "learning"
    data = True
    line_no = 1

    with open("pretical.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
            
    return -1
check_lineNo()