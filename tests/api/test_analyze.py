import json

from fastapi.testclient import TestClient

from apisample.main import app
from apisample.api.types import AnalyzeTask, ClassifierMethod


client = TestClient(app)


def test_post_analyze():
    param = {
        "task": AnalyzeTask.classify.value, 
        "method": ClassifierMethod.svm.value
    }
    response = client.post(
        "/api/v1/analyze/test1",
        data=json.dumps(param))
        
    print(response.json())
    assert response.json()["message"] == "ok"