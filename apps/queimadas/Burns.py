#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd

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

def main():
    data = pd.read_csv("DIMIF-queima.csv",delimiter=";",decimal=',')
    data.fillna(0,inplace = True)
    
    areas_hec = data_cleaning(data['Área estimada da UC (ha)'])
    
    
    index_str = 'Área queimada em 201'
    areas_queimadas_total = [0.00 for i in range(len(areas_hec))]
    for i in range(2,9):
        areas_queimadas_tratada = data_cleaning(data[index_str+str(i)])
        data[index_str+str(i)] = [x.replace('.','') if type(x) == str else float(x) for x in data[index_str+str(i)]]
        areas_queimadas_tratada = [float(x.split(',')[0]) if type(x) == str else x for x in data[index_str+str(i)]]
        for i,x in enumerate(areas_queimadas_tratada):
            areas_queimadas_total[i]+=float(x)
            
        print(areas_queimadas_tratada)
        
    
    print("\n\n\n\n\n\n")

    print(areas_queimadas_total)
    
    for i,(total, queimado) in enumerate(zip(areas_hec,areas_queimadas_total)):
        print("\t#\t",i,"\tTotal\t",total,"\tPorcentagem queimada:\t",queimado/float(total))
        
if __name__ == "__main__":
    main()


# In[2]:




