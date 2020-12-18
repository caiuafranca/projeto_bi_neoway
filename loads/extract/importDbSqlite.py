import pandas as pd 
import os
from sqlalchemy import create_engine

empresas = pd.read_csv('../../files/spreadsheets/empresas.csv',sep=";")

engine = create_engine("sqlite:///../../files/dataMirrors/empresas.db", echo=True)
sqlite_connection = engine.connect()

sqlite_table = "Empresas"
empresas.to_sql(sqlite_table, sqlite_connection, if_exists='fail')

sqlite_connection.close()