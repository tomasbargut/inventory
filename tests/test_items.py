def test_item_list(client):
    response = client.get('/api/item/')
    assert response.status_code == 200

def test_item_create(client, ):
    payload = {
        "name": "Item loco",
        "desc": "Este es un item muy loco"
    }
    response = client.post('/api/item/', json=payload)
    assert response.status_code == 201
    json_response = response.json()
    assert "id" in json_response
    assert all(item in response.items() for item in payload.items())