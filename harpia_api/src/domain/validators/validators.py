# THIRD PART IMPORTS
from pydantic import BaseModel, validator, EmailStr, root_validator


class UserDataValidator(BaseModel):
    name: str
    email: EmailStr
    role: str
    password: str = None

    @root_validator(pre=True)
    def validate_unexpected_fields_from_body(cls, values):
        allowed_fields = {'name', 'email', 'role', 'password'}

        not_allowed_field = set(values) - allowed_fields

        if not_allowed_field:
            raise ValueError(f"Unexpected field was sent to the request body: {', '.join(not_allowed_field)}")

        return values

    @validator('name')
    def validate_name(cls, v: str) -> str:
        if v == "" or not v:
            raise ValueError(
                "Error: name is a required field"
            )

        return v

    @validator('email')
    def validate_email(cls, v: str) -> str:
        if v == "" or not v:
            raise ValueError(
                "Error: Email is a required field"
            )

        return v

    @validator('role')
    def validate_role(cls, v: str) -> str:
        if v == "" or not v:
            raise ValueError(
                "Error: Email is a required field"
            )

        if v not in ["Gold", "Silver", "Bronze"]:
            raise ValueError(
                "Error: You may only use the roles: Gold, Silver and Bronze. Try again"
            )

        return v
