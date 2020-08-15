# IMPORTACION DE LIBRERIAS
from requests.auth import HTTPBasicAuth
from requests import Session
from zeep import Client
from zeep.transports import Transport


# DECLARACION DE VARIABLES NECESARIAS PARA LA SOLUCION
session = Session()
user = 'sa'
password = 'usac'

# UTILIZACION DE METODO AUTH DE LA SESION CREADA COMO VARIABLE ANTERIORMENTE
session.auth = HTTPBasicAuth(user, password)

# CODIGO PARA REALIZAR REQUEST CON TODOS LAS VARIABLES NECESARIAS DE AUTENTICACION
client = Client(wsdl='https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=soap&wsdl',
            transport=Transport(session=session))


# BUCLE FOR PARA CREACION DE OBJETOS
c = 0
for i in range(10):
    if c<10:
        print("ingresando...",client.service.create("201020975-basicA-"+str(c))) 
    c+=1

        
#CICLO QUE UTILIZA FUNCION PARA OBTENER CLIENTES ESPECIFICOS ENVIANDO PARAMETROS PARA UN FILTRADO
for c in client.service.readList(0,10,"201020975-basicA"):    
    print(c.name)
