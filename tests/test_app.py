from http import HTTPStatus


def test_root_retorna_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_root_retorna_ola_mundo_html(client):
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


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'melancia',
            'email': 'melancia@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'melancia',
        'email': 'melancia@example.com',
        'id': 1,
    }
