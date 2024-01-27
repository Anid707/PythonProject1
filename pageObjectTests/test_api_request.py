#import pytest
import json

import requests

from models.category import Category
from models.pet import Pet
from models.tag import Tag


#import jsonpath

class TestPets:
    base_url = "https://petstore.swagger.io/v2"

    def endpoint_pet(self,id):
        return f"/pet/{id}"

    def get_url(self,id):
        return self.base_url + self.endpoint_pet(id)

    #GET
    def test_get_pet_by_id(self):
        response = requests.request("GET", self.get_url(1))
        assert response.status_code == 200

        print(response.text)

        json_response = json.loads(response.text)

        pet_name = json_response["name"]
        pet_id = json_response["id"]
        pet_category = json_response["category"]

        assert pet_name == "dog"
        assert pet_id == 1
        assert pet_category["name"] == "cat"

    #POST
    def test_post_create_a_pet(self):
        category = Category(2, "Dogs")
        tag = Tag(5, "Red")
        pet = Pet(777557, "available", "Bibbie", category.__dict__, ['string'], [tag.__dict__])
        body = json.dumps(pet.__dict__)
        headers = {'Content-Type': 'application/json'}

        response = requests.post(self.base_url + "/pet", headers=headers, data=body)

        assert response.status_code == 200
        json_response = json.loads(response.text)
        print(response.text)

        pet_name = json_response["name"]
        pet_id = json_response["id"]

        assert pet_name == "Bibbie"
        assert pet_id == 777557

        #Get after Post
        response = requests.request("GET", self.get_url(777557))
        assert response.status_code == 200

        json_response = json.loads(response.text)

        pet_name = json_response["name"]
        pet_id = json_response["id"]
        pet_category = json_response["category"]

        assert pet_name == "Bibbie"
        assert pet_id == 777557
        assert pet_category["name"] == "Dogs"

    # PUT
    def test_put_update_pet(self):
        category = Category(2, "dogs")
        tag = Tag(5, "Red")
        pet = Pet(777557, "available", "Rose", category.__dict__, ['string'], [tag.__dict__])
        body = json.dumps(pet.__dict__)
        headers = {'Content-Type': 'application/json'}

        response = requests.put(self.base_url + "/pet", headers=headers, data=body)
        #response = requests.request("PUT", self.get_url(777557), headers=headers, data=body)

        assert response.status_code == 200
        json_response = json.loads(response.text)
        print(response.text)

        pet_name = json_response["name"]
        pet_id = json_response["id"]

        assert pet_name == "Rose"
        assert pet_id == 777557

        # Get after Post
        response = requests.request("GET", self.get_url(777557))
        assert response.status_code == 200

        json_response = json.loads(response.text)

        pet_name = json_response["name"]
        pet_id = json_response["id"]
        pet_category = json_response["category"]

        assert pet_name == "Rose"
        assert pet_id == 777557
        assert pet_category["name"] == "dogs"

    # Delete
    def test_delete_pet_by_id(self):
        response = requests.request("DELETE", self.get_url(777556))
        assert response.status_code == 200

        response = requests.request("GET", self.get_url(777556))
        assert response.status_code == 404

        json_response = json.loads(response.text)
        print(response.text)
        assert json_response["code"] == 1
        assert json_response["type"] == "error"
        assert json_response["message"] == "Pet not found"


        








    #print(response) #<Response [200]>
    #print(type(response))

    # body = {
    #     "id": 1,
    #     "category": {
    #         "id": 1,
    #         "name": "string"
    #     },
    #     "name": "doggie",
    #     "photoUrls": [
    #         "string"
    #     ],
    #     "tags": [
    #         {
    #             "id": 1,
    #             "name": "string"
    #         }
    #     ],
    #     "status": "available"
    # }




