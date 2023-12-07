# Data Engineering Group Project [![CI](https://github.com/jaxonyue/DE-Group-Project/actions/workflows/cicd.yml/badge.svg)](https://github.com/jaxonyue/DE-Group-Project/actions/workflows/cicd.yml)

## Team Members

Team: Jaxon Yue, Haochong(Harry) Xia, Vivian Zhang, Eve

## Overview
We use python to build this Flask app in `app.py`. This app provide the diagnosis of the wages change of 36 countries, which includes a data pipeline,a load testing with 10000 request per second, data engineering, and CI/CD integrations.

The Overall Archetecture of our final project is shown as below:

## Link to the deployed app:
https://wagess.azurewebsites.net/

## Features
- **Microservice**: Provides ICU-related information for specified MMSAs.
- **Data Engineering**: Using `SQLite database` to manage wages data.
- **Load Testing**: Test 10000 request per second.
- **Continuous Integration and Continuous Delivery**: Automated using GitHub Actions.

## Technologies
- Python
- SQLite database
- Docker
- Use locust for load test

## Setup and Installation
1. Clone the repository

2. Install `requirements.txt` using `make install`


## Running the Application
- **Locally**: python app.py
- **Using Docker**:
```
docker build -t <insert member username>/wages .
docker push <insert member username>/wages
docker run -p 7000:7000 wages
```

## Endpoints
http://0.0.0.0:7000/api/wages

## Database Setup
Loading the data use function `load` in `loadData.py`.

## File Descriptions
- `app.py`: Flask application
- `Development of Average Annual Wages.csv`: dataset.
- `loadData.py`: load the csv.
- `operations`: SQLite operation on the dataset.
- `Makefile`: Contains commands for setting up the environment, testing, linting, and formatting
- `Dockerfile`: For containerizing the application

## CI/CD
CI/CD is implemented using GitHub Actions for automated testing and deployment.

## Video
