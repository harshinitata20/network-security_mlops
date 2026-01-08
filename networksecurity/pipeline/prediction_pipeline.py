import os
import sys
import pandas as pd
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.utils.main_utils.utils import load_object

class NetworkData:
    def __init__(self,
                 having_IP_Address,
                 URL_Length,
                 Shortining_Service,
                 having_At_Symbol,
                 double_slash_redirecting,
                 Prefix_Suffix,
                 having_Sub_Domain,
                 SSLfinal_State,
                 Domain_registeration_length,
                 Favicon,
                 port,
                 HTTPS_token,
                 Request_URL,
                 URL_of_Anchor,
                 Links_in_tags,
                 SFH,
                 Submitting_to_email,
                 Abnormal_URL,
                 Redirect,
                 on_mouseover,
                 RightClick,
                 popUpWidnow,
                 Iframe,
                 age_of_domain,
                 DNSRecord,
                 web_traffic,
                 Page_Rank,
                 Google_Index,
                 Links_pointing_to_page,
                 Statistical_report):
        """
        Network Data constructor
        Input: all features of the trained model for prediction
        """
        try:
            self.having_IP_Address = having_IP_Address
            self.URL_Length = URL_Length
            self.Shortining_Service = Shortining_Service
            self.having_At_Symbol = having_At_Symbol
            self.double_slash_redirecting = double_slash_redirecting
            self.Prefix_Suffix = Prefix_Suffix
            self.having_Sub_Domain = having_Sub_Domain
            self.SSLfinal_State = SSLfinal_State
            self.Domain_registeration_length = Domain_registeration_length
            self.Favicon = Favicon
            self.port = port
            self.HTTPS_token = HTTPS_token
            self.Request_URL = Request_URL
            self.URL_of_Anchor = URL_of_Anchor
            self.Links_in_tags = Links_in_tags
            self.SFH = SFH
            self.Submitting_to_email = Submitting_to_email
            self.Abnormal_URL = Abnormal_URL
            self.Redirect = Redirect
            self.on_mouseover = on_mouseover
            self.RightClick = RightClick
            self.popUpWidnow = popUpWidnow
            self.Iframe = Iframe
            self.age_of_domain = age_of_domain
            self.DNSRecord = DNSRecord
            self.web_traffic = web_traffic
            self.Page_Rank = Page_Rank
            self.Google_Index = Google_Index
            self.Links_pointing_to_page = Links_pointing_to_page
            self.Statistical_report = Statistical_report
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def get_data_as_dataframe(self):
        """
        This function returns a dataframe with the data
        """
        try:
            input_data = {
                "having_IP_Address": [self.having_IP_Address],
                "URL_Length": [self.URL_Length],
                "Shortining_Service": [self.Shortining_Service],
                "having_At_Symbol": [self.having_At_Symbol],
                "double_slash_redirecting": [self.double_slash_redirecting],
                "Prefix_Suffix": [self.Prefix_Suffix],
                "having_Sub_Domain": [self.having_Sub_Domain],
                "SSLfinal_State": [self.SSLfinal_State],
                "Domain_registeration_length": [self.Domain_registeration_length],
                "Favicon": [self.Favicon],
                "port": [self.port],
                "HTTPS_token": [self.HTTPS_token],
                "Request_URL": [self.Request_URL],
                "URL_of_Anchor": [self.URL_of_Anchor],
                "Links_in_tags": [self.Links_in_tags],
                "SFH": [self.SFH],
                "Submitting_to_email": [self.Submitting_to_email],
                "Abnormal_URL": [self.Abnormal_URL],
                "Redirect": [self.Redirect],
                "on_mouseover": [self.on_mouseover],
                "RightClick": [self.RightClick],
                "popUpWidnow": [self.popUpWidnow],
                "Iframe": [self.Iframe],
                "age_of_domain": [self.age_of_domain],
                "DNSRecord": [self.DNSRecord],
                "web_traffic": [self.web_traffic],
                "Page_Rank": [self.Page_Rank],
                "Google_Index": [self.Google_Index],
                "Links_pointing_to_page": [self.Links_pointing_to_page],
                "Statistical_report": [self.Statistical_report],
            }
            return pd.DataFrame(input_data)
        except Exception as e:
            raise NetworkSecurityException(e, sys)


class PredictionPipeline:
    def __init__(self):
        """
        Initialize prediction pipeline
        """
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def predict(self, dataframe):
        """
        This method performs prediction
        """
        try:
            model_path = os.path.join("saved_models", "model.pkl")
            
            # Check if model exists
            if not os.path.exists(model_path):
                # Look for the latest model in saved_models directory
                saved_models_dir = "saved_models"
                if os.path.exists(saved_models_dir):
                    model_dirs = [d for d in os.listdir(saved_models_dir) if os.path.isdir(os.path.join(saved_models_dir, d))]
                    if model_dirs:
                        # Get the latest model directory
                        latest_model_dir = sorted(model_dirs)[-1]
                        model_path = os.path.join(saved_models_dir, latest_model_dir, "model.pkl")
            
            logging.info(f"Loading model from: {model_path}")
            model = load_object(file_path=model_path)
            
            prediction = model.predict(dataframe)
            
            return prediction
        except Exception as e:
            raise NetworkSecurityException(e, sys)
