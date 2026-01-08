from fastapi import FastAPI, Request, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uvicorn import run as app_run
from pydantic import BaseModel
import pandas as pd
import sys
import os

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.pipeline.training_pipeline import TrainingPipeline
from networksecurity.pipeline.prediction_pipeline import PredictionPipeline, NetworkData

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Templates
templates = Jinja2Templates(directory="templates")


class NetworkDataInput(BaseModel):
    having_IP_Address: int
    URL_Length: int
    Shortining_Service: int
    having_At_Symbol: int
    double_slash_redirecting: int
    Prefix_Suffix: int
    having_Sub_Domain: int
    SSLfinal_State: int
    Domain_registeration_length: int
    Favicon: int
    port: int
    HTTPS_token: int
    Request_URL: int
    URL_of_Anchor: int
    Links_in_tags: int
    SFH: int
    Submitting_to_email: int
    Abnormal_URL: int
    Redirect: int
    on_mouseover: int
    RightClick: int
    popUpWidnow: int
    Iframe: int
    age_of_domain: int
    DNSRecord: int
    web_traffic: int
    Page_Rank: int
    Google_Index: int
    Links_pointing_to_page: int
    Statistical_report: int


@app.get("/", tags=["authentication"])
async def index():
    return JSONResponse(content={"message": "Welcome to Network Security Phishing Detection API"})


@app.get("/train")
async def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
        return JSONResponse(content={"message": "Training successful!"})
    except Exception as e:
        raise NetworkSecurityException(e, sys)


@app.post("/predict")
async def predict_route(data: NetworkDataInput):
    try:
        network_data = NetworkData(
            having_IP_Address=data.having_IP_Address,
            URL_Length=data.URL_Length,
            Shortining_Service=data.Shortining_Service,
            having_At_Symbol=data.having_At_Symbol,
            double_slash_redirecting=data.double_slash_redirecting,
            Prefix_Suffix=data.Prefix_Suffix,
            having_Sub_Domain=data.having_Sub_Domain,
            SSLfinal_State=data.SSLfinal_State,
            Domain_registeration_length=data.Domain_registeration_length,
            Favicon=data.Favicon,
            port=data.port,
            HTTPS_token=data.HTTPS_token,
            Request_URL=data.Request_URL,
            URL_of_Anchor=data.URL_of_Anchor,
            Links_in_tags=data.Links_in_tags,
            SFH=data.SFH,
            Submitting_to_email=data.Submitting_to_email,
            Abnormal_URL=data.Abnormal_URL,
            Redirect=data.Redirect,
            on_mouseover=data.on_mouseover,
            RightClick=data.RightClick,
            popUpWidnow=data.popUpWidnow,
            Iframe=data.Iframe,
            age_of_domain=data.age_of_domain,
            DNSRecord=data.DNSRecord,
            web_traffic=data.web_traffic,
            Page_Rank=data.Page_Rank,
            Google_Index=data.Google_Index,
            Links_pointing_to_page=data.Links_pointing_to_page,
            Statistical_report=data.Statistical_report
        )
        
        dataframe = network_data.get_data_as_dataframe()
        prediction_pipeline = PredictionPipeline()
        prediction = prediction_pipeline.predict(dataframe)
        
        result = "Phishing Website" if prediction[0] == 1 else "Legitimate Website"
        
        return JSONResponse(content={
            "prediction": int(prediction[0]),
            "result": result
        })
    except Exception as e:
        raise NetworkSecurityException(e, sys)


@app.post("/predict_csv")
async def predict_csv_route(file: UploadFile = File(...)):
    try:
        # Read CSV file
        contents = await file.read()
        
        # Save temporarily
        temp_file = "temp_prediction.csv"
        with open(temp_file, "wb") as f:
            f.write(contents)
        
        # Read dataframe
        df = pd.read_csv(temp_file)
        
        # Remove target column if exists
        if "Result" in df.columns:
            df = df.drop("Result", axis=1)
        
        # Make predictions
        prediction_pipeline = PredictionPipeline()
        predictions = prediction_pipeline.predict(df)
        
        # Add predictions to dataframe
        df["Prediction"] = predictions
        df["Result"] = df["Prediction"].apply(lambda x: "Phishing" if x == 1 else "Legitimate")
        
        # Save result
        output_file = "predictions_output.csv"
        df.to_csv(output_file, index=False)
        
        # Clean up
        os.remove(temp_file)
        
        return JSONResponse(content={
            "message": "Predictions completed successfully",
            "total_records": len(df),
            "phishing_count": int((predictions == 1).sum()),
            "legitimate_count": int((predictions == 0).sum()),
            "output_file": output_file
        })
    except Exception as e:
        raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    app_run(app, host="0.0.0.0", port=8000)
