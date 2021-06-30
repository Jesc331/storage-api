# Image Bank
## Consiste en:

Este proyecto almacena archivos con algun formato de imagen permitido(PNG, JPG, JPEG, GIF) subidas por el usuario, y consultar la las imagenes por su etiqueta que los usuarios añadiran al momento de subir sus archivos.

# Estrucutra deseada
Se debera de crear un banco de imagenes, lo cual debemos de pensar que entidades *necesitaremos*:

- Usuario (user, password)
- Imagen (categoria, identificador, path)

---

## Modo de uso

El usuario debera de crear un usuario para usar la API, ya que el nombre del usuario registrado tambien servira como etiqueta para buscar imagenes de alguna persona en particular y almacenar las imagenes correspondientes.

# Procesos dentro de la API
## Registro de Usuaurio
- Se solicitara un usuario, una contraseña y un correo
- Se le pedira confirmar su contraseña

Archivos relacionados a este proceso:

| Path                    | Descripción                                         |
| ----------------------- | --------------------------------------------------- |
| `/auth/login`         | Sera el archivo encargado de **recibir la informacion y compararlo en la validacion para que el usuario pueda acceder a la API**                           |
| `/auth/user_storage` | Se almacenara la informacion de los usuarios en un json con la **siguiente estructura: ```{"user": "exampleName","password":"examplePass"``` (se requiere que este archivo este cifrado.)**   |
| `/auth/validate_user`  | Este archivo **ejecutara una validacion de los datos recibidos del archivo "login.py"** para dar el acceso a usuarios registrados o denegar el acceso usuarios no registrados en su contraparte |

 ---

## Subir una imagen
- Se le pedira que inicie sesion(ingresar con su usuario y contraseña previamente registrado)
- Se le pedira seleccionar el archivo que desea subir (debe de cumplir con los siguientes formatos: JPEG, JPG, GIF o PNG)
- Subir archivo y esperar la confirmacion

Archivos relacionados a este proceso:

| Path                    | Descripción                                         |
| ----------------------- | --------------------------------------------------- |
| `/auth/login`         | Sera el archivo encargado de **recibir la informacion y compararlo en la validacion para que el usuario pueda acceder a la API**                           |
| `/main`  | Esta es la pagina de inicio donde se presentaran las imagenes que se han subido recientemente, una barra buscadora y un boton para subir nuestras imagenes que redirigira a la siguiente direccion '/main/upload' |
| `/main/upload` | Se presentara una interfaz con un formato que sera rellanado con la siguiente informacion: *Nombre del Archivo*(sera extraido del documento que seleccione el usuario), *PATH*(se extraera del archivo seleccionado), *Categoria*(El usuario debera seleccionar las distintas opciones de un 'ComboBox' )   |

Acciones dentro de la API:

- Buscar imagenes por categoria
- Buscar imagenes por nombre
- Buscar imagenes por usuario
- Subir imagenes
- Borrar imagenes

# Archivos Relacionados

 - `routes/dell-warranty.py`

Prefijos de almacenamiento:

 - `dell-warranty/`

Tablas de Base de Datos

> Pendiente o Nulo
