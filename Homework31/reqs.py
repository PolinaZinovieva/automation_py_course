import requests
import json
class TestRequests:
    product_url = "https://api.restful-api.dev/objects"

    product_headers = {"content-type": "application/json"}
    product_json = json.dumps({
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    })


    def test_post(self):
        post_add_object = requests.post(
            TestRequests.product_url,
            data=TestRequests.product_json,
            headers=TestRequests.product_headers,
            )
        a = post_add_object.json()["id"]
        get_obj = requests.get(f"{TestRequests.product_url}/{a}",headers=TestRequests.product_headers)


        self.cnvtr = get_obj.json()
        self.cnvtr2 = post_add_object.json()
        self.id_var = self.cnvtr["id"]
        self.name_var = self.cnvtr["name"]
        self.year_var = self.cnvtr["data"]["year"]
        self.price_var = self.cnvtr["data"]["price"]
        self.cpu_var = self.cnvtr["data"]["CPU model"]
        self.hard_var = self.cnvtr["data"]["Hard disk size"]
        assert get_obj.status_code == 200
        assert self.cnvtr["id"] == a
        assert self.cnvtr["name"] == self.cnvtr2["name"]
        assert self.cnvtr["data"]["year"] == self.cnvtr2["data"]["year"]
        assert self.cnvtr["data"]["price"] == self.cnvtr2["data"]["price"]
        assert self.cnvtr["data"]["CPU model"] == self.cnvtr2["data"]["CPU model"]
        assert self.cnvtr["data"]["Hard disk size"] == self.cnvtr2["data"]["Hard disk size"]
TestRequests().test_post()










