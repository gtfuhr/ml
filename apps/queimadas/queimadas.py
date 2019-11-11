import streamlit as st
import pandas as pd
import numpy as np
from collections import namedtuple
import matplotlib.pyplot as plt

# Data attribs
# Index(['Código CNUC', 'Nome da UC', 'Categoria da UC: sigla federal',
#        'Categoria da UC: nomenclatura nacional', 'Grupo de Proteção',
#        'Ano de criação', 'Coordenação Regional do ICMBio',
#        'Área estimada da UC (ha)', 'Bioma referencial',
#        'Área queimada em 2018', 'Área queimada em 2017',
#        'Área queimada em 2016', 'Área queimada em 2015',
#        'Área queimada em 2014', 'Área queimada em 2013',
#        'Área queimada em 2012'],

def data_cleaning(data):
    data = [x.replace('.','') if type(x) == str else float(x) for x in data]
    clean_data = [float(x.split(',')[0]) if type(x) == str else x for x in data]
    
    return clean_data

st.title('Queimadas em parques de preservação no Brasil')

@st.cache
def load_data():
    data = pd.read_csv("DIMIF-queima.csv",delimiter=";",decimal=',')
    data.fillna(0,inplace = True)
    return data

data_cached = load_data()
data = data_cached.copy()

if st.checkbox("Selecionar dados por bioma ou coordenação em especifico"):
    filtro = st.selectbox("Selecionar dados atraves da sua coordenação ou bioma?", options=["Coordenação","Bioma"])
    if(filtro == "Bioma"):
        biomas = list(set(data["Bioma referencial"]))
        bioma = st.selectbox("Selecionar o bioma desejado",biomas)
        data = data[data["Bioma referencial"] == bioma]

    if(filtro == "Coordenação"):
        estados = list(set(data["Coordenação Regional do ICMBio"]))
        estado = st.selectbox("Selecionar a coordenação desejada",estados)
        data = data[data["Coordenação Regional do ICMBio"] == estado]
        

if st.checkbox("Visualizar os dados sobre as queimadas no Brasil ou no Bioma especificado"):
	st.subheader("Dados sobre queimadas no Brasil")
	st.write(data)

st.subheader("Area total de cada reserva em hectares")

def queimadas_totais(data):
    areas_hec = data_cleaning(data['Área estimada da UC (ha)'])
   
    index_str = 'Área queimada em 201'
    areas_queimadas_total = [0.00 for i in range(len(areas_hec))]

    for i in range(2,9):
        areas_queimadas_tratada = data_cleaning(data[index_str+str(i)])
        data[index_str+str(i)] = [x.replace('.','') if type(x) == str else float(x) for x in data[index_str+str(i)]]
        areas_queimadas_tratada = [float(x.split(',')[0]) if type(x) == str else x for x in data[index_str+str(i)]]
        for i,x in enumerate(areas_queimadas_tratada):
            areas_queimadas_total[i]+=float(x)
    
    return areas_queimadas_total, areas_hec


areas_queimadas, areas_hec = queimadas_totais(data)
data["areas_queimadas"] = areas_queimadas

resultado = []
for total, queimado, nome in zip(areas_hec,data["areas_queimadas"],data["Nome da UC"]):
    resultado.append({"Nome":nome,"Area_Total":total,"%_de_queimadas":queimado/float(total)*100})

resultado = pd.DataFrame(resultado)
st.write(resultado.sort_values(by=['%_de_queimadas'],ascending=False))

st.header("Visualizar graficamente a quantidade de queimadas por Parque de preservação:")
parques = data_cached["Nome da UC"]
parque = st.selectbox("Selecionar a coordenação desejada",parques)
parque_data = data_cached[data_cached["Nome da UC"] == parque]

def gera_dados_individuais(parque_data):

    index_str = 'Área queimada em 201'
    areas_queimadas_tratada = []
    for i in range(2,9):
        areas_queimadas_tratada.append(data_cleaning(parque_data[index_str+str(i)]))


    return list(areas_queimadas_tratada)

def gera_anos(ano_limite):
    index_str = "201"
    anos = []
    for i in range(2,9):
        anos.append(int(index_str+str(i)))
    return anos

queimadas_parque = gera_dados_individuais(parque_data)
anos = gera_anos(2019)
plt.plot(anos,queimadas_parque)

st.pyplot()