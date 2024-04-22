from Budget import Budget
class Project :
    idCounter=0
    def __init__(self,name:str,deadline:str) -> None:
        Project.idCounter+=1
        self.set_id(Project.idCounter)      #id

        self.set_name(name)                 #name

        self.set_deadline(deadline)         #deadline

        describtion=input("Enter the describtion of the project")
        self.set_describtion(describtion)

        balance=(input("Enter the budget of the project"))
        while not(balance.isdigit()):    
           balance=(input("Enter the budget of the project"))

        self.__budget=Budget(float(balance)) #budget


    # setters and getters
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    
    def set_describtion(self,describtion):
        self.__decribtiion=describtion
    def get_describtion(self):
        return self.__decribtiion
    
    def set_deadline(self,deadline):
        self.__deadline=deadline
    def get_deadline(self):
        return self.__deadline
    
    def set_id(self,id):
        self.__id=id
    def get_id(self):
        return self.__id
    
    def read(self):
        name=input("Enter the project name   :  ")
        self.set_name(name)

        desc=input("Enter the project desc   :  ")
        self.set_describtion(desc)

        deadline=input("deadline   :  ")
        self.set_deadline(deadline)

        self.edit_budget()
        

    def print(self):
        print(
f'''print("The prooject info")             
id   : {self.get_id()}
name : {self.get_name()}
description : {self.get_describtion()}
deadline    : {self.get_deadline()}
budget      : {self.__budget.get_balance()}
''')
        
    def edit_budget(self):
        choice=-1
        print(
"""1. increase the budget
2. decrease the budget
3. reset to 0
0. return""")
        choice=int(input("Enter your choice"))
        while choice!=0:
            if choice==1:
                inc=float(input("enter the increment"))
                self.__budget.increaseBudget(inc)
            elif choice==2:
                dec=float(input("enter the decrement"))
                self.__budget.decreseBudget(dec)
            elif choice==3:
                self.__budget.resetto0()
                print("the broject balance is 0")
            else:
                print('enter valid number')





    