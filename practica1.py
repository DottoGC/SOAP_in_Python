#IMPORTACION DE LIBRERIA USADA LLAMADA ZEEP
from zeep  import Client 

#CREACION VARIABLE QUE REFERENCIA AL WEB SERVICES
client = Client(wsdl="https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=soap&wsdl") 

				
#CICLO QUE UTILIZA FUNCION PARA OBTENER CLIENTES
for c in client.service.readList():    
        print(c.name) 



#CICLO QUE UTILIZA FUNCION PARA INGRESAR 10 CLIENTES SOLICITADOS
c = 0 
for i in range(10): 
    if c < 10: 
        print("ingreasndo... ",client.service.create("201020975_"+str(c))) 
    c +=1 



#CICLO QUE UTILIZA FUNCION PARA OBTENER CLIENTES ESPECIFICOS ENVIANDO PARAMETROS
for c in client.service.readList(0,10,201020975):    
        print(c.name) 