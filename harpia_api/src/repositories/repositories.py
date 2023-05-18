# STANDARD IMPORTS
import datetime
from datetime import datetime

# THIRD PART IMPORTS
from sqlalchemy import desc

# PROJECT IMPORTS
from src.infrastructure.postgres.infrastructure import PostgresDBInfrastructure
from src.models.models import Role, Claim, User, UserClaim
from src.utils.utils import HelpersFunctions


class SqlAlchemyRepositories:
    infra = PostgresDBInfrastructure

    @classmethod
    def get_users_from_database(cls):
        session = cls.infra.get_session()

        query_response = session.query(User.name, User.email, Role.description, Claim.description) \
            .join(Role, User.role_id == Role.id) \
            .join(UserClaim, User.id == UserClaim.user_id) \
            .join(Claim, UserClaim.claim_id == Claim.id) \
            .all()

        return query_response

    @classmethod
    def get_roles_from_database(cls, session):
        roles = session.query(Role).order_by(desc(Role.id)).all()
        roles_list = HelpersFunctions.object_as_dict(roles)

        response = []

        for role in roles_list:
            role_obj = {
                "id": role["id"],
                "description": role["description"]
            }
            response.append(role_obj)

        return response

    @classmethod
    def get_claims_from_database(cls, session):
        claims = session.query(Claim).order_by(desc(Claim.id)).all()
        claims_list = HelpersFunctions.object_as_dict(claims)

        response = []

        for claim in claims_list:
            claim_obj = {
                "id": claim["id"],
                "description": claim["description"]
            }
            response.append(claim_obj)

        return response

    @classmethod
    def create_new_user_database(cls, name, email, password, description):
        session = cls.infra.get_session()
        roles = cls.get_roles_from_database(session)
        claims = cls.get_claims_from_database(session)

        role_id = next(role["id"] for role in roles if role["description"] == description)
        claim_id = next(claim["id"] for claim in claims if claim["description"] == "Read")

        user = User(
            name=name,
            email=email,
            password=password,
            role_id=role_id,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        session.add(user)
        session.commit()

        user_claims = UserClaim(
            user_id=user.id,
            claim_id=claim_id,
        )
        session.add(user_claims)
        session.commit()

        response = {"DATABASE": "Data Inserted on System"}

        return response
