import requests
import json
from Homework31.storage import Storage
class TestRequests(Storage):
    super().new_data()
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

    product_update = json.dumps({
        "name": "Iphone 12 pro max",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "256 GB"
        }
    })
    post_add_object = requests.post(product_url, data=product_json,headers=product_headers,
    )
    def test_post(self):

        a = TestRequests.post_add_object.json()["id"]
        get_obj = requests.get(f"{TestRequests.product_url}/{a}",headers=TestRequests.product_headers)


        self.cnvtr = get_obj.json()
        self.cnvtr2 = post_add_object.json()
        self.id_var = self.cnvtr["id"]
        self.name_var = self.cnvtr["name"]
        self.year_var = self.cnvtr["data"]["year"]
        self.price_var = int(self.cnvtr["data"]["price"])
        self.cpu_var = self.cnvtr["data"]["CPU model"]
        self.hard_var = self.cnvtr["data"]["Hard disk size"]
        assert get_obj.status_code == 200
        assert self.id_var == a
        assert self.name_var == self.cnvtr2["name"]
        assert self.year_var == self.cnvtr2["data"]["year"]
        assert self.cnvtr["data"]["price"] == self.cnvtr2["data"]["price"]
        assert self.cpu_var == self.cnvtr2["data"]["CPU model"]
        assert self.hard_var == self.cnvtr2["data"]["Hard disk size"]

    def put_update(self):
        a = TestRequests.post_add_object.json()["id"]
        put_update_object = requests.put(f"{TestRequests.product_url}/{a}",
                data=TestRequests.product_update,
                headers=TestRequests.product_headers,
                )
        b = put_update_object.json()["id"]
        get_obj2 = requests.get(f"{TestRequests.product_url}/{b}", headers=TestRequests.product_headers)
        self.cnvtr = get_obj2.json()
        self.cnvtr2 = put_update_object.json()
        self.id_var_n = self.cnvtr["id"]
        self.name_var_n = self.cnvtr["name"]
        self.year_var_n = self.cnvtr["data"]["year"]
        self.price_var_n = int(self.cnvtr["data"]["price"])
        self.cpu_var_n = self.cnvtr["data"]["CPU model"]
        self.hard_var_n = self.cnvtr["data"]["Hard disk size"]
        assert get_obj.status_code == 200
        assert self.id_var_n == b
        assert self.name_var_n == self.cnvtr2["name"]
        assert self.year_var_n == self.cnvtr2["data"]["year"]
        assert self.cnvtr["data"]["price"] == self.cnvtr2["data"]["price"]
        assert self.cpu_var_n == self.cnvtr2["data"]["CPU model"]
        assert self.hard_var_n == self.cnvtr2["data"]["Hard disk size"]


    def from_storage(self):

        Storage().new_data(name='airpods', price=2000, year=2022, name2=self.name_var_n)
        a = TestRequests.post_add_object.json()["id"]

        put_update2_object = requests.put(f"{TestRequests.product_url}/{a}",
                                             data=self.new_product,
                                             headers=TestRequests.product_headers,
                                             )
        c = put_update2_object.json()["id"]
        get_obj3 = requests.get(f"{TestRequests.product_url}/{c}", headers=TestRequests.product_headers)
        self.cnvtr = get_obj3.json()
        self.cnvtr2 = put_update2_object.json()







    # def test_put(self):
    #     put_update_object = requests.put(
    #         TestRequests.product_url,
    #         data=TestRequests.product_update,
    #         headers=TestRequests.product_headers,
    #     )
    #     a = put_update_object.json()["id"]
    #     get_obj = requests.get(f"{TestRequests.product_url}/{a}", headers=TestRequests.product_headers)
    #     self.cnvtr2 = get_obj.json()
    #     self.cnvtr = put_update_object.json()
    #     self.id_var_n = self.cnvtr["id"]
    #     self.name_var_n = self.cnvtr["name"]
    #     self.year_var_n = self.cnvtr["data"]["year"]
    #     self.price_var_n = int(self.cnvtr["data"]["price"])
    #     self.cpu_var_n = self.cnvtr["data"]["CPU model"]
    #     self.hard_var_n = self.cnvtr["data"]["Hard disk size"]
    #     assert get_obj.status_code == 200
    #     assert self.id_var_n == a
    #     assert self.name_var_n == self.cnvtr2["name"]
    #     assert self.year_var_n == self.cnvtr2["data"]["year"]
    #     assert self.cnvtr["data"]["price"] == self.cnvtr2["data"]["price"]
    #     assert self.cpu_var_n == self.cnvtr2["data"]["CPU model"]
    #     assert self.hard_var_n == self.cnvtr2["data"]["Hard disk size"]

TestRequests().test_post()

















