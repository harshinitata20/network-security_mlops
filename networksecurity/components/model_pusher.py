import os
import sys
import shutil
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.artifact_entity import ModelPusherArtifact, ModelEvaluationArtifact
from networksecurity.entity.config_entity import ModelPusherConfig

class ModelPusher:
    def __init__(self, model_pusher_config: ModelPusherConfig,
                 model_eval_artifact: ModelEvaluationArtifact):
        """
        :param model_pusher_config: Configuration for model pusher
        :param model_eval_artifact: Output reference of model evaluation artifact stage
        """
        try:
            self.model_pusher_config = model_pusher_config
            self.model_eval_artifact = model_eval_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_model_pusher(self) -> ModelPusherArtifact:
        """
        Method Name :   initiate_model_pusher
        Description :   This method initiates the model pusher component for the pipeline
        
        Output      :   Returns model pusher artifact
        On Failure  :   Write an exception log and then raise an exception
        """
        try:
            logging.info("Entered initiate_model_pusher method of ModelPusher class")
            
            # Create model pusher dir to save model
            model_file_path = self.model_eval_artifact.trained_model_file_path
            
            # Create directory for model pusher
            model_pusher_dir = os.path.dirname(self.model_pusher_config.model_file_path)
            os.makedirs(model_pusher_dir, exist_ok=True)
            
            # Copy model to model pusher directory
            shutil.copy(src=model_file_path, dst=self.model_pusher_config.model_file_path)
            
            # Create directory for saved models
            saved_model_dir = os.path.dirname(self.model_pusher_config.saved_model_path)
            os.makedirs(saved_model_dir, exist_ok=True)
            
            # Copy model to saved models directory
            shutil.copy(src=model_file_path, dst=self.model_pusher_config.saved_model_path)

            # Prepare artifact
            model_pusher_artifact = ModelPusherArtifact(
                saved_model_path=self.model_pusher_config.saved_model_path,
                model_file_path=self.model_pusher_config.model_file_path
            )
            
            logging.info(f"Model pusher artifact: {model_pusher_artifact}")
            return model_pusher_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
