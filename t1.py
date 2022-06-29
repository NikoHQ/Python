def readFile():
	file = open("primos.txt","r")
	listFile = []
	for line in file:
		listFile.append(line.rstrip('\n'))
	file.close()
	return listFile
def obtainExp(list1):
	listExp = []
	listExp2 = []
	count = 0
	for sub_list in list1:
		count = count + 1
		aux = 0
		bas = 0
		i = 0
		while(i < len(sub_list)):
			if(sub_list[i] != ' '):
				if aux == 0:
					aux = 1						
					bas = int(sub_list[i])
				else:
					aux = 0
					listExp.append(bas**int(sub_list[i]))
			i = i + 1
		if(count == 2):
			count = 0
			aux1 = 0
			ax = 0
			for one in listExp:
				if aux1 == 0:
					ax = int(one)
					aux1 = 1
				else:
					listExp2.append(ax * int(one))
					aux1 = 0
			if((len(listExp)%2) == 1):
				listExp2.append(ax)
			listExp = []
	return listExp2
def primolandia(listExp2):
	writeList = []
	i = 0
	while(i < len(listExp2)):
		if(listExp2[i]%listExp2[i+1] == 0):
			factors = sorted(factores((int(listExp2[i]/listExp2[i+1])), llena_lista_primos(233)), reverse=True)
			find = 0
			primolandNumber = []
			used = []
			array = ""
			for number in factors:
				for r in used:
					if(number == r):
						find = 1
						break
				if(find == 0):
					primolandNumber.append(number)
					primolandNumber.append(factors.count(number))
					find = 0
			for char in primolandNumber:
				array = array + str(char) + " "
			writeList.append(array)
		else:
			writeList.append("NO DIVISIBLE")
		i = i + 2
	return writeList
def saveFile(writeList):
	file = open("resultado.txt", "w")
	for write in writeList:
		file.write(write + '\n')
	file.close()
def primo(num1):
	for x in range (1,num1):
		if (num1%x==0 and x!=num1 and x!=1):
			return False
	return num1
def llena_lista_primos(nro):
	primos = []
	for i in range(2, nro):
		if primo(i) :
			primos.append(i)
	return primos
def factores(numero, primos):
	divisibles=[]
	while numero > 1:
		if primo(numero):
			divisibles.append(numero)
			break
		for i in range(len(primos)):
			if numero % primos[i] == 0:
				divisibles.append(primos[i])
				numero = numero // primos[i]
				break
	return divisibles
if __name__ == "__main__":
	list1 = readFile()
	list2 = obtainExp(list1)
	list3 = primolandia(list2)
	saveFile(list3)