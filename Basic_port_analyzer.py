import nmap
import pyfiglet 

banner = pyfiglet.figlet_format("PORT STATUS")

print(banner)

target = input("Especifique la IP que desea analiazar ")

start  = int(input("Diga el puerto del que le gustaria iniciar "))

end = int(input("Diga el puerto donde le gustaria finalizar "))

print("-" * 50)

print("Analizando la ip " + target)

print("Analizando desde el puerto " + str(start) + " hasta " + str(end))

scanner = nmap.PortScanner()

for i in range(start, end+1):
	
	res = scanner.scan(target,str(i))


	res = res["scan"][target]["tcp"][i]["state"]
	
	print(f"port {i} is {res}. ")

