import requests
from Homework26.jsons import JsonsCollection


class TestConfigs:
    product_url = "https://api.restful-api.dev/objects"

    product_headers = {"content-type": "application/json"}

    def test_get(self):
        get_object_by_id = requests.get(
            f"{TestConfigs.product_url}/3", headers=TestConfigs.product_headers
        )
        cnvtr = get_object_by_id.json()
        assert get_object_by_id.status_code == 200
        assert cnvtr["id"] == "3"
        assert cnvtr["name"] == "Apple iPhone 12 Pro Max"
        assert cnvtr["data"]["color"] == "Cloudy White"
        assert cnvtr["data"]["capacity GB"] == 512

    def test_post(self):
        post_add_object = requests.post(
            TestConfigs.product_url,
            data=JsonsCollection.product_json,
            headers=TestConfigs.product_headers,
        )
        cnvtr = post_add_object.json()
        assert post_add_object.status_code == 200
        assert cnvtr["id"] is not None
        assert cnvtr["name"] == "Apple MacBook Pro 16"
        assert cnvtr["data"]["year"] == 2019
        assert cnvtr["data"]["price"] == 1849.99
        assert cnvtr["data"]["CPU model"] == "Intel Core i9"
        assert cnvtr["data"]["Hard disk size"] == "1 TB"
        assert cnvtr["createdAt"] is not None

    def test_put(self):
        post_add_object = requests.post(
            TestConfigs.product_url,
            data=JsonsCollection.product_json,
            headers=TestConfigs.product_headers,
        )
        a = post_add_object.json()["id"]
        put_update_par = requests.put(
            f"{TestConfigs.product_url}/{a}",
            data=JsonsCollection.product_for_update,
            headers=TestConfigs.product_headers,
        )
        cnvtr = put_update_par.json()
        assert put_update_par.status_code == 200
        assert cnvtr["id"] == a
        assert cnvtr["name"] == "Apple MacBook Pro 16"
        assert cnvtr["data"]["year"] == 2019
        assert cnvtr["data"]["price"] == 2049.99
        assert cnvtr["data"]["CPU model"] == "Intel Core i9"
        assert cnvtr["data"]["Hard disk size"] == "1 TB"
        assert cnvtr["data"]["color"] == "silver"

    def test_patch(self):
        post_add_object = requests.post(
            TestConfigs.product_url,
            data=JsonsCollection.product_json,
            headers=TestConfigs.product_headers,
        )
        a = post_add_object.json()["id"]
        patch_update_partially = requests.patch(
            f"{TestConfigs.product_url}/{a}",
            data=JsonsCollection.string_for_partial_updt,
            headers=TestConfigs.product_headers,
        )
        cnvtr = patch_update_partially.json()
        assert patch_update_partially.status_code == 200
        assert cnvtr.json()["id"] == a
        assert cnvtr.json()["name"] == "Apple MacBook Pro 16 (Updated Name)"
        assert cnvtr.json()["data"]["year"] == 2019
        assert cnvtr.json()["data"]["price"] == 1849.99
        assert cnvtr.json()["data"]["CPU model"] == "Intel Core i9"
        assert cnvtr.json()["data"]["Hard disk size"] == "1 TB"

    def test_delete(self):
        post_add_object = requests.post(
            TestConfigs.product_url,
            data=JsonsCollection.product_to_del,
            headers=TestConfigs.product_headers,
        )
        b = post_add_object.json()["id"]
        delete_object = requests.delete(
            f"{TestConfigs.product_url}/{b}", headers=TestConfigs.product_headers
        )
        cnvtr = delete_object.json()
        assert delete_object.status_code == 200
        assert cnvtr["message"] == f"Object with id = {b} has been deleted."
        get_deleted_object = requests.get(
            f"{TestConfigs.product_url}/{b}", headers=TestConfigs.product_headers
        )
        assert get_deleted_object.status_code == 404



