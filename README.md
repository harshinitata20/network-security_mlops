# Network Security Phishing Detection MLOps Project

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A complete end-to-end MLOps project for detecting phishing websites using machine learning with FastAPI, Docker, and CI/CD pipeline.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Docker Deployment](#docker-deployment)
- [CI/CD Pipeline](#cicd-pipeline)
- [Contributing](#contributing)

## 🎯 Overview

This project implements a complete MLOps pipeline for phishing website detection. It includes data ingestion from MongoDB, data validation, transformation, model training, evaluation, and deployment via FastAPI with Docker containerization.

## 🚀 Features

- **Complete ML Pipeline**: Data ingestion → Validation → Transformation → Training → Evaluation → Deployment
- **MongoDB Integration**: Automated data ingestion from MongoDB Atlas
- **Data Validation**: Schema validation and data drift detection using Kolmogorov-Smirnov test
- **Feature Engineering**: KNN imputation for missing values
- **Model Training**: Multiple algorithms (RandomForest, DecisionTree, GradientBoosting, etc.)
- **Model Evaluation**: F1-score, Precision, Recall metrics
- **REST API**: FastAPI for model serving
- **Batch Prediction**: CSV file upload support
- **Docker Support**: Containerized deployment
- **CI/CD Pipeline**: GitHub Actions for automated testing and deployment
- **Logging & Exception Handling**: Comprehensive logging and custom exceptions

## 📁 Project Structure
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Project Components](#project-components)
- [Contributing](#contributing)
- [License](#license)

## 🔍 Overview

This project implements an end-to-end machine learning pipeline for network security analysis, including phishing detection. It follows MLOps best practices with modular code architecture, automated pipelines, and cloud deployment capabilities.

## 📁 Project Structure

```
NetworkSecurity/
├── Network_Data/              # Dataset directory
│   └── phisingData.csv.xlsx  # Phishing detection dataset
├── networksecurity/           # Main package
│   ├── __init__.py
│   ├── cloud/                # Cloud deployment utilities
│   ├── components/           # ML pipeline components
│   ├── constants/            # Project constants and configurations
│   ├── entity/               # Data entities and schemas
│   ├── exception/            # Custom exception handlers
│   ├── logging/              # Logging configuration
│   ├── pipeline/             # Training and prediction pipelines
│   └── utils/                # Utility functions
├── notebooks/                 # Jupyter notebooks for EDA
├── .github/                  
│   └── workflows/            # CI/CD workflows
├── Dockerfile                # Docker configuration
├── requirements.txt          # Project dependencies
├── setup.py                  # Package setup configuration
├── .gitignore               # Git ignore rules
└── README.md                # Project documentation
```

## ✨ Features

- **Modular Architecture**: Well-organized code structure with separation of concerns
- **ML Pipeline**: Complete training and prediction pipelines
- **Cloud Integration**: Ready for cloud deployment (AWS/Azure/GCP)
- **Logging & Monitoring**: Comprehensive logging system
- **Exception Handling**: Custom exception handling framework
- **Containerization**: Docker support for easy deployment
- **CI/CD**: GitHub Actions workflow integration
- **Data Management**: Structured data handling and preprocessing

## 🚀 Installation

### Prerequisites
- Python 3.10+
- Conda or Miniconda
- Git

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/NetworkSecurity.git
cd NetworkSecurity
```

2. **Create and activate conda environment**
```bash
conda create -p venv python=3.10 -y
conda activate C:\Users\Harshini\OneDrive\Documents\Desktop\mlops\NetworkSecurity\venv
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Install the package**
```bash
pip install -e .
```

## 📊 Usage

### Training Pipeline
```python
from networksecurity.pipeline import TrainingPipeline

# Initialize and run training pipeline
pipeline = TrainingPipeline()
pipeline.run()
```

### Prediction Pipeline
```python
from networksecurity.pipeline import PredictionPipeline

# Initialize and run prediction pipeline
pipeline = PredictionPipeline()
predictions = pipeline.predict(data)
```

## 📈 Dataset

The project uses a phishing detection dataset (`phisingData.csv.xlsx`) located in the `Network_Data/` directory. The dataset contains features related to network traffic and website characteristics for identifying phishing attempts.

## 🔧 Project Components

### Components
- **Data Ingestion**: Handles data loading and initial processing
- **Data Validation**: Validates data quality and schema
- **Data Transformation**: Feature engineering and preprocessing
- **Model Training**: ML model training and evaluation
- **Model Evaluation**: Performance metrics and validation

### Entity
- Data classes and schemas for pipeline configuration
- Input/output data structures

### Exception & Logging
- Custom exception classes for error handling
- Structured logging for debugging and monitoring

### Cloud
- Cloud storage integration
- Model deployment utilities

### Utils
- Helper functions and utilities
- Common operations and transformations

## 🐳 Docker

Build and run the Docker container:

```bash
# Build image
docker build -t networksecurity .

# Run container
docker run -p 8080:8080 networksecurity
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Harshini**

## 🙏 Acknowledgments

- Thanks to the open-source community for the tools and libraries used in this project
- Special thanks to contributors and supporters

---

**Note**: Make sure to add your `.env` file with necessary credentials before running the project. Never commit sensitive information to the repository.
