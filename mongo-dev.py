#!/usr/bin/env python

from pymongo import MongoClient
from datetime import datetime
import pytz

cet_zone = pytz.timezone('Europe/Paris')
cet_time = datetime.now(cet_zone)
#print(cet_time)

client = MongoClient()
client = MongoClient("mongodb://root:password@kalyan:27017/?authSource=admin")
db = client.ayurwise
collection = db.chat_history

chat1 = {
    "user": "Krishna",
    "question": "What is 1+2",
    "answer": "3",
    "date": cet_time,
}
chat_id = collection.insert_one(chat1).inserted_id
print(chat_id)

print(db)
print(db.list_collection_names())
