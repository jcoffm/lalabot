from config import settings
from orator import DatabaseManager

db = DatabaseManager(dict(settings.db))
