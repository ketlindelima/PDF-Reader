from time import sleep
import PyPDF4 
import re 
import os
from pdfminer.high_level import extract_text
import pandas as pd
from FindElements import find_in_list

text = ''

folder = 'C:/Users/Ketlin/Documents/GitHub/PDF-Reader/example_files'
for directory, subfolder, files in os.walk(folder):
    for file in files:
        FILE_PATH = os.path.join(os.path.realpath(directory), file)
        
        # Read the file to extract information
        try:
            with open(FILE_PATH):
                
                text += extract_text(FILE_PATH)
                basename = os.path.basename(FILE_PATH)
                file_name = os.path.splitext(basename)[0]
                sleep(2)
        except:
            print(f'Could not read file: {file_name}')
            sleep(2)   
        
    # Replaces the elements incrementing a \n
    text = re.sub('Client: ', 'Client: \n', text)
    text = re.sub('Company: ', 'Company: \n', text)

    # Break the text making a list when find \n
    out = list(text.split('\n'))

    out_trim=[]
    # Remove whitespace before and after elements
    for s in out:
        aux = s.strip()
        out_trim.append(aux)
    print(out_trim)

    # In this case I am finding dates using Regex
    vetor_aux=[]
    date = []
    for numbers in out_trim:
        r = re.compile(r'[0-9]{2}/[0-9]{2}/[0-9]{4}')
        check = r.findall(numbers)
        vetor_aux.append(check)

    for w in vetor_aux:
        if w!= []:
            for o in w:
                date.append(o)
    
    # Call the function
    clients = find_in_list("Client:", out_trim)
    company = find_in_list("Company:", out_trim)

    # Create the DataFrame
    lista_de_tuplas = list(zip(clients, company))
    df = pd.DataFrame(lista_de_tuplas, columns=['User', 'Company'])

    sleep(3)

    #df_reset=df.set_index('')  You can set the first columm with this command

    df['Date'] = date #Here you can put another columm in DataFrame

    print(df)
    
    # Check if the folder exists, if not, create the folder
    if not os.path.exists('Folder_Name'):
        os.makedirs('Folder_Name')

    variable_name = "file_sheet_name" #A random name to show that is possible create a name using a variable

    file = f'{variable_name}.xlsx'
    df.to_excel(os.path.join('Folder_Name', file))

      