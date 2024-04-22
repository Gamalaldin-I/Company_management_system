class Budget:
    def __init__(self,balance) -> None:
        self.set_balance(balance)


    def set_balance(self,balance):
        self.__balance=balance

    def get_balance(self):
        return self.__balance
    
    def increaseBudget(self,increment):
        self.__balance+=increment

    def decreseBudget(self,decrease):
        self.__balance-=decrease

    def resetto0(self):
        self.__balance=0