import requests
import json


class NationalityByNameApi:
    def __init__(self):
        self.__url = "https://api.nationalize.io/"

    def get_nationality(self, name: str):
        request = requests.get(self.__url, params={"name": name})
        return request.json()

    def response_to_json(self, data):
        json_file = json.dumps(data, indent=2)
        with open("response.json", "w", encoding="utf-8") as file_json:
            file_json.write(json_file)


send_request = NationalityByNameApi().get_nationality("polina")
print(send_request)
NationalityByNameApi().response_to_json(send_request)
