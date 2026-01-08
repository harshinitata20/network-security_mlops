import os
import sys
import pandas as pd
import pymongo
from dotenv import load_dotenv
from typing import List
from sklearn.model_selection import train_test_split

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        """
        :param data_ingestion_config: configuration for data ingestion
        """
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def export_collection_as_dataframe(self):
        """
        Read data from MongoDB and return as pandas DataFrame
        """
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            collection = self.mongo_client[database_name][collection_name]
            
            df = pd.DataFrame(list(collection.find()))
            
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            
            df.replace({"na": pd.NA}, inplace=True)
            
            return df
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def export_data_into_feature_store(self, dataframe: pd.DataFrame):
        """
        Export dataframe to feature store
        """
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            
            # Creating folder
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def split_data_as_train_test(self, dataframe: pd.DataFrame):
        """
        Split the dataframe into train and test set
        """
        try:
            train_set, test_set = train_test_split(
                dataframe,
                test_size=self.data_ingestion_config.train_test_split_ratio
            )
            logging.info("Performed train test split on the dataframe")
            
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path, exist_ok=True)
            
            logging.info(f"Exporting train and test file path.")
            train_set.to_csv(
                self.data_ingestion_config.training_file_path,
                index=False,
                header=True
            )
            test_set.to_csv(
                self.data_ingestion_config.testing_file_path,
                index=False,
                header=True
            )
            
            logging.info(f"Exported train and test file path.")
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_ingestion(self):
        """
        Method Name :   initiate_data_ingestion
        Description :   This method initiates the data ingestion components of training pipeline
        
        Output      :   train set and test set are returned as the artifacts of data ingestion components
        On Failure  :   Write an exception log and then raise an exception
        """
        try:
            logging.info("Starting data ingestion")
            dataframe = self.export_collection_as_dataframe()
            logging.info(f"Shape of dataframe: {dataframe.shape}")
            dataframe = self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe=dataframe)
            
            data_ingestion_artifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_file_path,
                test_file_path=self.data_ingestion_config.testing_file_path
            )
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
