# Api Vistas 

<img width="518" alt="image" src="https://github.com/user-attachments/assets/8cb3f829-8818-45ee-a18c-9e0c3b8c6ff5">



## Descripción General

Esta API está diseñada para gestionar las vistas de contenido en una aplicación de streaming similar a Netflix. Las vistas son colecciones de contenidos multimedia organizadas según ciertos criterios o filtros, como géneros, tipos de contenido o preferencias del usuario. El propósito principal de esta API es permitir la gestión eficiente de estas colecciones o listas de contenidos, tanto para los usuarios finales como para los administradores del sistema.}

## Endpoints de la API


- **Obtener lista de vistas**  
  `GET /vista`: Recupera todas las vistas disponibles en el sistema.

- **Crear una nueva vista**  
  `POST /vista`: Crea una nueva vista en el sistema.

- **Obtener vista por ID**  
  `GET /vista/{idVista}`: Obtiene los detalles de una vista específica mediante su ID.

- **Actualizar vista**  
  `PUT /vista/{idVista}`: Actualiza la información de una vista existente usando su ID.

- **Eliminar vista por ID**  
  `DELETE /vista/{idVista}`: Elimina una vista del sistema mediante su ID.

- **Obtener contenidos de una vista**  
  `GET /vista/{idVista}/contenidos`: Recupera los contenidos multimedia asociados a una vista específica.

- **Obtener vista por nombre**  
  `GET /vista/{nombreVista}`: Obtiene los detalles de una vista mediante su nombre.

- **Eliminar vista por nombre**  
  `DELETE /vista/{nombreVista}`: Elimina una vista del sistema utilizando su nombre.

- **Actualizar vista por nombre**  
  `PUT /vista/{nombreVista}`: Actualiza la vista especificada por su nombre.


## Tecnologías y Herramientas Usadas:

- Se utilizó **PostgreSQL** como base de datos SQL para almacenar y gestionar los datos de la API.

- **Postman** se utilizó para realizar pruebas de los endpoints de la API, asegurando que todas las solicitudes y respuestas fueran correctas.

- **GitHub Actions** se configuró para automatizar el proceso de integración continua, ejecutando pruebas y despliegues cada vez que se realizaba un push al repositorio.

- **Swagger** se usó para definir la arquitectura de la API, incluyendo los endpoints del microservicio. Esto proporcionó una documentación interactiva y permitió probar la API directamente desde la interfaz.

- **OpenAPI Generator** se empleó para generar el esqueleto del código de la API, lo que permitió comenzar rápidamente con una estructura base para los endpoints definidos en el archivo Swagger.

- El desarrollo se realizó en **Python**, utilizando el framework **Flask** para construir la API. Flask es ligero, fácil de usar y perfecto para construir microservicios.

- **Docker** se utilizó para crear contenedores tanto para la API como para la base de datos, permitiendo simular un entorno de despliegue real. Esto garantizó que la API funcionara correctamente tanto en desarrollo como en pruebas, aislando el entorno de ejecución.

- Se utilizó una **arquitectura modular**, separando el código en diferentes paquetes y clases. Esto permitió un orden claro y mantenible en el código. La separación en paquetes facilita el desarrollo y la extensión del sistema sin que otras partes se vean afectadas, favoreciendo la escalabilidad del proyecto.

- Se utilizaron las siguientes librerías:

    Flask-SQLAlchem: Para la integración con la base de datos PostgreSQL, gestionando las operaciones CRUD.

    Flask-CORS: Para habilitar el soporte de CORS, permitiendo que la API sea accesible desde diferentes dominios.


## Requisitos de la API
Python 3.5.2+

## Guía de Uso En el Directorio

### Despliegue en Directorio 

1. Instalación:
 * Asegúrate de tener Python 3.5.2 o superior instalado en tu máquina.

2. Configuración del entorno
 * Asegúrate de tener PostgreSQL corriendo y configurado en tu entorno local o usa un servicio en la nube .
<<<<<<< HEAD
 * Nombra tu base de datos como Contenidos 
=======
 * Nombra tu base de datos como Vistas
>>>>>>> b3eb0104767d52429b438f9fdbd1d44a12f77d92
 * Para inicializar las tablas la base de datos y el contenido de esta, asegúrate de ejecutar las query definidas en el archivo Init.sql para crear las tablas y estructuras necesaria

3. Para ejecutar la Api Contenidos , ejecute lo siguiente desde el directorio raíz
 * Instale los requerimientos 
    ```
    pip3 install -r requirements.txt
    pip3 install -r requeriments_sqlalchemy.txt
    ```
 * Ejecute la Api con el siguiente Comando
    ```
    python3 -m openapi_server
    ```
 * La Api debe estarse  ejecutando 

4. Definición de OpenAPI

Abre tu navegador y accede a la siguiente URL para ver la interfaz de usuario de la API:
```
http://localhost:8080/ui/
```

La definición de OpenAPI está disponible en formato JSON en:
```
http://localhost:8080/openapi.json
```

## Despliegue en Docker 
<<<<<<< HEAD
=======

Este documento describe los pasos necesarios para desplegar una API dentro de un contenedor Docker utilizando `docker-compose`.

---

### Requisitos previos

1. **Docker**: Asegúrate de tener instalado Docker en tu sistema. Puedes descargarlo desde [Docker](https://www.docker.com/).
2. **docker-compose**: Comprueba que tienes instalado `docker-compose`. Si no, sigue las instrucciones de instalación [aquí](https://docs.docker.com/compose/install/).

---

### Pasos para el despliegue

### Paso 1: Crear una red en Docker

Antes de desplegar la API, necesitas crear una red específica para el proyecto. Esto permitirá que los contenedores se comuniquen entre sí.

Ejecuta el siguiente comando en la terminal:
>>>>>>> b3eb0104767d52429b438f9fdbd1d44a12f77d92

Para desplegar la API en un contenedor Docker , Ejecute el siguiente comando 
```bash
<<<<<<< HEAD
# Construir e iniciar la imagen y el contenedor
docker-compose up --build
=======
docker network create flask_network
```

### Paso 2: Construir e iniciar la API

Para construir la imagen de Docker y poner en marcha los contenedores, sigue los pasos a continuación:

Desde el directorio donde se encuentra el archivo `docker-compose.yml`, ejecuta el siguiente comando para construir las imágenes y levantar los contenedores:

```bash
docker-compose up --build
```

### Paso 3. Verificar el despliegue
Una vez que los contenedores estén en funcionamiento, puedes verificar el estado de los servicios con el siguiente comando:

```bash
docker ps
```

## ¡Todo listo! 🚀

Tu API ahora está en funcionamiento dentro de un contenedor Docker, junto con su base de datos y otros servicios asociados.

>>>>>>> b3eb0104767d52429b438f9fdbd1d44a12f77d92
