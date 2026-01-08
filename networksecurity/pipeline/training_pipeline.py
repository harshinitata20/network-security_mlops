import os
import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig,
    ModelPusherConfig
)

from networksecurity.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact,
    ModelEvaluationArtifact,
    ModelPusherArtifact
)

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.components.model_evaluation import ModelEvaluation
from networksecurity.components.model_pusher import ModelPusher


class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()
    
    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        This method of TrainingPipeline class is responsible for starting data ingestion component
        """
        try:
            logging.info("Entered the start_data_ingestion method of TrainingPipeline class")
            logging.info("Getting the data from MongoDB")
            
            data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            
            logging.info("Got the train_set and test_set from MongoDB")
            logging.info("Exited the start_data_ingestion method of TrainingPipeline class")
            
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        """
        This method of TrainingPipeline class is responsible for starting data validation component
        """
        try:
            logging.info("Entered the start_data_validation method of TrainingPipeline class")
            
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=data_validation_config
            )
            data_validation_artifact = data_validation.initiate_data_validation()
            
            logging.info("Performed the data validation operation")
            logging.info("Exited the start_data_validation method of TrainingPipeline class")
            
            return data_validation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def start_data_transformation(self, data_validation_artifact: DataValidationArtifact) -> DataTransformationArtifact:
        """
        This method of TrainingPipeline class is responsible for starting data transformation component
        """
        try:
            logging.info("Entered the start_data_transformation method of TrainingPipeline class")
            
            data_transformation_config = DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            data_transformation = DataTransformation(
                data_validation_artifact=data_validation_artifact,
                data_transformation_config=data_transformation_config
            )
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            
            logging.info("Performed the data transformation operation")
            logging.info("Exited the start_data_transformation method of TrainingPipeline class")
            
            return data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def start_model_trainer(self, data_transformation_artifact: DataTransformationArtifact) -> ModelTrainerArtifact:
        """
        This method of TrainingPipeline class is responsible for starting model training
        """
        try:
            logging.info("Entered the start_model_trainer method of TrainingPipeline class")
            
            model_trainer_config = ModelTrainerConfig(training_pipeline_config=self.training_pipeline_config)
            model_trainer = ModelTrainer(
                model_trainer_config=model_trainer_config,
                data_transformation_artifact=data_transformation_artifact
            )
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            
            logging.info("Performed the model training operation")
            logging.info("Exited the start_model_trainer method of TrainingPipeline class")
            
            return model_trainer_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def start_model_evaluation(self, data_validation_artifact: DataValidationArtifact,
                             model_trainer_artifact: ModelTrainerArtifact) -> ModelEvaluationArtifact:
        """
        This method of TrainingPipeline class is responsible for starting model evaluation
        """
        try:
            logging.info("Entered the start_model_evaluation method of TrainingPipeline class")
            
            model_evaluation_config = ModelEvaluationConfig(training_pipeline_config=self.training_pipeline_config)
            model_evaluation = ModelEvaluation(
                model_eval_config=model_evaluation_config,
                data_validation_artifact=data_validation_artifact,
                model_trainer_artifact=model_trainer_artifact
            )
            model_evaluation_artifact = model_evaluation.initiate_model_evaluation()
            
            logging.info("Performed the model evaluation operation")
            logging.info("Exited the start_model_evaluation method of TrainingPipeline class")
            
            return model_evaluation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def start_model_pusher(self, model_eval_artifact: ModelEvaluationArtifact) -> ModelPusherArtifact:
        """
        This method of TrainingPipeline class is responsible for starting model pusher
        """
        try:
            logging.info("Entered the start_model_pusher method of TrainingPipeline class")
            
            model_pusher_config = ModelPusherConfig(training_pipeline_config=self.training_pipeline_config)
            model_pusher = ModelPusher(
                model_pusher_config=model_pusher_config,
                model_eval_artifact=model_eval_artifact
            )
            model_pusher_artifact = model_pusher.initiate_model_pusher()
            
            logging.info("Performed the model pusher operation")
            logging.info("Exited the start_model_pusher method of TrainingPipeline class")
            
            return model_pusher_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def run_pipeline(self):
        """
        This method of TrainingPipeline class is responsible for running complete pipeline
        """
        try:
            logging.info("Started the training pipeline")
            
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact = self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            model_trainer_artifact = self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            model_evaluation_artifact = self.start_model_evaluation(
                data_validation_artifact=data_validation_artifact,
                model_trainer_artifact=model_trainer_artifact
            )
            model_pusher_artifact = self.start_model_pusher(model_eval_artifact=model_evaluation_artifact)
            
            logging.info("Training pipeline completed successfully")
            
        except Exception as e:
            raise NetworkSecurityException(e, sys)
