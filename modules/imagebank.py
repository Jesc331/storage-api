import json
from datetime import datetime
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
# curl http://localhost:8081/imagebank/user_list -X GET
def get_storage_users(path=None):
    query_result = query_storage(
        "image/users",
    )
    print(query_result)
    return query_result['content']

# Funcion para hacer un Get de todos los usuarios registrados
# curl http://localhost:8081/imagebank/user/<user_id> -X GET
def get_user_by_id(user_id=None):
    print(username, password)
    print("Exito")


# ----------------------------------COMENTARIOS--------------------------------

def add_comment(comment_id = None,  image_id = None, user = None, user_id = None , description = None):

    print("Desde Modulo add_comment")

    almacenable = {
        "comment_id": comment_id,
        "image_id": image_id,
        "user": user,
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

def get_storage_comment(path=None):
    query_result = query_storage(
        "image/comments",
    )
    print(query_result)
    return query_result['content']
