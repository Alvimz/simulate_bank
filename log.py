import os
class Log:
    def __init__(self,filename) -> None:
        self.filename = filename
        self.entry = list()
    
    def create_file_log(self): 
        if not os.path.exists(self.filename):
            with open(self.filename,'w',encoding='utf-8') as file:
                file.write('--Transações--\n')
    
             
    def add_entrie(self,entry:str):
        self.entry.append(entry)
        
    def save_file(self):
        with open(self.filename,'a',encoding='utf-8') as file:
            for item in self.entry:
                file.write(f'{item}\n')
            self.entry.clear()
        
    def log_deposit(self,cash:int):
        self.entry.append('Depósito: R$',cash)
        
    def log_withdraw(self,cash:int):
        self.entry.append('Saque: R$',cash)
        
    def log_see_money(self):
        self.entry.append('Viu o saldo da conta corrente!')
        
    
        
            
if __name__ == '__main__':
    ...
