import os

from sqlalchemy import create_engine

ORM_URL = os.environ.get(
    "ORM_URL",
    "mysql+pymysql://user:password@0.0.0.0/mydatabase"
)
DEBUG = bool(os.environ.get("DEBUG", "true"))
HOST = os.environ.get("HOST", "0.0.0.0")
PORT = os.environ.get("PORT", "5000")
SPECS_ROUTE = os.environ.get("SPECS_ROUTE", "/")

engine = create_engine(ORM_URL, echo=DEBUG)
