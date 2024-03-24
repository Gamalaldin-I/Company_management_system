from SalariedEmployee import SalariedEmployee
class CommisionEmployee(SalariedEmployee):
    def __init__(self) -> None:
        super().__init__()

    def set_commission(self,comm:float):
        self.commission=comm

    def get_commission(self):
        return self.commission
    
    def read(self):
        super().read()
        self.set_commission(float(input('Enter the percent of the commission of salary : ')))

    def get_salary(self):
        inc=super().get_salary()*self.get_commission()
        return super().get_salary()+inc
 