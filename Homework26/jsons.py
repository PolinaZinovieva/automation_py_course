import json

class JsonsCollection:


    product_json = json.dumps({
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    })

    product_for_update = json.dumps({

        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    })

    string_for_partial_updt = json.dumps({
        "name": "Apple MacBook Pro 16 (Updated Name)"

    })

    product_to_del = json.dumps({

        "name": "Samsung S22",
        "data": {
            "year": 2022,
            "price": 2000,
            "CPU model": "idk",
            "Hard disk size": "1 TB",
            "color": "black"
        }

    })