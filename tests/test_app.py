from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_retorna_ok_e_ola_mundo():
    client = TestClient(app)
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_root_retorna_ola_mundo_html():
    client = TestClient(app)
    response = client.get('/hello')

    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """
    <html>
      <head><title>Hello HTML</title></head>
      <body><p>Olá Mundo!</p></body>
    </html>"""
    )
