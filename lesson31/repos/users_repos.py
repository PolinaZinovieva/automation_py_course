from lesson31.session import session
from lesson31.models.users import  Users


class Users_Repository:
    def __init__(self):
        self.__session = session

    def get_all(self):
        for user in self.__session.query(Users).all():
            print(user)

    def insert_one(self, user: Users):
        self.__session.add(user)
        self.__session.commit()

    def one_by_email(self, email):
        print(self.__session.query(Users).filter_by(email=email).first())













users_repos = Users_Repository()
users_repos.get_all()
# users_repos.insert_one(Users(id = '2', first_name = ' Jack', age ='2', email = 'jack"gmail.com'))
# users_repos.get_all()

users_repos.one_by_email(email='a@gmail')