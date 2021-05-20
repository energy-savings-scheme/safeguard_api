import json
import unittest

from server import server


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = server.test_client()

    def test_get(self):
        """ The GET on `/user` should return an user """
        response = self.client.get("/user/Doe/John")

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response_json, {"foo": "bar"})

    def test_create(self):
        """ The POST on `/user` should create an user """
        response = self.client.post(
            "/user/Doe/John",
            content_type="application/json",
            data=json.dumps({"age": 30}),
        )

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response_json, {"foo": "bar"})

    def test_update(self):
        """ The PUT on `/user` should update an user's age """
        response = self.client.put(
            "/user/Doe/John",
            content_type="application/json",
            data=json.dumps({"age": 30}),
        )

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response_json, {"foo": "bar"})
