import unittest

from flask import json

from openapi_server.models.contenido import Contenido  # noqa: E501
from openapi_server.models.vista import Vista  # noqa: E501
from openapi_server.test import BaseTestCase


class TestVistaController(BaseTestCase):
    """VistaController integration test stubs"""

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_add_vista(self):
        """Test case for add_vista

        Crear una nueva vista
        """
        vista = {"listaContenidos":[0,0],"idVista":10,"nombreVista":"tipoContenido"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/vista',
            method='POST',
            headers=headers,
            data=json.dumps(vista),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_vista(self):
        """Test case for delete_vista

        Eliminar una vista específica por su id
        """
        headers = { 
        }
        response = self.client.open(
            '/vista/{id_vista}'.format(id_vista=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_vista_by_nombre(self):
        """Test case for delete_vista_by_nombre

        Eliminar una vista específica por su nombre
        """
        headers = { 
        }
        response = self.client.open(
            '/vista/{nombre_vista}'.format(nombre_vista='nombre_vista_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_vista(self):
        """Test case for get_all_vista

        Obtener el catalogo de las todas las listas de contenido de la aplicacion
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/vista',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_contenidos_vista(self):
        """Test case for get_contenidos_vista

        Obtener el listado de contenidos multimedia de la vista
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/vista/{id_vista}/contenidos'.format(id_vista=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_vista_by_id(self):
        """Test case for get_vista_by_id

        Obtener una vista específica por su id
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/vista/{id_vista}'.format(id_vista=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_vista_by_nombre(self):
        """Test case for get_vista_by_nombre

        Obtener una vista específica por su nombre
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/vista/{nombre_vista}'.format(nombre_vista='nombre_vista_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_vista_by_nombre(self):
        """Test case for update_vista_by_nombre

        Actualizar una vista específica por su nombre
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/vista/{nombre_vista}'.format(nombre_vista='nombre_vista_example'),
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_updatevista(self):
        """Test case for updatevista

        Actualizar una vista específica por su identificador
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/vista/{id_vista}'.format(id_vista=56),
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
