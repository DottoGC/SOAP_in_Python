#IMPORTACION DE LIBRERIAS
import requests
import json


# URL DE SERVIDOR DE TOKENS
endpoint = "https://api.softwareavanzado.world/index.php?option=token&api=oauth2"

# CREACION DE PARAMETROS NECESARIOS PARA EL HEADER O ENCABEZADO
headers = {"client_id":"sa",
            "client_secret":"fb5089840031449f1a4bf2c91c2bd2261d5b2f122bd8754ffe23be17b107b8eb103b441de3771745",
            "grant_type": "client_credentials",
            }

# OBTENEMOS RESPU7ESTA DEL SERVIDOR DE AUTENTICACION QUE MANEJA LA CREACION DE TOKENS
response = requests.post(endpoint, data=headers)

#imprimirmos el status del response
print("status cod:", response.status_code)
print(response.json()["access_token"])

# GUARDAMOS EL BEARER TOKEN EN UNA VARIABLE
bearer = response.json()["access_token"]

# URL DE LA API RESTful PARA LA CREACION DE UN OBJETO
endpoint = "https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=hal"

# BUCLE FOR PARA LA CREACION DE 10 OBJETOS
c=0
for i in range(10):
    if c<10:
        data = {"name":"201020975-"+str(c)}
        headers = { "Authorization": "Bearer "+str(bearer)}
        response = requests.post(endpoint, data=data, headers=headers )
    c+=1


# URL DE LA API RESTful PARA LISTAR OBJETOS CREADOS
endpoint = "https://api.softwareavanzado.world/administrator/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=hal&filter[search]=201020975-"
headers = { "Authorization": "Bearer "+str(bearer)}
response = requests.get(endpoint, headers=headers )


# IPRIMIMOS RESPUESTA FINAL FILTRADA
print(response.json())