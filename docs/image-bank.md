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

# Casos De uso


---
# Historial de Commits
# Solo para evaluación
| Hash                                       | Fecha        | Descripción                            |
|--------------------------------------------|--------------|----------------------------------------|
| acf10d461c05b4fbe37dd275050386d93d9c9804   | Jun 28, 2021 | Se agregó la descripción del proyecto. |
| 152be431f1969780b0bc749f90b34e78c1e87f5c   | Jun 28, 2021 | Se agregó la primera descripción acerca del modo de  uso de la API.|
| 347bcb37533bddd9c52f0cef5c2c9b129cbc0ffb   | Jun 28, 2021 | Se agregó la primera descripción acerca de como iniciar sesion en la API |
| 07f1450e38d507ca06c7a692f7fd9ff032e250d9   | Jun 28, 2021 | Se agregaron mas detalles en la descripcion acerca de como iniciar sesion en la API |
| db1e012f0480be0f7a1bff9543e77f177d7cb5b3   | Jun 29, 2021 | Se corrigieron detalles en la descripción del inicio de sesión en la API |
| c15cab512f8577f680e6fa8d7e0907c1ad41f44e   | Jun 28, 2021 | Se agregó la descripción de que archivos se verían involucrados en el inicio de sesión |         
| c15cab512f8577f680e6fa8d7e0907c1ad41f44e   | Jun 28, 2021 | Se corrigieron detalles estéticos en archivo 'image-bank.md' |
| 2c4ab74aeed2ace15f87bfda73fae564349dc94b   | Jun 28, 2021 | Se corrigieron más detalles estéticos            |
| 649fcbe788a4bd71da5ef819f29e749b2edf5bfd   | Jun 28, 2021 | Solo corrección en detalles estéticos |
| 2f464930c6e449b0bba0a9fccd0e14637a5aebed   | Jun 29, 2021 | Se agregó descripción de la estructura deseada(solo de forma textual).|
| 96b17a3c2fcb37deef00e6267ca94bd81edaa148   | Jun 29, 2021 | Solo se corrigieron algunos errores en el texto. |
| 5c2653c3aefd9f7ca33221aded696b69c45afc0b   | Jun 28, 2021 | Se modificaron los archivos que se utilizan en la API para tener relación con la estructura deseada. |
| 1d06e9d7c5e984198766894a9889e2ef1d64f2ce   | Jun 29, 2021 | Se corrigieron detalles en las acciones dentro de la API |
| 8bd63e34199a32bf7d6b5724d03c93e0d2f3bc28   | Jun 29, 2021 | Se agregó la descripción del proceso "como borrar una imagen dentro de la API" |         
| f5d117d1cc64b7b31f33a53dd78340f9089dadc7   | Jun 29, 2021 | Se corrigieron detalles estéticos en archivo 'image-bank.md' |
| 3c6affb55c27c1147596b4eb5a9f51f067189937   | Jul 01, 2021 | Se agregó la descripción de las acciones que se pueden realizar siendo administrador o usuario |
| a8dd434d4cb380090a7ecf6104e3c4c42a524169   | Jul 01, 2021 | Se corrigió la descripción de las acciones que puede hacer el usuario en la API|         
| c107384531a102588fa10c069f2250f157a07d46   | Jul 01, 2021 | Se modificaron y se añadieron nuevas entidades que se necesitarán en la API |
| 157cb9388b79239a93d860970379be31094a90cd   | Jul 05, 2021 | Se añadió un ejemplo de aplicación de la API            |
| d29f7422a972758997a7184be3703eab81900499   | Jul 06, 2021 | Se añadió la descripción de las relaciones en la base de datos |
| 2fe9222ce0851adc39d74343184dec490c303c26   | Jul 06, 2021 | Se añadió una carpeta con imágenes necesarias para 'image-bank.md'|
| efa9a327e513ff396e46265bddcf3a1454cc01d9   | Jul 06, 2021 | Se añadió un diagrama entidad relación |
| 2b67b2b83d531a6a119b46046943ab93f36ab664   | Jul 06, 2021 | Cambios en el diseño al diagrama |
| 1d06e9d7c5e984198766894a9889e2ef1d64f2ce   | Jul 06, 2021 | Cambios al diseño del diagrama v2 |
| ab357d60f6d503860230d1102026887979fda5a8   | Jul 06, 2021 | Se añadió las consultas hacia los datos |         
| a008dec7fc6c4dbe9b8bb503bdbbfa3d7b300d8e   | Jul 06, 2021 | Permisos y acciones CRUD |
| e189a4a61d954d524c9056ef16b3ef8b2c9e8c78   | Jul 06, 2021 | Permisos y acciones CRUD v2 |
| 1d06e9d7c5e984198766894a9889e2ef1d64f2ce   | Jun 29, 2021 | Se corrigieron detalles en las acciones dentro de la API |
| 8bd63e34199a32bf7d6b5724d03c93e0d2f3bc28   | Jun 29, 2021 | Se agregó la descripción del proceso "como borrar una imagen dentro de la API" |         
| f5d117d1cc64b7b31f33a53dd78340f9089dadc7   | Jun 29, 2021 | Se corrigieron detalles estéticos en archivo 'image-bank.md' |
| 3c6affb55c27c1147596b4eb5a9f51f067189937   | Jul 01, 2021 | Se agregó la descripción de las acciones que se pueden realizar siendo administrador o usuario |
| 03e854fec44a439e6cd1a06f1a538fa0ac82d3bd   | Jul 07, 2021 | Acciones que se pueden realizar en la API y permisos necesarios|         
| c02b0d90969e131db1267c77e7b98fc45eb9d71b   | Jul 07, 2021 | Procesos dentro de la API |
| 98cc2a1e174f8a65f0ad2b9bc5d35478fc6d75df   | Jul 07, 2021 | Se añadió una imagen con un diagrama de rutas |
| 108f452ba02183b0b8e51382f53874ab9a89a096   | Jul 07, 2021 | Se añadió un comentario de ruta relativo y una imagen al respecto |
| 539e5fa32aabd76ca19a5adcf58ea701e55329d8   | Jul 07, 2021 | Estructura de solicitud y respuesta |
| 7b9876d349cf0448ee695248ed649efedfa22c54   | Jul 07, 2021 | Actualización de la descripción del apartado "Modo de Uso" |
| df8bc6a4fd3183770d4699f50b9ee2b19591c270   | Jul 07, 2021 | Se añadió la implementación de rutas para los recursos |
| d543e067aae48e4007da3ebf1de293517262b056   | Jul 08, 2021 | Se añadieron moqups acerca del aspecto visual de la API |
| 832649d58cc5b57594d7a9f742fef9830db52ea2   | Jul 08, 2021 | Se añadieron moqups acerca del aspecto visual de la API v2 |         
| d96a4d3c20c7209ff3a3278eadb9b3c9f68cf1ab   | Jul 08, 2021 | Se añadió el diseño relativo de user storage y login |
| 1524f70ba97fffe7e3c738c1530340da9adf73e1   | Jul 08, 2021 | Se añadió el diseño relativo de user storage y login v2 |
| 9883eb307fffabaddb5164e79c8396d7758f7901   | Jul 08, 2021 | Se añadió el diseño relativo de user storage y login v3 |
| d0d826f198c1bacec915982be5f019b7d95cf31b   | Jul 08, 2021 | Prueba de Error|         
| 1886e7c1e9fd06311f67357a5588540e4a53cd70   | Jul 08, 2021 | Diseños moqups Login y Register |
| ff371fc1787516a9e61be30bffac4082a2b263bc   | Jul 08, 2021 | Modificaciones de diseño a los moqups de Login y User Storage |
| 0548bca34f086820892f1efe81622b0d9e73266d   | Jul 08, 2021 | Se añadieron los maqups de home |
| 80c9c3ad15127f739689208adc67cfadaa1b92fb   | Jul 08, 2021 | Se añadió moqups del diseño de la subida de las imagenes |
| 8302cca963135c6859949ee6302a043f51f09ac2   | Jul 08, 2021 | Se añadió los moqups del perfil de usuario |
| 40f1e3079809cf9eea6944523e0c3d8deaff703c   | Jul 08, 2021 | Se añadieron los moqups para el layout de borrar imagenes y reportes |
