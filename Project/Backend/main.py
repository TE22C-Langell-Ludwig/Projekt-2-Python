from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
print("Mongo URI loaded:", MONGO_URI)
client = MongoClient(MONGO_URI)
db = client["Cluster0"]
collection = db["Combined_averages"]

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/stats/latest")
def get_latest_stats():
    doc = collection.find_one({"_id": "combined_average"}, {"_id": 0})
    if doc:
        return doc
    return {"error": "No stats found in MongoDB"}
