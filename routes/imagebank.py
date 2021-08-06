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
# -----------------------------REPORTES-------------------------------
@app.get("/report/<code>")
def reports_per_id(*args,code=None, **kwargs):
    try:
        respuesta = get_storage_reports(report_id=code)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)

@app.get("/report/list")
def get_all_reports(*args, **kwargs):
    try:
        respuesta = get_storage_reports()
    except:
        raise bottle.HTTPError(501, "Error")
    raise bottle.HTTPError(200, respuesta)

@app.post("/report")
def report(*args, **kwargs):
    payload = bottle.request.json
    print(payload)
    try:
        report_id = str(payload['report_id'])
        username = str(payload['username'])
        status = str(payload['status'])
        message = str(payload['message'])
        image_id = str(payload['image_id'])
        print("datos validos")
        respuesta = add_report(**payload)
        print(respuesta)
        print("Apunto de terminar")
    except:
        print("datos invalidos")
        raise bottle.HTTPError(400, "Invalid data")
    raise bottle.HTTPError(201, respuesta)

# -----------------------------USUARIOS-------------------------------
@app.get("/user/<code>")
def users_per_id(*args,code=None, **kwargs):
    try:
        respuesta = get_storage_users(user_id=code)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)

@app.get("/user/list")
def get_all_users(*args, **kwargs):
    try:
        respuesta = get_storage_users()
    except:
        raise bottle.HTTPError(501, "Error")
    raise bottle.HTTPError(200, respuesta)

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
# -----------------------------Imagenes-------------------------------
@app.post("/image/new")
def new_image(*args, **kwargs):
    payload = bottle.request.json
    obligatory_fields = ['image_id', 'name', 'username', 'category']
    try:
        if any(key not in payload for key in obligatory_fields):
            raise Exception()
        print("Valid data")
        respuesta = store_new_image(**payload)
    except:
        print("Invalid data")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(201, respuesta)

@app.post("/image/new/<image_number>")
def new_image(image_number):
    try:
        image_file = bottle.request.files.get("image_file")
        extension = image_file.filename.split(".")[-1]
        payload = {
            "image_number": image_number,
            "image_file": image_file.file,
            "image_ext": image_file.filename.split(".")[-1]
        }
        if extension == "jpg" or extension == "jpeg" or extension == "png" or extension == "gif":
            respuesta = store_new_image(**payload)
    except:
        print("Invalid data")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(201, respuesta)

@app.get("/image/pictures/<code>")
def pictures_per_id(*args,code=None, **kwargs):
    try:
        respuesta = get_storage_pictures(image_number=code)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)

@app.get("/image/pictures/list")
def get_all_pictures(*args, **kwargs):
    try:
        respuesta = get_storage_pictures()
    except:
        raise bottle.HTTPError(501, "Error")
    raise bottle.HTTPError(200, respuesta)
# -----------------------------COMENTARIOS-------------------------------
@app.get("/comment/<code>")
def comments_per_id(*args,code=None, **kwargs):
    try:
        respuesta = get_storage_comment(comment_id=code)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)

@app.get("/comment/list")
def get_all_comments(*args, **kwargs):
    try:
        respuesta = get_storage_comment()
    except:
        raise bottle.HTTPError(501, "Error")
    raise bottle.HTTPError(200, respuesta)

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
