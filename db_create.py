from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI as DB_URI
from config import SQLALCHEMY_MIGRATE_REPO as DB_REPO
from app import db
import os.path

db.create_all()
if not os.path.exists(DB_URI):
    api.create(DB_REPO, 'database repository')
    api.version_control(DB_URI, DB_REPO)
else:
    api.version_control(DB_URU, DB_REPO, api.version(DB_REPO))
