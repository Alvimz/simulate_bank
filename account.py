class Account:
    def __init__(self,name:str) -> None:
        self._name = name
        self._money = 0.0
        
        
    @property    
    def name(self):
        return self._name
    
    @property
    def money(self)->float:
        return self._money
    
    @money.setter
    def money(self,qnt):
        if qnt<=0:
            raise ValueError('Não pode ser um valor negativo!')
        self._money= qnt
        
    def deposit(self,qnt:float):
        self.money+=qnt
        
    def withdraw(self,qnt:float):
        if qnt>self._money:
            raise ValueError('Saldo insuficiente para resgate!')
        self.money-=qnt
        
    def see_money(self)->float:
        return self._money
    
if __name__ == '__main__':
    gabriel_account = Account('Gabriel')
    gabriel_account.deposit(30)
    gabriel_account.withdraw(35)
    print(gabriel_account.see_money())
 
   
    