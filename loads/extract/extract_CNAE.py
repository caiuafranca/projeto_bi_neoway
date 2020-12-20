import pandas as pd 
cnae = pd.read_csv('../../files/spreadsheets/cnae.csv',sep=";")

#Etapa de Transformação
#splitar a ~@~ e transformar em dataframe
new_ordem = cnae["nu_ordem"].str.split("~@~",expand = True)
new_cd_ramo_atividade = cnae["cd_ramo_atividade"].str.split("~@~",expand = True)
new_de_ramo_atividade = cnae["de_ramo_atividade"].str.split("~@~",expand = True)

#concatenar os  dataframes 
new_df_ordem = pd.concat([cnae["cd_cnpj"],new_ordem],axis=1,ignore_index=False)
new_df_cod_ramo = pd.concat([cnae["cd_cnpj"],new_cd_ramo_atividade],axis=1,ignore_index=False)
new_df_de_ramo = pd.concat([cnae["cd_cnpj"],new_de_ramo_atividade],axis=1,ignore_index=False)

#renomenando as colunas
df1 = new_df_ordem.melt(id_vars=["cd_cnpj"])[["cd_cnpj","value"]].rename(columns={'cd_cnpj': 'cd_cnpj', 'value':'cod_ordem'})
df2 = new_df_cod_ramo.melt(id_vars=["cd_cnpj"])[["cd_cnpj","value"]].rename(columns={'cd_cnpj': 'cd_cnpj', 'value':'cod_ramo'})
df3 = new_df_de_ramo.melt(id_vars=["cd_cnpj"])[["cd_cnpj","value"]].rename(columns={'cd_cnpj': 'cd_cnpj', 'value':'desc_ramo'})

dff = pd.merge(df2,df3, how="inner", left_index=True, right_index=True)[["cd_cnpj_x","cod_ramo","desc_ramo"]]
dff = pd.merge(dff,df1, how="inner", left_index=True, right_index=True)[["cd_cnpj_x","cod_ordem","cod_ramo","desc_ramo"]]
dff["chave_cnae"] = dff["cod_ramo"].str[:2]

dataFrame = dff.query("cod_ordem not in [None]").rename(columns={
    "cd_cnpj_x": "cd_cnpj"
})

#exportando Dados para dataMirrors
dataFrame.to_csv("../../files/dataMirrors/extract_cnae.csv", sep=";", index=False)