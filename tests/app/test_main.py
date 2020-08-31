import re
from typing import Dict, List

import pytest  # type: ignore
from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.applications import Starlette


class TestCors:
    """Test CORS middleware integration.
    ---
    - https://fastapi.tiangolo.com/tutorial/cors/
    - FastAPI/tests/test_tutorial/test_cors/test_tutorial001.py
    - Starlette/tests/middleware/test_cors.py
    """

    # Replace uris["good"] with one of your CORS approved origins.
    uris: Dict[str, str] = {
        "good": "https://br3ndon.land",
        "bad": "https://othersite.com",
    }

    def test_cors_preflight(self, clients: List[TestClient]) -> None:
        """Test pre-flight response."""
        headers: Dict[str, str] = {
            "Origin": self.uris["good"],
            "Access-Control-Request-Method": "GET",
            "Access-Control-Request-Headers": "X-Example",
        }
        for client in clients:
            response = client.options("/", headers=headers)
            assert response.status_code == 200, response.text
            assert response.text == "OK"
            assert response.headers["access-control-allow-origin"] == self.uris["good"]
            assert response.headers["access-control-allow-headers"] == "X-Example"

    @pytest.mark.xfail(reason="CORS disallowed origin")
    def test_cors_preflight_error(self, clients: List[TestClient]) -> None:
        """Test pre-flight response to disallowed origin."""
        headers: Dict[str, str] = {
            "Origin": self.uris["bad"],
            "Access-Control-Request-Method": "GET",
            "Access-Control-Request-Headers": "X-Example",
        }
        for client in clients:
            response = client.options("/", headers=headers)
            assert response.status_code == 200, response.text
            assert response.text == "OK"
            assert response.headers["access-control-allow-origin"] == self.uris["bad"]
            assert response.headers["access-control-allow-headers"] == "X-Example"

    def test_cors_standard(self, clients: List[TestClient]) -> None:
        """Test standard response."""
        headers = {"Origin": self.uris["good"]}
        for client in clients:
            response = client.get("/", headers=headers)
            assert response.status_code == 200, response.text
            assert response.json() == {"Hello": "World"}
            assert response.headers["access-control-allow-origin"] == self.uris["good"]

    def test_non_cors(self, clients: List[TestClient]) -> None:
        """Test non-CORS response."""
        for client in clients:
            response = client.get("/")
            assert response.status_code == 200, response.text
            assert response.json() == {"Hello": "World"}
            assert "access-control-allow-origin" not in response.headers


class TestEndpoints:
    """Test API endpoints
    ---
    - https://fastapi.tiangolo.com/tutorial/testing/
    - https://www.starlette.io/testclient/
    - https://docs.pytest.org/en/latest/parametrize.html
    """

    def test_get_root(self, clients: List[TestClient]) -> None:
        """Test a `GET` request to the root endpoint."""
        for client in clients:
            response = client.get("/")
            assert response.status_code == 200
            assert response.json() == {"Hello": "World"}

    @pytest.mark.parametrize("endpoint", ["/health", "/status"])
    def test_gets_with_basic_auth(
        self, basic_auth: tuple, clients: List[TestClient], endpoint: str
    ) -> None:
        """Test a `GET` request to endpoints that require HTTP Basic Auth."""
        for client in clients:
            assert client.get(endpoint).status_code in [401, 403]
            response = client.get(endpoint, auth=basic_auth)
            assert response.status_code == 200
            assert "application" in response.json().keys()
            assert "status" in response.json().keys()
            assert response.json()["application"] == "inboard"
            assert response.json()["status"] == "active"

    def test_get_status_message(
        self,
        basic_auth: tuple,
        clients: List[TestClient],
        endpoint: str = "/status",
    ) -> None:
        """Test the message returned by a `GET` request to a status endpoint."""
        for client in clients:
            assert client.get(endpoint).status_code in [401, 403]
            response = client.get(endpoint, auth=basic_auth)
            assert response.status_code == 200
            assert "message" in response.json().keys()
            assert "Hello World, from Uvicorn" in response.json()["message"]
            assert [
                word in re.split(r"[!?',;.\s]+", response.json()["message"])
                for word in ["Hello", "World", "Uvicorn", "Python"]
            ]
            if isinstance(client.app, FastAPI):
                assert "FastAPI" in response.json()["message"]
            elif isinstance(client.app, Starlette):
                assert "Starlette" in response.json()["message"]

    def test_get_user(
        self,
        basic_auth: tuple,
        clients: List[TestClient],
        endpoint: str = "/users/me",
    ) -> None:
        """Test a `GET` request to an endpoint providing user information."""
        for client in clients:
            assert client.get(endpoint).status_code in [401, 403]
            response = client.get(endpoint, auth=basic_auth)
            assert response.status_code == 200
            assert "application" not in response.json().keys()
            assert "status" not in response.json().keys()
            assert response.json()["username"] == "test_username"
