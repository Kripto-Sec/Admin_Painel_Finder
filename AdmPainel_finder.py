import requests
import sys


if len(sys.argv) < 2:
    print ("Criado por Jean(Kripto-Sec)")
    print ("github:https://github.com/Kripto-Sec")
    print ('\033[1m'+"Para usar digite python AdmPainel_finder.py https://exemplo.com wordlist.txt"+'\033[1m')
    sys.exit(0)

print("###########################")
print("#  Admin Painel Finder v1 #")
print("#  Script por Kripto-Sec  #")
print("#  Uma frase daora        #")
print("###########################")
print("\n")
	


url = sys.argv[1]

lives = []

arq = open(sys.argv[2],'r')
lines = arq.readlines()
arq.close


for line in lines:

    line = line.replace("\n", "")
    request = url+"/"+line
    http = requests.get(request)
    code = http.status_code
    if code != 301 and code != 404:
        
        if not "Page not found" in http.content:
            print('\033[;1m'+'\033[32m'+"[+] ==>> PAGINA ENCONTRADA: "+request)
            lives.append(request)
        else:
            print('\033[;1m'+'\033[31m'+"[-] ==>> PAGINA NAO ENCONTRADA: "+request)
    else:
        print('\033[;1m'+'\033[31m'+"[-] ==>> PAGINA NAO ENCONTRADA: "+request)      

print("FIM! OBRIGADO POR USAR!")
print("\n")
print('\033[1;33m'+"TODAS AS PAGINAS ENCONTRADAS")
for live in lives:
    print(live)