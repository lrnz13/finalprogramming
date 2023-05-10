import pandas as pd
from sqlite3 import connect
import streamlit as st
conection = connect("InfoDatabase.db")
consulta = pd.read_sql('SELECT * FROM ProjectsDB', conection)
conection.close()
st.write(consulta)

