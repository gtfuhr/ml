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
def main():
    data = pd.read_excel("DIMIF-queima.csv",delimiter=";",decimal='.')
    areas_hec = data['Área estimada da UC (ha)']
    areas_queimada = data['Área queimada em 2016']

    print(areas_queimada)    

if __name__ == "__main__":
    main()