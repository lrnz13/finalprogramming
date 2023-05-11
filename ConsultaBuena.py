import pandas as pd
from sqlite3 import connect
import stremlit as st
#import streamlite as st
conection = connect("InfoDatabase.db") #Definimos a dónde nos vamos a conectar
ProjectsBBDD = pd.read_sql('SELECT * FROM ProjectsDB', conection)  
CountriesBBDD = pd.read_sql('SELECT * FROM CountriesDB', conection)
ParticipantsBBDD = pd.read_sql('SELECT * FROM ParticipantsDB', conection)

#2.6
option=st.selectbox("Choose a country: ",'Belgium', 'Bulgaria', 'Czechia', 'Denmark', 'Germany', 'Estonia', 'Ireland','Greece', 'Spain', 'France', 'Croatia'
, 'Italy', 'Cyprus', 'Latvia', 'Lithuania','Luxembourg','Hungary', 'Malta', 'Netherlands', 'Austria', 'Poland', 'Portugal','Romania', 'Slovenia', 'Slovakia', 'Finland', 'Sweden')
    
countriesdictionary= {'Belgium': 'BE', 'Bulgaria': 'BG', 'Czechia': 'CZ', 'Denmark': 'DK', 'Germany':
'DE', 'Estonia': 'EE', 'Ireland': 'IE','Greece': 'EL', 'Spain': 'ES', 'France': 'FR', 'Croatia':
'HR', 'Italy': 'IT', 'Cyprus': 'CY', 'Latvia': 'LV', 'Lithuania': 'LT','Luxembourg': 'LU',
'Hungary': 'HU', 'Malta': 'MT', 'Netherlands': 'NL', 'Austria': 'AT', 'Poland': 'PL', 'Portugal':
'PT','Romania': 'RO', 'Slovenia': 'SI', 'Slovakia': 'SK', 'Finland': 'FI', 'Sweden': 'SE'}
acronym=countriesdictionary[option]
print("Your acronym is: ", acronym)

consultadf = ParticipantsBBDD[ParticipantsBBDD["country"]==acronym] #Genera un dataframe de la tabla participants del país seleccionado
consultacolumnas = consultadf.groupby('name').agg({
    "shortName": "first",  # use the first value of 'shortName'
    "activityType": "first",  # use the first value of 'activityType'
    "organizationURL": "first",  # use the first value of 'organizationURL'
    "ecContribution": "sum"  # sum the 'ecContribution' column
}).sort_values(by='ecContribution', ascending=False)

st.write(consultacolumnas)