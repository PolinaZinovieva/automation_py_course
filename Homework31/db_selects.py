import psycopg2
import json
class Storage1:
    def __init__(self):
        self.connection = psycopg2.connect(user='postgres', host='localhost', password='1', port='5432',
                                           database='postgres')
        self.__cursor = self.connection.cursor()

    def new_data(self,name,price,year,name2):
        self.__cursor.execute(
            f"Update api_stuff SET name = '{name}', price = {price}, year = {year} WHERE api_stuff.name= '{name2}'")
        self.connection.commit()
        product = {'name': 'Iphone 12 pro max', 'data': 'a'}
        product_2= {'year': 2019, 'price': 1849.99, 'CPU model': 'Intel Core i9', 'Hard disk size': '256 GB'}
        product['name'] = name
        product_2['price'] = price
        product_2['year'] = year
        product['data'] = product_2
        print(product)
        new_product = json.dumps(product, indent=4)
        print(new_product)

        self.__cursor.execute(f"SELECT * FROM api_stuff where name ='airpods' and year = 2022 and price = 2000;")
        return self.__cursor.fetchall()




print(Storage1().new_data(name='airpods',price=2000,year=2022,name2='a'))






