import sys
from pandas import DataFrame
from sklearn.pipeline import Pipeline
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkModel:
    def __init__(self, preprocessor: Pipeline, model: object):
        """
        :param preprocessor: Preprocessor Object
        :param model: Trained Model Object
        """
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def predict(self, x: DataFrame) -> DataFrame:
        """
        :param x: Input dataframe
        :return: Returns predicted value
        """
        try:
            x_transform = self.preprocessor.transform(x)
            y_hat = self.model.predict(x_transform)
            return y_hat
        except Exception as e:
            raise NetworkSecurityException(e, sys)
