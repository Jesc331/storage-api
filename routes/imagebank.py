import datetime as dt
import bottle
from modules.bottles import BottleJson
from modules.imagebank import (
    add_user
)

app = BottleJson()

@app.get("/home")
def display_home(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code= 501, message = "Page Not implemented")

@app.post("/store")
def store(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        user_id = str(payload['user_id'])
        username = str(payload['username'])
        password = str(payload['password'])
        print("datos validos")
        respuesta = add_user(**payload)
        print(respuesta)
        print("Apunto de terminar")
    except:
        print("datos invalidos")
        raise bottle.HTTPError(400, "Invalid data")
    raise bottle.HTTPError(201, respuesta)

@app.get("/user_list")
def get_all_users(*args, **kwargs):
    try:
        respuesta = get_storage_users()
    except:
        raise bottle.HTTPError(501, "Error")
    raise bottle.HTTPError(200, respuesta)


@app.get("/info/<code>")
def devices_per_st(*args,code=None, **kwargs):
    try:
        respuesta = get_device_list(st=code)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)

'''
@app.post("/auth/user_storage/<data>")
def create_profile(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        email = str(payload['email'])
        user = str(payload['user'])
        password = str(payload['password'])
        if "@gmail.com" in email:
	        print("Correo Valido")
        else:
	        print("Correo Invalido")
        if len(password)>= 8:
            print("Contraseña Correcta")
        else:
            print("Contraseña demasiado Corta")
    except:
        print("Datos Invalidos")
        raise HTTPError(400)
    raise HTTPError(500)
    return dict(code = 501, message = "Not implemented")

@app.get("/main/profile/reportTools/<report_id>")
def get_info_by_id(*args, **kwargs):
    # Codigo
    return dict(code = 501, message = "Not implemented")
'''
