from lesson31.session import session
from lesson31.models.users import  Users


class Users_Repository:
    def __init__(self):
        self.__session = session

    def get_all(self):
        for user in self.__session.query(Users).all():
            print(user)
users_repos = Users_Repository()
users_repos.get_all()