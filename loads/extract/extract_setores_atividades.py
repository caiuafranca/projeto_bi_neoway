import pandas as pd 

setor = pd.read_csv('../../files/spreadsheets/Setores e Ramos de Atividade.csv',sep=";")

setor_csv = setor[["Ramo de Atividade","Divisões","(DIVISÃO - 2digitos CNAE)"]].rename(columns={
    "Ramo de Atividade": "ramo_atividade",
    "Divisões": "divisao",
    "(DIVISÃO - 2digitos CNAE)": "chave_cnae"
}).fillna(method="ffill")

#Exportando DataFrame para dataMirror
setor_csv.to_csv("../../files/dataMirrors/extract_setor_atividades.csv", sep=";", index=False)