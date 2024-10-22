from http import HTTPStatus


def test_create_todo(client, token):
    response = client.post(
        '/todos',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'title': 'my test todo',
            'description': 'my test todo description',
            'state': 'draft',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'title': 'my test todo',
        'description': 'my test todo description',
        'state': 'draft',
    }
