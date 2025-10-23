from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

_client = AsyncIOMotorClient(settings.MONGO_URI)
_database = _client[settings.DB_NAME]

def get_database():
    return _database
