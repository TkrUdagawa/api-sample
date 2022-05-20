from fastapi.testclient import TestClient

from apisample.main import app


client = TestClient(app)


def test_post_csv():
    upload_file = [("upload_file", open("./tests/data/sample1.csv", "rb"))]
    response = client.post(
        "/api/v1/files",
        files=upload_file)
    assert response.json()["message"] == "ok"