# THIRD PART IMPORTS
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# PROJECT IMPORTS
from src.infrastructure.postgres.infrastructure import PostgresDBInfrastructure
from src.models.models import Base


class ScriptCreateTables:

    @staticmethod
    def create_tables():
        connection = PostgresDBInfrastructure.get_postgres_connection()

        engine = create_engine('postgresql+psycopg2://', creator=lambda: connection)
        Session = sessionmaker(bind=engine)
        session = Session()

        Base.metadata.create_all(engine, checkfirst=True)
        session.close()

    @classmethod
    def populate_roles_tables(cls):
        connection = PostgresDBInfrastructure.get_postgres_connection()
        engine = create_engine('postgresql+psycopg2://', creator=lambda: connection)

        with engine.begin() as connection:
            script = """
                        INSERT INTO roles (description)
                        SELECT d.description
                        FROM (VALUES ('Gold'), ('Silver'), ('Bronze')) AS d(description)
                        WHERE NOT EXISTS (
                        SELECT 1
                        FROM roles r
                        WHERE r.description = d.description
                    )
            """
            connection.execute(script)

    @classmethod
    def populate_claims_table(cls):
        connection = PostgresDBInfrastructure.get_postgres_connection()
        engine = create_engine('postgresql+psycopg2://', creator=lambda: connection)

        with engine.begin() as connection:
            script = """
                INSERT INTO claims (description, active)
                SELECT d.description, d.active
                FROM (VALUES ('Create', true), ('Read', true), ('Update', true), ('Delete', true)) AS d(description, active)
                WHERE NOT EXISTS (
                    SELECT 1
                    FROM claims c
                    WHERE c.description = d.description
                );
                """
            connection.execute(script)
