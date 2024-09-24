import os
class Log:
    def __init__(self,filename) -> None:
        self.filename = filename
        self.entries = list()
    
    def create_file_log(self): 
        if not os.path.exists(self.filename):
            with open(self.filename,'w',encoding='utf-8') as file:
                file.write(f'--Transações--')
             
    def add_entrie(self,entry:str):
        self.entries.append(entry)
        
    def save_file(self):
        with open(self.filename,'a',encoding='utf-8') as file:
            for item in self.entries:
                file.write(f'{item}\n')
            self.entries.clear()
            
if __name__ == '__main__':
    ...
