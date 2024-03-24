from Employee import Employee
class HourlyEmployee(Employee):
    def __init__(self) -> None:
        super().__init__()
        
    def set_hours(self,hours:float):
        self.__hours=hours

    def get_hours(self):
        return self.__hours
    
    def set_hourCoast(self,hourCost:float):
        self.__hourCost=hourCost

    def get_hourCost(self):
        return self.__hourCost


    def read(self):
        super().read()
        self.set_hours(float(input('Enter your working hours : ')))
        self.set_hourCoast(float(input('Enter the cost of hour : ')))
    
    def set_salary(self):
        self._salary=self.get_hours()*self.get_hourCost()
