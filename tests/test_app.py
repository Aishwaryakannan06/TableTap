
import app as tabletap_app


def test_homepage_loads():
    client = tabletap_app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_empty_order_is_rejected():
    client = tabletap_app.app.test_client()
    response = client.post(
        "/api/orders",
        json={"items": []}
    )
    assert response.status_code == 400


def test_valid_order_is_created(tmp_path, monkeypatch):
    monkeypatch.setattr(
        tabletap_app, "DATABASE",
        str(tmp_path / "test.db")
    )
    tabletap_app.create_database()

    client = tabletap_app.app.test_client()
    response = client.post(
        "/api/orders",
        json={
            "items": [
                {"name": "Burger", "quantity": 2, "price": 100}
            ]
        }
    )

    assert response.status_code == 201
    assert response.json["total"] == 200
