# from django.test import TestCase


def test_root_deve_retornar_200(client):
    response = client.get('/')  # Act
    assert response.status_code == 200  # Assert
