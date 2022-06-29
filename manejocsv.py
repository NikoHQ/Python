
contador_hombres_colom=0
miarchivo=open("testeocsv.csv", "r")
#lectura = miarchivo.readline() Lee toda una linea
lectura = miarchivo.readline() 

for i in range(10):
    lectura=miarchivo.readline().split(",") #Divide las lineas y se invocan con [0,2,etc...]
    if lectura[2]=="hombre":    #Comprueba si son hombres y los añade
        if lectura[4]=="colombia\n":    #Aparte de ser hombres deben cumplir con ser de colombia
            contador_hombres_colom=contador_hombres_colom+1

print("numero de hombres:", contador_hombres_colom ) #Lee las divisiones