from log import Log
class Account:
    def __init__(self,name:str) -> None:
        self._name = name
        self._money = 0.0
        self.log = Log(f'log_{name}.txt')
        self.log.create_file_log()
        
        
    @property    
    def name(self):
        return self._name
    
    @property
    def money(self)->float:
        return self._money
    
    @money.setter
    def money(self,qnt):
        if qnt<=0:
            self.log.add_entrie(f'Tentou adicionar: R${qnt}')

            #raise ValueError('Não pode ser um valor negativo!')
        self._money= qnt
        
    def deposit(self,qnt:float):
        self.money+=qnt
        self.log.add_entrie(f'Depositou: R${qnt}')
        
    def withdraw(self,qnt:float):
        if qnt>self._money:
            self.log.add_entrie(ValueError('Saldo insuficiente!'))
            #raise ValueError('Saldo insuficiente para resgate!')
        self.money-=qnt
        
    def see_money(self)->float:
        self.log.add_entrie('viu o saldo da conta!')
        return self._money
    
if __name__ == '__main__':
    gabriel_account = Account('Gabriel')
    gabriel_account.deposit(30)
    gabriel_account.withdraw(35)
    print(gabriel_account.see_money())
    gabriel_account.log.save_file()
 
   
    