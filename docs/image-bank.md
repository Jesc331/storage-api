# Image Bank
## Consiste en:

Este proyecto almacena archivos con algun formato de imagen permitido(PNG, JPG, JPEG, GIF) subidas por el usuario, y consultar la las imagenes por su etiqueta que los usuarios añadiran al momento de subir sus archivos.

## Modo de uso

El usuario debera de crear un usuario para usar la API, ya que el nombre del usuario registrado tambien servira como etiqueta para buscar imagenes de alguna persona en particular y almacenar las imagenes correspondientes.

Archivos relacionados a este proceso:

| Path                    | Descripción                                         |
| ----------------------- | --------------------------------------------------- |
| /auth/login.py          | Sera el archivo encargado de recibir la informacion y compararlo en la validacion para que el usuario pueda acceder a la API                           |
|                         | Se almacenara la informacion de los usuarios en un  |
| /auth/user_storage.json | json con la siguiente estructura:                   |
|                         | {"user": "exampleName","password":"examplePass"     |
|                         | se requiere que este archivo este cifrado.          |
| ----------------------- | --------------------------------------------------- |
| ----------------------- | --------------------------------------------------- |
|                         | Este archivo ejecutara una validacion de los datos  |
| /auth/validate_user.py  | recibidos del archivo "login.py" para dar el acceso |
|                         | a usuarios registrados o denegar el acceso          |
|                         | usuarios no registrados en su contraparte           |
| ----------------------- | --------------------------------------------------- |

## API

| Path                  | Descripción |
| --------------------- | ----------- |
| /bankImg/store           |             |
| /bankImg/info/<id>       |             |
| /bankImg/void            |             |


# Archivos Relacionados

 - `routes/dell-warranty.py`

Prefijos de almacenamiento:

 - `dell-warranty/`

Tablas de Base de Datos

> Pendiente o Nulo
