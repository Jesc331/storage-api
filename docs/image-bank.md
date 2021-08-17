# Image Bank
## Consiste en:

Este proyecto almacena archivos con algún formato de imagen permitido
(PNG, JPG, JPEG, GIF) o mejor conocidas como imágenes que serán subidas por el
usuario, y se puedan consultar y visualizar las imágenes por su categoria que los
usuarios añadirán al momento de subir sus archivos. Así como los usuarios puedan
borrar sus propias imágenes si así lo desean, y poder tener un apartado de sus
propias imágenes que han subido.

## Aplicación en:

Podemos esperar que se aplique en alguna empresa que venda o comercialice
productos para el uso público en la cual se requiere saber la opinión acerca
del producto para generar actualización o modificaciones al producto con el
fin de mejorarlo.

# Estructura deseada
Se deberá de crear un banco de imágenes, lo cual debemos de pensar que
entidades *necesitaremos*:

- Usuario (user_id, user, password)
- Image (name, file, owner, image_id, category, original_description)
- Comment(id_comment, image_id, user_id, description)
- Reporte( repor_id, user, status, message)

<div>
<p style = 'text-align:center;'>
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/ERdeHockey.png" alt="ERD" width="640px">
</p>
</div>

---
# Consulta de Datos
- Solcitar un usuario
  - Por ID de usuario
  - Por username
- Solicitar una imágen
  - por el id de la imágen
  - por la fecha de subida
  - por extensión
- solicitar reporte
  - por el usuario
  - por el id del reporte
  - por el status
- solicitar un comentario
  - por el id del comentario
  - por el id de la imágen
  - por el usuario
---
# Acciones que se pueden realizar en la API:
## *Administrador*
- Visualizar todos los reportes(`app:imageReports:read:all`)
- Cambiar los estados de los reportes(`app:imageReports:update:all`)
- Borrar reportes de los usuarios(`app:imageReports:delete:all`)
- Borrar imágenes de otros usuarios(`app:imageBank:delete:all`)
- Solicitar imágenes de otros usuarios(`app:imageBank:read:all`)

## *Usuario*
- Buscar sus imágenes y de otros usuarios (`app:imageBank:read:all`)
- Subir imágenes a su cuenta (`app:imageBank:write:self`)
- Actualizar descripciones de sus imagenes (`app:imageReports:update:self`)
- Eliminar imágenes de su cuenta (`app:imageBank:delete:self`)
- Reportar imágenes inapropiadas (`app:imageReports:write:self`)
- Eliminar sus reportes (`app:imageReports:read:all`)

 ---
## Ruta relativa para los Archivos

Se propone que se siga la siguiente estructura para los documentos para
así mismo contruir las rutas.

<div>
<p style = 'text-align:center;'>
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/Rutas%20HTTP.png" alt="RHTTP" width="640px">
</p>
</div>

La intención de presentar esta imagen es que se sepa donde se deban dirigir
los documentos para cada proceso.

## Modo de uso
Con las siguientes descripciones se busca que se te mantenga en claro lo que
se quiere lograr en esta API

El usuario deberá de crear un usuario para usar la API, ya que el nombre
del usuario registrado también servirá como etiqueta para buscar imágenes
de alguna persona en particular y almacenar las imágenes correspondientes.

Habrá una sección en la cual se podrán crear reportes para avisar a los
administradores sobre imágenes inapropiadas para que sean eliminadas así como
también podrían usar esta función para reportar bugs o errores.

Por último una página de inicio donde habrá una barra buscadora donde podrán
visualizar y buscar las imágenes de otros usuarios.

# Procesos dentro de la API

## Registro de Usuario
1. Se solicitará un usuario, una contraseña
2. Se le pedirá confirmar su contraseña

Archivos relacionados con este proceso:

| Path                    | Descripción                                         |
| ----------------------- | --------------------------------------------------- |
| `/user/login`         | Será el archivo encargado de **recibir la información
y compararlo en la validación para que el usuario pueda acceder a la API**                           |
| `/user/list` | Se almacenará la información de los usuarios en un JSON
 con la **siguiente estructura: ```{"user_id": "001","username": "exampleName","password":"examplePass"``` (se requiere que este archivo este cifrado.)**   |
| `/user/validate_user`  | Este archivo **ejecutará una validación de los datos
recibidos del archivo "login.py"** para dar el acceso a usuarios
registrados o denegar el acceso usuarios no registrados en su contraparte |
| `/user/<code>`  | Esta dirección es para hacer una consulta y extraer la información de un usuario segun los parametros definidos en la consulta. |

 ---

 ## Subir una imagen
 1. Se le pedirá que inicie sesión(ingresar con su usuario y contraseña
   previamente registrado)
 2. Se le pedirá seleccionar el archivo que desea subir
 (debe de cumplir con los siguientes formatos: JPEG, JPG, GIF o PNG)
 3. Subir archivo y esperar la confirmación

 Archivos relacionados con este proceso:

 | Path                    | Descripción                                       |
 | ----------------------- | ------------------------------------------------- |
 | `/user/login`         | Será el archivo encargado de **recibir la información y compararlo en la validación para que el usuario pueda acceder a la API**   |
 | `/main/home`  | Esta es la página de inicio donde se presentaran las imágenes
que se han subido recientemente, una barra buscadora y un botón para subir
nuestras imágenes que redirigirá a la siguiente dirección '/main/upload' |
 | `/image/new` | Se presentará una interfaz con un formato que será rellenado
  con la siguiente información: *Nombre del Archivo*
  (será extraído del documento que seleccione el usuario),
  *PATH*(se extraerá del archivo seleccionado), *Categoría*
  (El usuario deberá seleccionar las distintas opciones de un 'ComboBox')   |

---

## Borrar una imagen
1. Se le pedirá que inicie sesión(ingresar con su usuario y contraseña
  previamente registrado).
2. Se le pedirá seleccionar una de sus imágenes que el usuario haya subido
con anterioridad.
3. Se le preguntará que confirme que si **realmente quiere borrar la imagen seleccionada**.
4. Se borrará la imagen seleccionada-

Archivos relacionados con este proceso:

| Path                    | Descripción                                         |
| ----------------------- | --------------------------------------------------- |
| `/auth/login`         | Será el archivo encargado de **recibir la información
 y compararlo en la validación para que el usuario pueda acceder a la API**                           |
| `/main/profile/user_home`  | En esta página se desplegará una interfaz donde
el usuario podrá ver su 'nickname' y las imágenes que ha subido hasta el momento
 y un botón en la parte superior de la página que activará el evento para
 'borrar imágenes' y otro más para `crar reportes` |
| `/main/profile/delete` | Se le mostrara un 'ComboBox' de las imágenes que ha
subido y seleccionara las que desea borrar luego tendrá que confirmar para
borrar las imágenes.  |

---

## Crear un reporte
1. Se le pedirá que inicie sesión(ingresar con su usuario y contraseña
  previamente registrado).
2. Se le pedirá dirigirse a su perfil donde podrá ver un **botón** para crear reportes.
3. Se desplegara un recuadro donde rellenara un formulario
con los siguientes datos: **user, id_image y un mensaje acerca del problema**.
4. Pulsar el **botón** de enviar y esperar respuesta del administrador

Archivos relacionados con este proceso:

| Path                    | Descripción                                         |
| ----------------------- | --------------------------------------------------- |
| `/auth/login`         | Será el archivo encargado de
**recibir la información y compararlo en la validación para que el usuario pueda acceder a la API**                           |
| `/main/profile`  | En esta página se desplegará una interfaz donde
el usuario podrá ver su 'nickname' y las imágenes que ha subido
hasta el momento y un botón en la parte superior de la página
que activara el evento para ´borrar imágenes´ y otro más para `crear reportes` |
| `/imagebank/report` | Se les redirigirá a otra página donde estará
el formato de reporte correspondiente donde contener lo siguiente 3 `textbox`
para el  'id de la imagen', 'nombre del usuario' y 'mensaje del reporte'    |
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
  "code" : 201,
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
# Implementacion de rutas para los recursos
`POST /auth/user_storage`
- Recibe una estructura para registrar un usuario nuevo.
- 201, registra al usuario y regresa un mensaje informando que se ha
registrado exitosamente.
- D.O.M. regresa un mensaje de falla del servidor(500) o falla del usuario(400).

<div>
<p style = 'text-align:center;'>
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/login_register_messages.png" width="480px">
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/login_register_OK.png"  width="480px">
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/login_register_error.png"  width="480px">
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/login_register_error2.png"  width="480px">
</p>
</div>

`GET /auth/login`
- Recibe una estructura para consultar un usuario existen.
- 201, se reconoce al usuario por sus credenciales y se le permite el acceso a la API.
- D.O.M. regresa un mensaje de falla del servidor(500) o falla del usuario(400)

<div>
<p style = 'text-align:center;'>
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/login_layout.png"  width="480px">
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/login_options.png" width="480px">
</p>
</div>

`GET /main/home`
- Recibe una petición para mostrar la página principal de la API.
- 201, se despliega la página de inicio de la API..
- D.O.M. regresa un mensaje de falla del servidor(500).

<div>
<p style = 'text-align:center;'>
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/home_layout.png"  width="480px">
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/home_layout2.png"  width="480px">
</p>
</div>

`POST /image/new`
- Recibe una estructura para subir una imagen nueva.
- 201, sube correctamente la imagen y se guarda en el almacenamiento
de la API y muestra un mensaje de que el proceso se realizó correctamente.
- D.O.M. regresa un mensaje de falla del servidor(500) o falla del usuario(400)

<div>
<p style = 'text-align:center;'>
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/uploaded_layout.png"  width="480px">
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/uploaded_succesfully.png"  width="480px">
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/uploaded_error.png"  width="480px">
</p>
</div>

`GET /main/profile/user_home`
- Recibe una petición para mostrar la página del perfil del usuario.
- 201, se desplega una página en la cual podra ver las imagenes que
ha subido ese usuario y un botón para eliminar y crear reportes.
- D.O.M regresa un mensaje de falla del servidor(500) o falla del usuario(400)

<div>
<p style = 'text-align:center;'>
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/create_reports_layout.png"  width="480px">
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/delete_images.png"  width="480px">

`DELETE /main/profile/delete`
- Recibe una estructura para eliminar una imagen en especifico
- 201, se muestra un mensaje de que la tarea se realizo con exitosamente.
- D.O.M regresa un mensaje de falla del servidor(500) o falla del usuario(400)

<div>
<p style = 'text-align:center;'>
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/delete_images_process.png"  width="480px">
</p>
</div>


`POST /main/profile/reportTools`
- Recibe crear un reporte que recibirá el administrador
- 201, se muestra un mensaje de que la tarea se realizo con exitosamente.
- D.O.M regresa un mensaje de falla del servidor(500) o falla del usuario(400)


<div>
<p style = 'text-align:center;'>
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/reports_layout.png" width="480px">
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/report_message_ok.png"  width="480px">
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/report_message_error.png"  width="480px">
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/report_message_ok2.png"  width="480px">
</p>
</div>

---
# Casos De uso 1

## Como subir una imágen a la API utilizando CURL
Este es la función principal que necesitaremos en la API, con ello podremos subir imágenes utilizando la siguiente estructura donde se debera especificar la ruta muy importante poner un "@" al inicio y sin caracteres especiales como ":$·" y procurar que el ID no se repita ya que fallara el CURL ya que no se permiten los ID repetidos.

### Estructura del CURL
```
curl http://localhost:8081/imagebank/register \
-X POST \
-H 'Content-Type: multipart/form-data' \
-F 'image_file=@/C/prueba3.gif'
```
Con -X especificamos el metodo
Con -H especificamos el header
Con -F especificamos la ruta de nuestro archivo asignando a la variable "image_file"
---
# Casos De uso 2

## Como crear un usuario en la API utilizando CURL
Con esta función se plantea crear usuarios con su respectiva user_id, username y contraseñas para despues poder logearse en la pagina en la interfaz que se plantea tener un futuro, pero por ahora se pueden crear usuarios sin problemas.

### Estructura del CURL
```
curl http://localhost:8081/imagebank/register \
-X POST \
-H 'Content-Type: application/json' \
-d '{"user_id":"001", "username":"eduardo", "password":"hola123"}'
```
Con -X especificamos el metodo
Con -H especificamos el header
Con -d especificamos los datos con los que se creara el usuario, es importante no dejar ningún dato incompleto ya que obtendremos un error de datos invalidos
---
---
# Casos De uso 3

## Como crear un reporte en la API utilizando CURL
Con esta función se plantea que los usuarios puedan reportar imagenes inapropiadas para tener un control con lo que se suba en la API y asi tambien los usuarios se sientan escuchados y que tenga algo de control en la API.

### Estructura del CURL
```
curl http://localhost:8081/imagebank/report \
-X POST \
-H 'Content-Type: application/json' \
-d '{"report_id":"007", "username":"jesc331", "status":"open", "message":"esta imagen es inapropiada", "image_id":"001"}'
```
Con -X especificamos el metodo
Con -H especificamos el header
Con -d especificamos los datos con los que se creara el reporte, es importante especificar el id de la imágen, además de adjuntar un mensaje hablando del porque se debe de borrar para que los administradores puedan dar una justificación al respecto en caso de que se borre la imagen o no.
---
# Casos De uso 4

## Como consultar todos los usuarios registrados en la API utilizando CURL
Con esta función se plantea que los administradores puedan obtener todos los usuarios registrados en la API, asi tambien en un futuro se plantea que se use esta funcion para que otros usuarios busquen a otros usuarios.

### Estructura del CURL
```
curl http://localhost:8081/imagebank/user/list -X GET

```
Con -X especificamos el metodo
Se especifica solo la ruta de "imagebank/user/list" la cual ejecutara una consulta sin parametros especificos y de esta manera devolvera todos los usuarios registrados.
---
# Casos De uso 5

## Como consultar a un usuario registrado con parametros especificos en la API utilizando CURL
Con esta función se plantea que podamos buscar a los usuarios con alguno de los siguientes parametros: 'user_id' o 'username'.

### Estructura del CURL
```
curl http://localhost:8081/imagebank/user/<user_id or username> -X GET

```
Con -X especificamos el metodo
Se especifica solo la ruta de "imagebank/user/ y despues algun user_id como por ejemplo "001" o un username como "jesc33", para obtener los datos de ese usuario en especifico.
---
---
# Casos De uso 6

## Como consultar una imagen en espcifico con distintos parametros
Con esta función se plantea que los administradores o usuarios puedan buscar imágenes con distintos parametros como: image_id, fecha o extensión del archivo esto para que podamos encontrar las imagenes que necesitemos especificamente.
Esto mismo se podrá utilizar para el buscador de imágenes cuando se tenga frontend.

### Estructura del CURL
```
curl http://localhost:8081/imagebank/image/pictures/<iamge_id or date or extension> -X GET

```
Con -X especificamos el metodo
Se especifica solo la ruta de "imagebank/image/pcitures y despues algun image_id como por ejemplo "001" o una fecha como "2021-08-02 o alguna extension de las permitidas como: jpg, jpeg, png o gif. Para obtener los datos de esa imagen  en especifico.
---
# Planeación del FrontEnd
Con esto se plantea llevar a cabo el desarrollo del frontend de nuestra API, para que tenga una vista más agradable con el usuario y se pueda utilizar sin problemas, pero antes de empezar con el desarrollo se tendrá que tomar en cuenta los siguientes puntos y que se cumplan sin omitir ninguno de ellos:
  
- El servidor debe poder procesar las consultas para GET, UPDATE, POST y DELETE de las siguientes variables dentro de la API: usuarios, reportes, imágenes y cometarios.
- Que el inicio de sesión de la página funcione correctamente además de que se asignes los permisos correspondientes.
- Que las validaciones para subir imágenes o archivos con formatos incorrectos estén funcionando para evitar archivos incorrectos en el servidor.
- Que las validaciones para que no haya usuarios duplicados estén funcionando correctamente.

Sin los puntos mencionados la API funcionará, pero no como se espera, lo cual generará errores y mantenimientos constantes a la aplicación lo cual sería un gasto innecesario de horas de trabajo, aclarado esto empezare a mencionar lo que se plantea desarrollar para este proyecto.
  
Se deberá crear una página web funcional con base de archivos HTML y Javascript, para poder utilizar las funciones que se ha desarrollado y que tenga conexión con nuestro servidor, asi mismo agregar estilo a la página web por medio de un lenguaje de diseño como CSS, esto es la base de nuestros frontend. 

---
  
**Para el login se plantea lo siguiente:**

Que se presenten dos campos de textos en los que vayan a escribirse las credenciales del usuario que son “usuario” y “contraseña”, y con un botón debajo para poder acceder en la API una vez escrita tu información, además de otro botón para “registrarse” si es que no tienes un usuario valido.
  
Se piensa que tenga los colores que contrasten con el logo que represente la API además de que el logo aparezca en la esquina inferior derecha junto con el nombre de la API, esto aún no está definido, pero es un detalle que se planea en un futuro.

<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/login_layout.png" width="480px">

---
**Para la página de inicio se plantea lo siguiente:**
  
Se plantea que se observen las imágenes de otros usuarios en el inicio como una especie de vista previa, y en la parte de arriba una barra de búsqueda, para hacer una búsqueda específica y arriba de la barra de búsqueda en el parte superior derecho un hipervínculo al perfil del usuario. Esta página debe de ser capaz de realizar consultas y ejecutar funciones para obtener imágenes específicas y subir nuevas imágenes.
  
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/home_layout.png" width="480px">
---
**Para la página de subir imágenes se plantea lo siguiente:**
  
Al momento de hacer clic en el botón de subir imágenes, que se presenta en el inicio de la API se abrirá esta página, donde podremos rellenar la información que se requiere para subir una imagen y en caso de que no se cumplan los requisitos, salte un error por parte del usuario, se plantea que se despliegue el explorador de archivos al momento que se trate de seleccionar la imagen específica y que se seleccionen las categorías.

<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/uploaded_layout.png" width="480px">
---
**Para la página de reportes:**

  Para poder acceder a este apartado primero deberá de hacer clic en el atajo del perfil que están en la página inicial, y ahí en la página del perfil podrás ver el botón de crear reportes, donde se podrá visualizar 3 cuadros de textos, una para escribir el usuario, el ID de la imagen y un reporte de retroalimentación y el botón de enviar en caso de que falte alguna información salte un error por parte del usuario, además el usuario podrá ver el estatus de otros reportes suyos en caso de que tenga otros más. 

 <img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/reports_layout.png" width="480px"> 
---
**Para la página de crear usuarios:**

Para crear un usuario en nuestra API tendremos que acceder primero a la página del login y hacer clic en el botón de registro y que te mandara  a una página donde encontraras tres campos de texto que se deberán de llenar correctamente y en caso de que falte alguna información salte un error, asi como si el usuario se repite con uno ya registrado se saltara un error y se le dará un menaje al usuario de que por favor cambie el usuario y por ultimo si la contraseña no cumple con ciertas reglas que salte otro error y dándole un mensaje al usuario de que mejore la seguridad de la contraseña.
  
<img src="https://github.com/Jesc331/storage-api/blob/master/storage/images_resources/login_register_layour.png" width="480px">
---
# Historial de Commits
# Solo para evaluación - Se pidio que se borrara
