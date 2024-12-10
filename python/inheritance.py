class Animal:
    
    def bark(self):
        print("is barking")
    
    def sleep(self):
        print("is sleeping")

class Dog(Animal):
    
    def eat(self):
        print("is eating")
        
d1 = Dog()
# d1.bark()
# d1.sleep()
# d1.eat()



#___________________________________________________________________________________________


#overriding in Inheritance

class Birds:
    def fly(slef):
        print("I am flying")
        
class Parrot(Birds):
    def fly(self):
        super().fly()
        print("I am Like to fly")
        
p1 = Parrot()
p1.fly()