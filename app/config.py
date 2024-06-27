import os
from distutils.util import strtobool

DEBUG = bool(strtobool(os.environ.get("DEBUG", "true")))
INSIDE_DOCKER = bool(strtobool(os.environ.get("INSIDE_DOCKER", "false")))
ORM_URL = os.environ.get("ORM_URL", "mysql+pymysql://user:password@0.0.0.0/mydatabase")
SPECS_ROUTE = os.environ.get("SPECS_ROUTE", "/")
