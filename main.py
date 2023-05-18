# THIRD PART IMPORTS
import uvicorn
from asgiref.wsgi import WsgiToAsgi

# PROJECT IMPORTS
from src.infrastructure.migrations.migrations import ScriptCreateTables as run_script
from src.routers.routers import app


asgi_app = WsgiToAsgi(app)

run_script.create_tables()
run_script.populate_roles_tables()
run_script.populate_claims_table()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
