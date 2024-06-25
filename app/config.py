import os

ORM_URL = os.environ.get("ORM_URL", "mysql+pymysql://user:password@0.0.0.0/mydatabase")
DEBUG = bool(os.environ.get("DEBUG", "true"))
HOST = os.environ.get("HOST", None)
PORT = os.environ.get("PORT", None)
SPECS_ROUTE = os.environ.get("SPECS_ROUTE", "/")
