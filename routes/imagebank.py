import datetime as dt
import bottle
from modules.bottles import BottleJson
from modules.imagebank import *
app = BottleJson()

@app.get("/home")
def display_home(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code= 501, message = "Page Not implemented")

# -----------------------------USUARIOS-------------------------------
@app.post("/register")
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

@app.get("/user/list")
def get_all_users(*args, **kwargs):
    try:
        respuesta = get_storage_users()
    except:
        raise bottle.HTTPError(501, "Error")
    raise bottle.HTTPError(200, respuesta)

@app.get("/user/<code>")
def devices_per_id(*args,code=None, **kwargs):
    try:
        respuesta = get_storage_users(user_id=code)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)
# -----------------------------COMENTARIOS-------------------------------
@app.post("/comment")
def comment(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        comment_id = str(payload['comment_id'])
        image_id = str(payload['image_id'])
        user = str(payload['user'])
        user_id = str(payload['user_id'])
        description = str(payload['description'])
        print("datos validos")
        respuesta = add_comment(**payload)
        print(respuesta)
        print("Apunto de terminar")
    except:
        print("datos invalidos")
        raise bottle.HTTPError(400, "Invalid data")
    raise bottle.HTTPError(201, respuesta)

@app.get("/comment/list")
def get_all_comments(*args, **kwargs):
    try:
        respuesta = get_storage_comment()
    except:
        raise bottle.HTTPError(501, "Error")
    raise bottle.HTTPError(200, respuesta)
