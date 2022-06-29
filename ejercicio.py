#PANGRAMA 

def valPangrama(cadena):
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    cadena =str.lower(input())
    
    cadena= cadena.replace("á", "a")
    cadena= cadena.replace("é", "e")
    cadena= cadena.replace("í", "i")
    cadena= cadena.replace("ó", "o")
    cadena= cadena.replace("ú", "u")
    cadena= cadena.replace("ü", "u")
    cadena= cadena.replace("ñ", "n")

    for elem in letras:
        if cadena.count(elem) == 0:
            return False
    return False

#Codigo principal    

if (__name__=="__main__"):
    entrada = input ()
    resultado = valPangrama(entrada)
    if (resultado):
        print("Si es pangrama")
    else:
        print("No es pangrama")