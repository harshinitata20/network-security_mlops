import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.pipeline.training_pipeline import TrainingPipeline

if __name__ == "__main__":
    try:
        training_pipeline = TrainingPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        raise NetworkSecurityException(e, sys)
