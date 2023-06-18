import psycopg2

class Storage:
    def __init__(self):
        self.connection = psycopg2.connect(user='postgres', host='localhost', password='1', port='5432',
                                           database='postgres')
        self.__cursor = self.connection.cursor()


    def create_db(self):
        self.__cursor.execute(
            'create table api_stuff(id varchar primary key, name varchar(50), year int,price int, cpu_model varchar(50), hard_disk varchar(50))'
        )
        self.connection.commit()

    def insert_into_db(self, id,name,year,cpu_model,hard_disk):
        self.__cursor.execute(
            f"insert into api_stuff(id,name,year,cpu_model, hard_disk) values ('{id}','{name}','{year}', '{cpu_model}','{hard_disk}')"

        )
        self.connection.commit()

    def select_everything(self):
        self.__cursor.execute('Select * from api_stuff')


    def __del__(self):
        if self.connection:
            self.__cursor.close()
            self.connection.close()

storage = Storage()
# storage.create_db()
print(storage.select_everything())
