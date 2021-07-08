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
<img src="https://github.com/Jesc331/storage-api/blob/master/images_resources/ERdeHockey.png" alt="ERD" width="640px">
</p>
</div>

---
# Consulta de Datos
- Solicitar una imagen
  - por el id de la imagen
  - por el usuario
  - por la categoria
- solicitar reporte
  - por el usuario
  - por el id del reporte
  - por el status
- solicitar un cometario
  - por el id del comentario
  - por el id de la imagen
  - por el usuario
---
# Acciones que se pueden realizar en la API:
## *Administrador*
- Visualizar todos los reportes(`app:imageReports:read:all`)
- Cambiar los estados de los reportes(`app:imageReports:update:all`)
- Borrar reportes de los usuarios(`app:imageReports:delete:all`)
- Borrar imagenes de otros usuarios(`app:imageBank:delete:all`)
- Solicitar imagenes de otros usuarios(`app:imageBank:read:all`)

## *Usuario*
- Buscar sus imagenes y de otros usuarios (`app:imageBank:read:all`)
- Subir imagenes a su cuenta (`app:imageBank:write:self`)
- Actualizar descripciones de sus imagenes (`app:imageReports:update:self`)
- Eliminar imagenes de su cuenta (`app:imageBank:delete:self`)
- Reportar imagenes inapropiadas (`app:imageReports:write:self`)
- Eliminar sus reportes (`app:imageReports:read:all`)

 ---
## Ruta relativa para los Archivos

Se propone que se siga la siguiente estructura para los documentos para asi mismo contruir las rutas.

<div>
<p style = 'text-align:center;'>
<img src="https://github.com/Jesc331/storage-api/blob/master/images_resources/Rutas%20HTTP.png" alt="RHTTP" width="640px">
</p>
</div>

La intencion de presentar esta imagen es que se sepa donde se deban dirigir los documentos para cada proceso.

## Modo de uso

El usuario debera de crear un usuario para usar la API, ya que el nombre del usuario registrado tambien servira como etiqueta para buscar imagenes de alguna persona en particular y almacenar las imagenes correspondientes.

# Procesos dentro de la API

## Registro de Usuaurio
1. Se solicitara un usuario, una contraseña
2. Se le pedira confirmar su contraseña

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

Archivos relacionados a este proceso:

| Path                    | Descripción                                         |
| ----------------------- | --------------------------------------------------- |
| `/auth/login`         | Sera el archivo encargado de **recibir la informacion y compararlo en la validacion para que el usuario pueda acceder a la API**                           |
| `/main/home`  | Esta es la pagina de inicio donde se presentaran las imagenes que se han subido recientemente, una barra buscadora y un boton para subir nuestras imagenes que redirigira a la siguiente direccion '/main/upload' |
| `/main/upload` | Se presentara una interfaz con un formato que sera rellanado con la siguiente informacion: *Nombre del Archivo*(sera extraido del documento que seleccione el usuario), *PATH*(se extraera del archivo seleccionado), *Categoria*(El usuario debera seleccionar las distintas opciones de un 'ComboBox' )   |

---

## Borrar una imagen
1. Se le pedira que inicie sesion(ingresar con su usuario y contraseña previamente registrado).
2. Se le pedira seleccionar una de sus imagenes que el usuario haya subido con anterioridad.
3. Se le preguntará que confirme que si **realmente quiere borrar la imagen seleccionada**.
4. Se borrará la imagen seleccionada-

Archivos relacionados a este proceso:

| Path                    | Descripción                                         |
| ----------------------- | --------------------------------------------------- |
| `/auth/login`         | Sera el archivo encargado de **recibir la informacion y compararlo en la validacion para que el usuario pueda acceder a la API**                           |
| `/main/profile/user_home`  | En esta pagina se desplegara una interfaz donde el usuario podra ver su 'nickname' y las imagenes que ha subido hasta el momento y un boton en la parte superior de la pagina que activara el evento para 'borrar imagenes' y otro mas para `crar reportes` |
| `/main/profile/delete` | Se le mostrara un 'ComboBox' de las imagenes que ha subido y seleccionara las que desea borrar luego tendra que cofirmar para borrar las imagenes.  |

---

## Crear un reporte
1. Se le pedira que inicie sesion(ingresar con su usuario y contraseña previamente registrado).
2. Se le pedira dirigirse a su perfil donde podra ver un **boton** para crear reportes.
3. Se desplegara un recuadro donde rellenara un formulario con los siguientes datos: **user, id_image y un mensaje acerca del problema**.
4. Pulsar el **boton** de enviar y esperar respuesta del administrador

Archivos relacionados a este proceso:

| Path                    | Descripción                                         |
| ----------------------- | --------------------------------------------------- |
| `/auth/login`         | Sera el archivo encargado de **recibir la informacion y compararlo en la validacion para que el usuario pueda acceder a la API**                           |
| `/main/profile`  | En esta pagina se desplegara una interfaz donde el usuario podra ver su 'nickname' y las imagenes que ha subido hasta el momento y un boton en la parte superior de la pagina que activara el evento para + ´borrar imagenes´ y otro mas para `crar reportes` |
| `/main/profile/reportTools` | Se les redirigirá a otra pagina donde estara el formato de reporte correspondiente donde contener lo siguiente 3 `textbox` para el  `id de la imagen', 'nombre del usuario' y 'mensaje del reporte'   |

---
# Estructuras de solicitud y respuesta

## Registrar a un usuario
```
{
  "user": "eduardo33",
  "password": "hello123"
}
```
### Respuesta a un usuario registrado
```
{
  "message": "usuario <user> registrado exitosamente",
  "user" : "eduardo33"
}
```
### Mensaje de fallo
```
{
  "code": 500,
  "message" : "fallo de registro intentalo nuevamente"
}
```
---

## Subir una imagen
```
{
  "name": "paisaje montañas",
  "file": "C:/Users/salas/ComputoenlaNube/bottle-demo/storage-api/images_resources.png",
  "owner" : "eduardo33",
  "category" : {
      "tag1" : "landscape",
      "tag2" : "nature"
    },
  "original_description" : "Un hermoso paisaje de unas montañas"
}
```
### Respuesta de una imagen correctamente subida
```
{
  "code" : 201,
  "message": "imagen <name> subida correctamente"
}
```
### Mensaje de fallo
```
{
  "code": 400,
  "message" : "Requisitos faltantes, por favor buscar errores en el formulario"
}
{
  "code": 500,
  "message" : "Algo falló en el servidor, por favor intentalo nuevamente"
}
```
---
## Crear un reporte
```
{
  "user": "eduardo33",
  "message": "esta imagen es inadecuada"
}
```
### Respuesta de un reporte recibido correctamente
```
{
  "code" : 201,
  "report_id": "acb123",
  "message": "se ha recibido su reporte <report_id> ",
  "status" : "open",
}
```
### Mensaje de fallo
```
{
  "code": 400,
  "message" : "Requisitos faltantes, por favor buscar errores en el formulario"
}
{
  "code": 500,
  "message" : "Algo falló en el servidor, por favor intentalo nuevamente"
}
```
---
## Borrar una imagen
```
{
  "user": "eduardo33",
  "name"¨: "paisaje montañas",
  "image_id": "a12",
}
```
### Respuesta de que la imagen fue borrada correctamente
```
{
  "code" : 201,
  "image_id": "a12",
  "name": "paisaje montañas",
  "message" : "la imagen <paisaje montañas> fue eliminada",
}
```
### Mensaje de fallo
```
{
  "code": 400,
  "message" : "Requisitos faltantes, por favor buscar errores en el formulario"
}
{
  "code": 500,
  "message" : "Algo falló en el servidor, por favor intentalo nuevamente"
}
```
---
#Implementacion de rutas para los recursos
