import psycopg2
class Storage1:
    def __init__(self):
        self.connection = psycopg2.connect(user='postgres', host='localhost', password='1', port='5432',
                                           database='postgres')
        self.__cursor = self.connection.cursor()


    def after_post_request(self):
        self.__cursor.execute("SELECT * FROM api_stuff where name ='Apple MacBook Pro 16' and year = 2019 and price = 1849 and cpu_model = 'Intel Core i9' and hard_disk = '1 TB';")
        return self.__cursor.fetchall()

stor = Storage1()
print(stor.after_post_request())


