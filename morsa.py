

def traduct(palabra)
    morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    palabra =str.lower(input())
    
    palabra= palabra.replace("á", "a")
    palabra= palabra.replace("é", "e")
    palabra= palabra.replace("í", "i")
    palabra= palabra.replace("ó", "o")
    palabra= palabra.replace("ú", "u")
    palabra= palabra.replace("ü", "u")
    palabra= palabra.replace("ñ", "n")

    for elem in alfabeto:
        if palabra.replace(elem, morse) 

#    for morse in alfabeto:
#        if palabra.replace(morse, alfabeto) 

#Codigo principal
if (__name__=="__main__"):
    entrada = input ()
    resultado = traduct(entrada)
            
    