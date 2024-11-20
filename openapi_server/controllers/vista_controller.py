import connexion

from openapi_server.models.vista import Vistas  # noqa: E501

from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

import requests

db = SQLAlchemy()

def import_db_controller(database):
    global db
    db = database

def add_vista():  # noqa: E501
    """Crear una nueva vista

    Crea una nueva vista # noqa: E501

    :param vista: 
    :type vista: dict | bytes

    :rtype: Union[Vista, Tuple[Vista, int], Tuple[Vista, int, Dict[str, str]]
    """
    try:
    # Obtener los datos de la solicitud JSON
        data = connexion.request.get_json()
        if not data:
            return {"error": "No data provided"}, 400  # Código 400: No se proporcionaron datos
    
    # Verificar que todos los campos requeridos están presentes
        required_fields = ['nombre', 'contenidos_ids']
        for field in required_fields:
            if field not in data:
                return {"error": f"Missing field: {field}"}, 422  # Código 422: Falta un campo requerido

        # Asignar los valores de los campos
        nombre = data['nombre']
        contenidos = data['contenidos_ids']

        # Crear el nuevo contenido
        new_vista = Vistas(
            nombre_vista=nombre, 
            contenidos_ids=contenidos
            )

    # Guardar el contenido en la base de datos
        db.session.add(new_vista)
        db.session.commit()

    # Retornar el contenido creado como diccionario
        return new_vista.to_dict(), 200  # Código 200: Contenido creado exitosamente

    except Exception as e:
    # En caso de error, retornar un mensaje con detalles
        return {"error": f"An error occurred: {str(e)}"}, 500  # Código 500: Error del servidor


def delete_vista(id_vista):  # noqa: E501
    """Eliminar una vista específica por su id

    Elimina una vista del sistema segun su identificador # noqa: E501

    :param id_vista: Id de la vista que se va a eliminar
    :type id_vista: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    try:
        id_vista = int(id_vista)
        
        vista = db.session.query(Vistas).get(id_vista)
        
        if vista is None:
            return jsonify({'error': 'Vista no encontrada'}), 404

        db.session.expunge(vista)
        
        db.session.delete(vista)
        db.session.commit()

        return jsonify({'message': 'vista eliminada correctamente'}), 200


    except ValueError:
        # Devolver un error 400 si el ID proporcionado no es un número entero
        return jsonify({'error': 'ID inválido, debe ser un número entero'}), 400

    except Exception as e:
        # Capturar cualquier otro error y devolver un error 500 con detalles adicionales
        return jsonify({'error': f'Error en el servidor: {str(e)}'}), 500


def delete_vista_by_nombre(nombre_vista):  # noqa: E501
    """Eliminar una vista específica por su nombre

    Elimina una vista del sistema segun su nombre # noqa: E501

    :param nombre_vista: nombre de la vista que se va a eliminar
    :type nombre_vista: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    try:        
        vista = db.session.query(Vistas).filter_by(nombre_vista=nombre_vista).first()
        
        if vista is None:
            return jsonify({'error': 'Vista no encontrada'}), 404

        db.session.expunge(vista)
        
        db.session.delete(vista)
        db.session.commit()

        return jsonify({'message': 'vista eliminada correctamente'}), 200

    except Exception as e:
        # Capturar cualquier otro error y devolver un error 500 con detalles adicionales
        return jsonify({'error': f'Error en el servidor: {str(e)}'}), 500


def get_all_vista():  # noqa: E501
    """Obtener el catalogo de las todas las listas de contenido de la aplicacion

    Retorna todas las listas de contenidos # noqa: E501


    :rtype: Union[List[Vista], Tuple[List[Vista], int], Tuple[List[Vista], int, Dict[str, str]]
    """
    vistas = Vistas.query.all()
    vistas_con_contenidos = []
    for vista in vistas:
        contenidos = []
        for id in vista.contenidos_ids:
            url = f'http://127.0.0.1:8080/contenido/{id}'
            response = requests.get(url)
            if response.status_code == 200:
                contenidos.append(response.json())
            else:
                print(f"Error al recuperar el contenido con id {id}: {response.status_code}")
        vistas_dict = {
            "id_vista": vista.id_vista,
            "nombre_vista": vista.nombre_vista,
            "contenidos_ids": vista.contenidos_ids,
            "contenidos": contenidos
        }
        vistas_con_contenidos.append(vistas_dict)

    return vistas_con_contenidos


def get_contenidos_vista(id_vista):  # noqa: E501
    """Obtener el listado de contenidos multimedia de la vista

    Retorna el conjunto de contenidos multimedia favoritos de la vista en función de su identificador # noqa: E501

    :param id_vista: Id de la vista que se quiere recuperar
    :type id_vista: int

    :rtype: Union[List[Contenido], Tuple[List[Contenido], int], Tuple[List[Contenido], int, Dict[str, str]]
    """
    vista = Vistas.query.get_or_404(id_vista)
    contenidos = []
    for id in vista.contenidos_ids:
        url = f'http://127.0.0.1:8080/contenido/{id}'
        response = requests.get(url)
        if response.status_code == 200:
            contenidos.append(response.json())
        else:
            print(f"Error al recuperar el contenido con id {id}: {response.status_code}")

    return contenidos


def get_vista_by_id(id_vista):  # noqa: E501
    """Obtener una vista específica por su id

    Retorna una vista en concreto recibiendo como input su id # noqa: E501

    :param id_vista: Id de la vista que se quiere recuperar
    :type id_vista: int

    :rtype: Union[Vista, Tuple[Vista, int], Tuple[Vista, int, Dict[str, str]]
    """
    vista = Vistas.query.get_or_404(id_vista)
    vistas_dict = {
        "id_vista": vista.id_vista,
        "nombre_vista": vista.nombre_vista,
        "contenidos_ids": vista.contenidos_ids,
        "contenidos": get_contenidos_vista(id_vista)
    }

    return vistas_dict    


def get_vista_by_nombre(nombre_vista):  # noqa: E501
    """Obtener una vista específica por su nombre

    Retorna una vista en concreto recibiendo como input su nombre # noqa: E501

    :param nombre_vista: nombre de la vista que se va a recuperar
    :type nombre_vista: str

    :rtype: Union[Vista, Tuple[Vista, int], Tuple[Vista, int, Dict[str, str]]
    """
    vista = Vistas.query.filter_by(nombre_vista=nombre_vista).first()
    vistas_dict = {
        "id_vista": vista.id_vista,
        "nombre_vista": vista.nombre_vista,
        "contenidos_ids": vista.contenidos_ids,
        "contenidos": get_contenidos_vista(vista.id_vista)
    }

    return vistas_dict


def update_vista_by_nombre(nombre_vista):  # noqa: E501
    """Actualizar una vista específica por su nombre

    Actualiza una vista en el sistema # noqa: E501

    :param nombre_vista: nombre de la vista que se va a actualizar
    :type nombre_vista: str

    :rtype: Union[Vista, Tuple[Vista, int], Tuple[Vista, int, Dict[str, str]]
    """
    try:
        # Obtener los datos de la solicitud JSON
        data = connexion.request.get_json()
        if not data:
            return {"error": "No data provided"}, 400  # Código 400: No se proporcionaron datos

        vista = db.session.query(Vistas).filter_by(nombre_vista=nombre_vista).first()

        if 'nombre_vista' in data:
            vista.nombre_vista = data['nombre_vista']
        if 'contenidos_ids' in data:
            vista.contenidos_ids = data['contenidos_ids']

        db.session.commit()

        return vista.to_dict(), 200

    except Exception as e:
        # Otro tipo de error
        return {"error": f"An error occurred: {str(e)}"}, 500  # Código 500: Error del servidor



def updatevista(id_vista):  # noqa: E501
    """Actualizar una vista específica por su identificador

    Actualiza una vista en el sistema # noqa: E501

    :param id_vista: Id de la vista que se va a actualizar
    :type id_vista: int

    :rtype: Union[Vista, Tuple[Vista, int], Tuple[Vista, int, Dict[str, str]]
    """
    try:
        # Obtener los datos de la solicitud JSON
        data = connexion.request.get_json()
        if not data:
            return {"error": "No data provided"}, 400  # Código 400: No se proporcionaron datos

        vista = db.session.query(Vistas).get(id_vista)

        if 'nombre_vista' in data:
            vista.nombre_vista = data['nombre_vista']
        if 'contenidos_ids' in data:
            vista.contenidos_ids = data['contenidos_ids']
            
    
        db.session.commit()

        return vista.to_dict(), 200

    except Exception as e:
        # Otro tipo de error
        return {"error": f"An error occurred: {str(e)}"}, 500  # Código 500: Error del servidor
