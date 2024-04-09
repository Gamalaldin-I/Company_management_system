from SalariedEmployee import SalariedEmployee
from HourlyEmployee import HourlyEmployee
from CommisionEmployee import CommisionEmployee
from Employee import Employee
from Volunteer import Volunteer
from Task import Task
class Team :
    id=0
    def __init__(self,name) -> None:
        self.employees=[]
        self.tasks=[]
        Team.id+=1
        self.set_name(name)
        self.set_id(Team.id)
#for team
    def set_name(self,name):
        self.__name=name

    def get_name(self):
        return self.__name
    
    def getEmpsSize(self):
        return len(self.employees)
    def getTasksSize(self):
        return len(self.tasks)
    
    def set_id(self,id):
        self.__id=id

    def get_id(self):
        return self.__id

    def Team_menu(self):
       choice=-1
       while  choice !=0: 
            teamMenu='''1. Join new employee
2. Delete employee
3. Edit employee
4. Show all the team
5. Add new task
6. Edit a task
7. Remove a task
8. Gvie a task
0. return'''
            print(teamMenu)
            choice= int(input('Enter your choice : '))
            if choice==1:
                self.join_employee()
            elif choice ==2 :
                id=int(input('Enter the id to delete >>>   '))
                self.remove_employee(id)
            elif choice ==3 : 
                id=int(input('Enter the id to Edit >>>   '))
                self.edit_employee(id)
            elif choice ==4 : 
                self.showTeam()
            elif choice ==5 : 
                self.add_task()
            elif choice ==6 : 
                id=int(input('Enter the id to Edit >>>   '))
                self.edit_task(id)
            elif choice ==7 : 
                id=int(input('Enter the id to delete >>>   '))
                self.remove_Task(id)
            elif choice ==8 : 
                ide=int(input('Enter the id of the employee >>>   '))
                idt=int(input('Enter the id of the task >>>   '))
                self.give_task_to(idt,ide)
            elif choice == 0 :
                pass

            else:
                print('the choice not in range')
#for Employees
    def join_employee(self):
        choice=-1
        while not choice==5 :        
            menu='''
        1.Salaried
        2.Hourly
        3.Commission
        4.Volunteer
        5.return'''
            new_emp:Employee=None
            print(menu)
            choice=int(input('Enter the choice'))
            if choice ==1:
                new_emp=SalariedEmployee()
                self.employees.append(new_emp)
            elif choice==2:
                new_emp=HourlyEmployee()
                self.employees.append(new_emp)
            elif choice==3:
                new_emp=CommisionEmployee()
                self.employees.append(new_emp)
            elif choice==4:
                new_emp=Volunteer()
                self.employees.append(new_emp)
            elif choice==5:
                pass
            else:
                print('the choice not in range')

    def showTeam(self):
        print(f"Team : {self.get_name()}   Id : {self.get_id()}")
        print("--------------------------------","Employees","--------------------------------",sep="\n")
        if self.noEmployees():
            return
        for i in range(0,self.getEmpsSize()):
            print(i+1,end='>>')
            self.employees[i].print()
        print("--------------------------------","Tasks","--------------------------------",sep="\n")
        if self.thereNoTasks():
            print("No tasks yet")
            return
        for i in range(0,self.getTasksSize()):
            self.tasks[i].print()

    def noEmployees(self):
        return self.getEmpsSize()==0

    def remove_employee(self,id):
        #case empty employee list
        if self.noEmployees():
            print('no elements to remove')
            return
        pos=-1
        #get the pos of id first
        for i in range(0,self.getEmpsSize()):
            #if found
            if self.employees[i].get_id()==id:
                pos=i
                break
        #if not found after looping
        if pos==-1:
            print('not found')
            return
        #shift the elements to the empty place
        for i in range(pos,self.getEmpsSize()-1):
            self.employees[i]=self.employees[i+1]
        #delete the last element
        self.employees.pop()        

    def edit_employee(self,id):
        #case empty employee list
        if self.noEmployees():
            print('no employees to edit')
            return
        pos=-1
        #get the pos of id first
        for i in range(0,self.getEmpsSize()):
            #if found
            if self.employees[i].get_id()==id:
                pos=i
                break
        #if not found after looping
        if pos==-1:
            print('not found')
            return
        #Edit
        print('Previos Data : ')
        self.employees[pos].print()
        print('Enter the new Data : ')
        self.employees[pos].read()
    
    def employeeFound(self,id):
        found=False
        pos=-1
        if self.noEmployees():
            print("no employees")
            return found
        for i in range(0,self.getEmpsSize()):
            if self.employees[i].get_id()==id:
                found=True
                pos=i
                break
        return found,pos
 
 #for Tasks       
    def add_task(self):
        new_task=Task()
        self.tasks.append(new_task)
    
    def taskFound(self,id):
        pos=-1
        found=False
        if self.thereNoTasks():
            print("no tasks")
            return found
        
        for i in range(0,self.getTasksSize()):
            if self.tasks[i].get_id()==id:
                found=True
                pos=i
                break
        return found,pos
    
    def thereNoTasks(self):
        return self.getTasksSize==0
    
    def remove_Task(self,id):
        #case empty Tasks list
        if self.thereNoTasks():
            print('no Tasks to remove')
            return
        pos=-1
        #get the pos of id first
        for i in range(0,self.getTasksSize()):
            #if found
            if self.tasks[i].get_id()==id:
                pos=i
                break
        #if not found after looping
        if pos==-1:
            print('not found')
            return
        #shift the elements to the empty place
        for i in range(pos,self.getTasksSize()-1):
            self.tasks[i]=self.tasks[i+1]
        #delete the last element
        self.tasks.pop()     

    def edit_task(self,id):
         #case empty employee list
        if self.thereNoTasks():
            print('no tasks to edit')
            return
        pos=-1
        #get the pos of id first
        for i in range(0,self.getTasksSize()):
            #if found
            if self.tasks[i].get_id()==id:
                pos=i
                break
        #if not found after looping
        if pos==-1:
            print('not found')
            return
        #Edit
        print('Previos Data : ')
        self.tasks[pos].print()
        print('Enter the new Data : ')
        self.tasks[pos].read()
    def notValid(self,bool,int):
        return bool==False and int==-1
    def give_task_to(self,idOfTask,idOfEmployee):
        tfound,tpos=self.taskFound(idOfTask)
        efound,epos=self.employeeFound(idOfEmployee)
        if self.notValid(tfound,tpos) or self.notValid(efound,epos):
            print("something wrong check you enterd a valid employee and task ids ")
            return
        else:
            self.tasks[tpos].giveTo(idOfEmployee)
            print(f"Task id {self.tasks[tpos].get_id()} was given to {idOfEmployee} successfully")
        


    