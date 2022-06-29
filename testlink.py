from numpy import inf


if __name__=="__main__":
    archivo = open("casosconfirmados.csv");
    for elem in archivo:
        info = elem.rstrip("\n").split(",")
        if(info[0]=="Maule" or info[0]=="Total"):
            print(info)
            print("si")



