# Image Bank
## Consiste en:

Este proyecto almacena archivos con algun formato de imagen permitido(PNG, JPG, JPEG, GIF) subidas por el usuario, y consultar la las imagenes por su etiqueta que los usuarios añadiran al momento de subir sus archivos.
Asi como los usuarios puedan borrar sus propias imagenes si asi lo desean, y poder tener un apartado de sus propias imagenes que han subido.

## Aplicacion en:

Podemos esperar que se aplique en alguna empresa que venda o comercialice productos para el uso publico en el cual se requiera saber la opinion acerca del producto para generar actualizacion o modificaciones al producto con el fin de mejorarlo.

# Estructura deseada
Se debera de crear un banco de imagenes, lo cual debemos de pensar que entidades *necesitaremos*:

- Usuario (user_id, user, password)
- Image (name, file, owner, image_id, category, original_description)
- Comment(id_comment, image_id, user_id, description)
- Reporte( repor_id, user, status, message)

<div>
<p style = 'text-align:center;'>
<img src="/Users/salas/Downloads/ERdeHockey.png" alt="JuveYell" width="300px">
</p>
</div>

---

# Acciones que puede realizar el **administrador** de la API:
- Visualizar los reportes
- Cambiar los estados de los reportes(pediente o resuelto)
- Borrar imagenes de otros usuarios
- Fijar mensajes para los otros usuarios

# Acciones que puede realizar el usuario dentro de la API:

- Buscar imagenes
  - Por usuarios
  - Por Categoria
  - Por Nombre
- Subir imagenes
- Borrar imagenes propias
- Reportar imagenes inapropiadas

## Operaciones de Almacenamiento de datos

### Operaciones de usuarios

Subir una nueva imagen
: solicitamos categoria, nombre y path.

Actualizar de categorias
: cambiar categorias ya establecidas o agregar más.

Crear reportes
: cambiar categoria
: añadir mensajes

### Operaciones de administrador

Borrar imagenes
: solicitar nombre de la imagen y usuario
: borrar imagenes

Atender reportes
: solicitar estados del reporte y descripcion
: cambiar estados de los reportes
: añadir mensajes de retroalimentacion para el usuario

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
1. Se le pedira que inicie sesion(ingresar con su usuario y contraseña previamente registrado)
2. Se le pedira seleccionar el archivo que desea subir (debe de cumplir con los siguientes formatos: JPEG, JPG, GIF o PNG)
3. Subir archivo y esperar la confirmacion

---

Archivos relacionados a este proceso:

| Path                    | Descripción                                         |
| ----------------------- | --------------------------------------------------- |
| `/auth/login`         | Sera el archivo encargado de **recibir la informacion y compararlo en la validacion para que el usuario pueda acceder a la API**                           |
| `/main`  | Esta es la pagina de inicio donde se presentaran las imagenes que se han subido recientemente, una barra buscadora y un boton para subir nuestras imagenes que redirigira a la siguiente direccion '/main/upload' |
| `/main/upload` | Se presentara una interfaz con un formato que sera rellanado con la siguiente informacion: *Nombre del Archivo*(sera extraido del documento que seleccione el usuario), *PATH*(se extraera del archivo seleccionado), *Categoria*(El usuario debera seleccionar las distintas opciones de un 'ComboBox' )   |

## Borrar una imagen
1. Se le pedira que inicie sesion(ingresar con su usuario y contraseña previamente registrado).
2. Se le pedira seleccionar una de sus imagenes que el usuario haya subido con anterioridad.
3. Se le preguntará que confirme que si **realmente quiere borrar la imagen seleccionada**.
4. Se borrará la imagen seleccionada-

Archivos relacionados a este proceso:

| Path                    | Descripción                                         |
| ----------------------- | --------------------------------------------------- |
| `/auth/login`         | Sera el archivo encargado de **recibir la informacion y compararlo en la validacion para que el usuario pueda acceder a la API**                           |
| `/main/profile`  | En esta pagina se desplegara una interfaz donde el usuario podra ver su 'nickname' y las imagenes que ha subido hasta el momento y un boton en la parte superior de la pagina que activara el evento para 'borrar imagenes' |
| `/main/profile/delete` | Se le mostrara un 'ComboBox' de las imagenes que ha subido y seleccionara las que desea borrar luego tendra que cofirmar para borrar las imagenes.  |

# Archivos Relacionados

 -

Prefijos de almacenamiento:

 - `image-bank/`

Tablas de Base de Datos

> Pendiente o Nulo
