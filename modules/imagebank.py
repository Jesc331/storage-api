import json
import datetime as dt
from os import environ
from pathlib import Path
from modules.storage import (
    store_string, store_bytes,
    query_storage, get_storage_file
)

def get_image_to_store(collection, filename):
    target = str(Path(collection) / filename)
    blob = get_blob(target)
    if blob.exists():
        raise Exception("Image already exists")
    return blob

def get_storage_image(path=""):
    target = (storage_dir / path)
    if not target.exists() or not target.is_file():
        raise Exception("Does not exists")
    mime = (guess_type(str(target)) or ["application/octet-stream"])[0]
    return mime, target.read_bytes()

# ----------------------------------Reportes--------------------------------
def add_report(report_id = None, username = None, status = None, message = None, image_id=None):

    print(report_id, username, status, message)
    print("Tarea Realizada Correctamente")

    almacenable = {
        "report_id": report_id,
        "username": username,
        "status": status,
        "message": message,
        "image_id": image_id
    }

    nombre_de_archivo = f"{report_id}-{username}-{status}.json"
    datos = store_string(
        "image/reports",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos

def get_storage_reports(report_id=None):
    query_result = query_storage(
        "image/reports",
    )
    if report_id is None:
        return query_result["content"]
    if report_id is not None:
        return [
           r
           for r in query_result["content"]
           if report_id in r
        ]
# ----------------------------------usuarios--------------------------------
# Funcion para añadir un usuario
def add_user(user_id = None, username = None, password = None):

    print(user_id, username, password)
    print("Tarea Realizada Correctamente")

    almacenable = {
        "user_id": user_id,
        "username": username,
        "password": password,
    }

    nombre_de_archivo = f"{username}-{user_id}.json"
    datos = store_string(
        "image/users",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos

# Funcion para hacer un Get de todos los usuarios registrados
# curl http://localhost:8081/imagebank/user/list -X GET
def get_storage_users(user_id=None):
    query_result = query_storage(
        "image/users",
    )
    if user_id is None:
        return query_result["content"]
    if user_id is not None:
        return [
           r
           for r in query_result["content"]
           if user_id in r
        ]

# ----------------------------------COMENTARIOS--------------------------------
#Ejemplo
#curl http://localhost:8081/imagebank/comment -X POST -H 'Content-Type: application/json' -d '{"comment_id":"001", "image_id":"001","name":"eduardo", "user_id":"001","description":"buena imagen me gusta el fondo que tiene"}'
def add_comment(comment_id = None,  image_id = None, username = None, user_id = None , description = None):

    print("Desde Modulo add_comment")

    almacenable = {
        "comment_id": comment_id,
        "image_id": image_id,
        "username": username,
        "user_id": user_id,
        "description": description,
    }
    nombre_de_archivo = f"{comment_id}-{user}.json"
    datos = store_string(
        "image/comments",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos

# curl http://localhost:8081/imagebank/comment/list -X GET
def get_storage_comment(comment_id=None):
    query_result = query_storage(
        "image/comments",
    )
    if comment_id is None:
        return query_result["content"]
    if comment_id is not None:
        return [
           r
           for r in query_result["content"]
           if comment_id in r
        ]
# ----------------------------------IMAGENES--------------------------------
# Pendiente de revision ya que no se como guardar imagenes
'''
def add_image(image_id = None, name = None, user_id = None, category = None, description = None):

    print(image_id, name, user_id, category, description)
    print("Tarea Realizada Correctamente")

    almacenable = {
        "image_id": image_id,
        "name": name,
        "user_id": user_id,
        "category": category,
        "description": description,
    }
    nombre_de_archivo = f"{name}-{image_id}.json"
    datos = store_string(
        "image/images",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos
'''

def store_new_image(image_number=None, image_file=None):
    date = dt.date.today().isoformat()
    filename = f"{image_number}-{date}.png"
    store_bytes(
        "image/pictures",
        filename,
        image_file.read()
    )
    return f"image/pictures/{filename}"
