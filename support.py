from csv import reader

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',')
        #print(level_map) -
        #print(layout)
        for row in layout:
            terrain_map.append(list(row))
            #print(row)
        return terrain_map

#print(import_csv_layout('mapa/mapa1_CSV._Delimitador.csv'))