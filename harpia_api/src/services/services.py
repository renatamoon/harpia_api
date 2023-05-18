# PROJECT IMPORTS
from src.repositories.repositories import SqlAlchemyRepositories


class UserServices:

    @classmethod
    def get_list_user(cls):
        query_response = SqlAlchemyRepositories.get_users_from_database()

        keys = ['Name', 'Email', 'User Role', 'Claim']

        data_list = [dict(zip(keys, values)) for values in query_response]
        return data_list

    @classmethod
    def create_user(cls, data):
        response = SqlAlchemyRepositories.create_new_user_database(
            name=data["name"], email=data["email"], password=data["password"],
            description=data["role"],
        )

        return response
