import psycopg2


class UserRepository:
    def __init__(self):
        self.connection = psycopg2.connect(user ='postgres', host='localhost', password ='1',port ='5432',database='postgres')
        self.__cursor = self.connection.cursor()

    def get_all(self):
        self.__cursor.execute(
            'SELECT * FROM users'
        )
        return self.__cursor.fetchall()
    def get_emails(self):
        self.__cursor.execute('Select email from users;')
        return self.__cursor.fetchall()

    def update_one_by_email(self,name,email):
        self.__cursor.execute(
            f"update users set first_name = '{name}'where users.email = '{email}' "
                            )

    def add_new_row(self, name,last_name,email,age):
        self.__cursor.execute(
            f"insert into users(first_name,last_name,age,email) values ('{name}','{last_name}','{age}', '{email}')"
        )
        self.connection.commit()
    def __del__(self):
        if self.connection:
            self.__cursor.close()
            self.connection.close()

user_repo = UserRepository()
print(user_repo.get_all())
print(user_repo.get_emails())
user_repo.update_one_by_email('Leo','pendo.dow@gmail.com')
user_repo.connection.commit()
print(user_repo.get_all())
user_repo.add_new_row('Arnold','Zelo','zel@gmail.com','34')
print(user_repo.get_all())
