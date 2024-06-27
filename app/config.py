import os

DEBUG = bool(os.environ.get("DEBUG", "true"))
INSIDE_DOCKER = bool(os.environ.get("INSIDE_DOCKER", "false"))
ORM_URL = os.environ.get("ORM_URL", "mysql+pymysql://user:password@0.0.0.0/mydatabase")
SPECS_ROUTE = os.environ.get("SPECS_ROUTE", "/")
