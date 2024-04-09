class Task:
    id=0
    def __init__(self) -> None:
        Task.id+=1
        self.set_id(Task.id)
        self.notDone()
        self.givenTo='None'
        self.read()

    def read(self):
        name= input('Enter the name of the task >>> ')
        desc= input('Enter the description of the task >>> ')
        dead= input('Enter the deadline >>> ')
        self.set_name(name)
        self.set_description(desc)
        self.set_deadline(dead)

    def edit(self):
        self.read()

    def print(self):
        
        self.info = f'''
#####################################################
id >>> {self.get_id()}  Status >>> {self.isDone()} Given to >>> {self.givenTo} 
name >>> {self.get_name()}
DeadLine >>> {self.get_deadline()}
description >>> {self.get_description()}'''
        print(self.info)
        
    def set_id(self,id):
        self.__id=id
    def get_id(self):
        return self.__id
    
    def set_name(self,name):
        self.__name=name

    def get_name(self):
        return self.__name
    
    def set_description(self,description):
            self.__description=description

    def get_description(self):
            return self.__description
    def set_deadline(self,deadline):
         self.__deadline=deadline
    def get_deadline(self):
            return self.__deadline
    def done(self):
        self.__done=True
    def isDone(self):
        return self.__done
    def notDone(self):
        self.__done=False   

    def giveTo(self,id):
            self.givenTo = id 
    
    