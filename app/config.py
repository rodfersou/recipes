import os

ORM_URL = os.environ.get("ORM_URL", "mysql+pymysql://user:password@0.0.0.0/mydatabase")
DEBUG = bool(os.environ.get("DEBUG", "true"))
SPECS_ROUTE = os.environ.get("SPECS_ROUTE", "/")
