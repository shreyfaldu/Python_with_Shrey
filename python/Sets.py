# A set is a collection of unique data, meaning that elements within a set cannot be duplicated.
# Set can have difference order during the Output

#creation of set

stut_id = {1,2,3,4,5}
print(stut_id)

vowel_latter = {"s", "h", "r", "e", "y"}
print(vowel_latter)

mixed_set = {"shrey", "faldu", 1, 8.05}
print(mixed_set)

#empty sets

setss = set()
print(setss)

#if we try to store duplicate element

numbers = {1,2,2,2,2,3}
print(numbers)







#Add and Update Set Items in Python
numbers = {1,2,3,4,5,6,7}
numbers.add(9)
print(numbers)








#remove element
numbers.remove(2)
print(numbers)
numbers.discard(3)
print(numbers)






#union and intersection 
col1 = {1,2,3}
col2 = {3,4,5}

print(col1.union(col2))
print(col1.intersection(col2))



numberrr = {1,2,3,4,5}
x = numberrr.pop()
print(x)
print(numberrr)
