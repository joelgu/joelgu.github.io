import requests
header={'Accept': 'application/json, text/plain, */*',
        'Content-Type':'application/json'}
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
datos_user={"password": "sin_pass", "username": "joelgu"}
acceso_usuario=requests.post("https://universewars.io/api/v1/auth/authenticate",verify=False, json=datos_user, proxies=proxy).json()
headers = {'Authorization': 'Bearer '+acceso_usuario["access_token"]}
#print(acceso_usuario["access_token"])
datos_warbots=requests.get("https://universewars.io/api/v1/warbot/filter?&page=0", verify=False, headers=headers)
print(datos_warbots.json)
#print(datos_warbots.json())
print("Tienes "+str(datos_warbots.json()["totalElements"]) + " Warbots")
