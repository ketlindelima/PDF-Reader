from time import sleep
from unittest import result
import PyPDF4 
import re 
import os
from pdfminer.high_level import extract_text

global result
global all_clients
all_clients = []

folder = 'C:/Users/Ketlin/Documents/GitHub/PDF-Reader/example_files'
for directory, subfolder, files in os.walk(folder):
    for file in files:
        FILE_PATH = os.path.join(os.path.realpath(directory), file)
        
        #Define modo de leitura do arquivo
        try:
            with open(FILE_PATH):
                text = extract_text(FILE_PATH)
                basename = os.path.basename(FILE_PATH)
                file_name = os.path.splitext(basename)[0]

                # Break the  list when find :
                text = re.sub('Client: ', 'Client: \n', text)
                text = re.sub('Company: ', 'Company: \n', text)
                
                #transforma em índices de uma lista assim que encontrar um \n
                out = list(text.split('\n'))

                out_trim=[]
                # Remove espaços em branco antes e depois dos elementos
                for s in out:
                    aux = s.strip()
                    out_trim.append(aux)
                print(out_trim)

                def find_in_list(Word_to_find):
                    
                    cont = 0

                    position_list = []

                    for elements in out_trim:
                        if elements == Word_to_find:
                            position_list.append(cont)
                        cont+=1
                    for r in position_list:
                        result = out_trim[r+1]
                    
                    return result

                print(result)
                all_clients = []
                
                
                

                # Encontra data de vencimento
                vetor_aux=[]
                for teste in out:
                    r = re.compile(r'[0-9]{2}/[0-9]{2}/[0-9]{4}')
                    check = r.findall(teste)
                    vetor_aux.append(check)

                for w in vetor_aux:
                    if w!= []:
                        for o in w:
                            date = o
                print(date)
                print(clients)
                sleep(1)
                
                # Verifica se existe a pasta, ou então cria a pasta
                '''if not os.path.exists(vencimento):
                    os.makedirs(vencimento)

                file = f'{nome_arquivo}.xlsx'''

        except:
            print(f'Could not read de file: {file_name}')
            print()
            sleep(4)

        clients = find_in_list("Client:")
        all_clients.append(clients)
print(all_clients)