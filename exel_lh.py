import pandas as pd
from docx import Document






df = pd.read_excel('exel_lh.xlsx');

tableau=[]

for index, row in df.iterrows():
#     # Get the necessary data from each row
    vars={
        'id':row['Id'],
        'nom':row['nom'],
        'prenom':row['prenom'],
        'age':row['age']
    }
    
    tableau.append(vars)




            
                  
    
                    
                    
    




    





