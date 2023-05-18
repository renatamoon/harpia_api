# STANDARD IMPORTS
import random
import string

# THIRD PART IMPORTS
from sqlalchemy import inspect


class HelpersFunctions:

    @classmethod
    def object_as_dict(cls, objs):
        list_ = []

        for obj in objs:
            data = {c.key: getattr(obj, c.key)
                    for c in inspect(obj).mapper.column_attrs}
            list_.append(data)

        return list_

    @classmethod
    def generate_basic_password_user(cls):
        random_numbers = ''.join(random.choices(string.digits, k=3))
        random_letters = ''.join(random.choices(string.ascii_letters, k=4))

        simple_password = random_numbers + random_letters

        return simple_password

    @classmethod
    def normalize_request_body(cls, payload):
        name_normalized = None
        role_normalized = None

        name = payload.get("name", None)
        email = payload.get("email", None)
        role = payload.get("role", None)
        password = payload.get("password", None)
        password_generated = HelpersFunctions.generate_basic_password_user()

        if name:
            name_normalized = name.title()
        if role:
            role_normalized = role.title()

        response_normalized = {
            "name": name_normalized,
            "email": email,
            "role": role_normalized,
            "password": password_generated if password is None else password
        }

        return response_normalized
