from fastapi.testclient import TestClient
from fastapi import status
from main import app
from users.models import User

client = TestClient(app=app)


def test_get_products():
    user_id_admin = 1
    new_user = {
        'id': 2,
        'email': "joseneira87@hotmail.com"
    }
    new_product = {
        'sku': "REF001",
        'name': "Refrigerator",
        'price': 870,
        'brand': "Indurama",
        'consulted': 0
    }
    update_product = {
        'sku': "REF001",
        'name': "Refrigerator",
        'price': 870.65,
        'brand': "Indurama RF",
        'consulted': 0
    }

    # Create new user
    response = client.post(f"/users/{user_id_admin}", json=new_user)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert len(data['detail']) == 2

    # Generate new product by new user
    response = client.post(f"/products/{new_user['id']}", json=new_product)
    assert response.status_code == status.HTTP_201_CREATED

    # Update product
    response = client.put(f"/products/{new_product['sku']}/{new_user['id']}", json=update_product)
    assert response.status_code == status.HTTP_200_OK
    # Send email to administrators
    data = response.json()
    assert data['detail']['price'] == update_product['price']

    # Consulting products
    response = client.get(f"/products/{new_user['id']}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data['detail']) == 1
