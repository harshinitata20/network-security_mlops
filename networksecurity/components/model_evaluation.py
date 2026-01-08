import os
import sys
from networksecurity.entity.artifact_entity import DataValidationArtifact, ModelTrainerArtifact, ModelEvaluationArtifact
from networksecurity.entity.config_entity import ModelEvaluationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.constants.training_pipeline import TARGET_COLUMN
from networksecurity.utils.main_utils.utils import load_object, write_yaml_file
from networksecurity.utils.ml_utils.metric.classification_metric import get_classification_score
import pandas as pd

class ModelEvaluation:
    def __init__(self, model_eval_config: ModelEvaluationConfig,
                 data_validation_artifact: DataValidationArtifact,
                 model_trainer_artifact: ModelTrainerArtifact):
        try:
            self.model_eval_config = model_eval_config
            self.data_validation_artifact = data_validation_artifact
            self.model_trainer_artifact = model_trainer_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_model_evaluation(self) -> ModelEvaluationArtifact:
        """
        Method Name :   initiate_model_evaluation
        Description :   This method initiates the model evaluation component for the pipeline
        
        Output      :   Returns model evaluation artifact
        On Failure  :   Write an exception log and then raise an exception
        """
        try:
            valid_train_file_path = self.data_validation_artifact.valid_train_file_path
            valid_test_file_path = self.data_validation_artifact.valid_test_file_path

            # Valid train and test file dataframe
            train_df = pd.read_csv(valid_train_file_path)
            test_df = pd.read_csv(valid_test_file_path)

            df = pd.concat([train_df, test_df])
            y_true = df[TARGET_COLUMN]
            y_true.replace(-1, 0, inplace=True)
            df.drop(TARGET_COLUMN, axis=1, inplace=True)

            trained_model_file_path = self.model_trainer_artifact.trained_model_file_path
            model = load_object(file_path=trained_model_file_path)

            y_pred = model.predict(df)

            train_metric = get_classification_score(y_true, y_pred)
            
            logging.info(f"Model evaluation metrics: {train_metric}")

            # Save the evaluation report
            model_evaluation_report = {
                "f1_score": train_metric.f1_score,
                "precision_score": train_metric.precision_score,
                "recall_score": train_metric.recall_score,
            }

            report_file_path = self.model_eval_config.report_file_path
            os.makedirs(os.path.dirname(report_file_path), exist_ok=True)
            write_yaml_file(file_path=report_file_path, content=model_evaluation_report)

            model_evaluation_artifact = ModelEvaluationArtifact(
                is_model_accepted=True,
                improved_accuracy=train_metric.f1_score,
                report_file_path=report_file_path,
                trained_model_file_path=trained_model_file_path
            )

            logging.info(f"Model evaluation artifact: {model_evaluation_artifact}")
            return model_evaluation_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)
