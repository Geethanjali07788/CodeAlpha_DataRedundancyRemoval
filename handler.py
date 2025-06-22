import hashlib
from db import get_collection

collection = get_collection()

def validate_data(data: dict) -> bool:
    return isinstance(data, dict) and "name" in data and "value" in data

def hash_data(data: dict) -> str:
    return hashlib.sha256(str(data).encode()).hexdigest()

def is_duplicate(data_hash: str) -> bool:
    return collection.find_one({"hash": data_hash}) is not None

def insert_data(data: dict) -> str:
    if not validate_data(data):
        return "Invalid data format"

    data_hash = hash_data(data)
    if is_duplicate(data_hash):
        return "Duplicate data found"

    collection.insert_one({"data": data, "hash": data_hash})
    return "Data inserted successfully"