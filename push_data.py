import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def csv_to_json(self, file_path):
        try:
            # Check if file is Excel or CSV
            if file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                data = pd.read_excel(file_path)
            else:
                data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def insert_data_mongodb(self, records, database, collection_name):
        try:
            self.database = database
            self.collection_name = collection_name
            self.records = records
            
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            self.database = self.mongo_client[self.database]
            
            self.collection = self.database[self.collection_name]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == '__main__':
    FILE_PATH = "Network_Data/phisingData.csv.xlsx"
    DATABASE = "MLOPS_DB"
    COLLECTION = "NetworkData"
    
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json(file_path=FILE_PATH)
    print(records[0])
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, COLLECTION)
    print(f"Successfully inserted {no_of_records} records into MongoDB")
        





