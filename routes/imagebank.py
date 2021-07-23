import bottle
from modules.auth import auth_required
from modules.bottles import BottleJson

app = BottleJson()

@app.get("/home")
def display_home(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code= 501, message = "Page Not implemented")

@app.get("/")
def index():
    payload = bottle.request.query
    print(bottle.request.query)
    print(payload.dict)
    raise bottle.HTTPError(501, 'Error')

@app.get("/home/<image_id>")
def get_image(image_id):
    print(image_id)
    raise bottle.HTTPError(501, 'Error')

@app.get("/main/profile/user_home/<user_id>")
def get_user(user_id):
    print(user_id)
    raise bottle.HTTPError(501, 'Error')

@app.delete("/main/profile/delete/<image_id>")
def delete_images(image_id):
    print(image_id)
    raise bottle.HTTPError(501, 'Error')

@app.get("/main/profile/reportTools")
def display_report_tools(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code= 501, message = "Page Not implemented")

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
