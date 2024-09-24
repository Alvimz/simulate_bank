import os

class FileHelper:
    @staticmethod
    def create_file_log(account_name:str): 
        log_file = f'./log_{account_name}'
        if not os.path.exists(log_file):
            with open(log_file,'w',encoding='utf-8') as file:
                file.write(f'--Transações de: {account_name} --')
                ...
                
            print('Arquivo de log criado!')
        else:
            
            print('Arquivo de log já criado!')
            
if __name__ == '__main__':
    a = FileHelper()
    a.create_file_log('Lucas')
