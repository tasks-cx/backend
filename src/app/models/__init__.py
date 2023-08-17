from pymongo import MongoClient
from config import *

# Generate config URI from env
config_uri = f"mongodb://{Config.MONGO_USERNAME}:{Config.MONGO_PASSWORD}@{Config.MONGO_HOST}:{Config.MONGO_PORT}"

mongo_client = MongoClient(config_uri)
db = mongo_client[Config.MONGO_DATABASE]