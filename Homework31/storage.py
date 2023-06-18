import psycopg2

class Storage:
    def __init__(self):
        self.connection = psycopg2.connect(user='postgres', host='localhost', password='1', port='5432',
                                           database='postgres')
        self.__cursor = self.connection.cursor()


    def create_db(self):
        self.__cursor.execute(
            'create table api_stuff(id varchar primary key, name varchar(50), year int,price float, cpu_model varchar(50), hard_disk varchar(50))'
        )
        self.connection.commit()

    def insert_into_db(self, id,name,year,price,cpu_model,hard_disk):
        self.__cursor.execute(
            f"INSERT INTO api_stuff(id,name,year,price,cpu_model, hard_disk) values ('{id}','{name}','{year}','{price}','{cpu_model}','{hard_disk}')"

        )
        self.connection.commit()

    def after_request(self, name,year,price,cpu_model,hard_disk):
        self.__cursor.execute(f"SELECT * FROM api_stuff where name ='{name}' and year = {year} and price = {price} and cpu_model = '{cpu_model}' and hard_disk = '{hard_disk}';")
        return self.__cursor.fetchall()

    def update_db(self,name,hard_disk):
        self.__cursor.execute(f"UPDATE api_stuff SET name = '{name}', hard_disk= '{hard_disk}' WHERE name= a")








    def __del__(self):
        if self.connection:
            self.__cursor.close()
            self.connection.close()

storage = Storage()

