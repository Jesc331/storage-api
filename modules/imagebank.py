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

# Sacar un usuario en especifico por ID
def get_user_by_id(user_id=None):
    query_result = query_storage(
    "image/users"
    )
    if user_id is None:
        return query_result["content"]
    if user_id is not None:
        return [
            r
            for r in query_result["content"]
            if user_id in r
        ]

def get_image_details(image_id=None):
    query_result = query_storage(
        "image/images",
    )
    if image_id is not None:
        return [
           r
           for r in query_result["content"]
           if movie_id in r
        ]
    print("Procesando Informacion")

def get_comments_from_image(image_id = None, description = None):
    print("Desde modulo imageBank.py")
    print(image, description)
    print("Tarea realizada exitosamente")

def add_comment(id_comment = None, user_id = None, image_id = None, name = None, description = None):

    print("Desde Modulo add_comment")
    print(id_comment, user_id, image_id, name, description)
    print("Tarea realizada exitosamente")

    almacenable = {
        "id_comment": id_comment,
        "image_id": image_id,
        "name": name,
        "user_id": user_id,
        "category": category,
        "description": description,
    }
    nombre_de_archivo = f"{review_id}-{movie_title}.json"
    datos = store_string(
        "images/comments",
        nombre_de_archivo,
        json.dumps(almacenable)
    )
    return datos
