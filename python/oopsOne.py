# class Student:
#     #Constructor
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        
# s1 = Student("Karan",99)
# print(s1.name,s1.marks)

# s2 = Student("Arjun",100)
# print(s1.name,s1.marks)


# class Student:
#     def __init__(self,name,sub1,sub2,sub3):
#         self.name = name
#         self.sub1 = sub1
#         self.sub2 = sub2
#         self.sub3 = sub3
        
#     def calAvg(self):
#         avg = (self.sub1+self.sub2+self.sub3)/3
#         print("The Avg marks of student is:",avg,self.name)
        
# s1 = Student("Sgun",99,89,79)
# ans = s1.calAvg()

class Account:
    def __init__(self,balance,accountNo):
        self.balance = balance
        self.accountNo = accountNo
        
    def debit(self,debit):
        self.balance += debit
        print(self.balance)
        
    def credit(self,credit):
        self.balance -= credit
        print(self.balance)
        
a1 = Account(10000,9898)
a1.credit(5000)

