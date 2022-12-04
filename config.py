import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'haunc3udacitystorage1'
    BLOB_STORAGE_KEY = os.environ.get(
        'BLOB_STORAGE_KEY') or '1ApYiC86nz9cuu+fO+RdPO1eKYJLJlVmlv2j4Ikh6t1s11D6VcGAWjuiXri4k9XQSDDJBKPhjM9n+ASt+2/k4g=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get(
        'SQL_SERVER') or 'haunc3-udacity-1-server.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'db-1'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'haunc08'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'okpassword.3'
    SQLALCHEMY_DATABASE_URI = f"mssql+pymssql://{SQL_USER_NAME}:{SQL_PASSWORD}@{SQL_SERVER}/{SQL_DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    CLIENT_SECRET = os.getenv(
        "CLIENT_SECRET") or '.wP8Q~rKoPsjg--NU1PoTpQ4FHL1sf3wY42XkblY'
    if not CLIENT_SECRET:
        raise ValueError("Need to define CLIENT_SECRET environment variable")

    # For multi-tenant app, else put tenant name
    AUTHORITY = "https://login.microsoftonline.com/hcmuit.edu.vn"
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "65fad117-182b-47eb-8825-3eba0ba84794"

    # Used to form an absolute URL; must match to app's redirect_uri set in AAD
    REDIRECT_PATH = "/getAToken"

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"]  # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
