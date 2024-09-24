import os
import datetime
class Log:
    def __init__(self,filename) -> None:
        self.filename = filename
        self.entry = list()
        self.date_now = None
    
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
        
    def deposit(self,cash:int):
        self.entry.append(f'Depósito: R${cash} - {self.date()}')
        
    def withdraw(self,cash:int):
        self.entry.append(f'Saque: R${cash} - {self.date()}')
        
    def see_money(self):
        self.entry.append(f'Viu o saldo da conta corrente! {self.date()}')
        
    def try_deposit(self):
        self.entry.append(f'Tentou adicionar saldo negativo na conta! {self.date()}')
        
    def date(self):
        self.date_now = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
        return self.date_now 
        
        
            
if __name__ == '__main__':
    ...
