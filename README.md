# Data Engineering Group Project [![CI](https://github.com/jaxonyue/DE-Group-Project/actions/workflows/cicd.yml/badge.svg)](https://github.com/jaxonyue/DE-Group-Project/actions/workflows/cicd.yml)

## Team Members

Team: Jaxon Yue, Haochong(Harry) Xia, Vivian Zhang, Eve

## Overview
We use python to build this Flask app in `app.py`. This app provide the diagnosis of the wages change of 36 countries, which includes a data pipeline,a load testing with 10000 request per second, data engineering, and CI/CD integrations.

The Overall Archetecture of our final project is shown as below:

## Purpose
- Microservice:
    Use Python to build a microservice that includes logging and be containerized using the Distroless Docker image and interfaces with a data pipeline.
- Load Test:
    A load test verifies that the microservice is capable of handling 10,000 requests per second.
- Data Engineering:
    Involve the use of a library specializing in data engineering such as Spark, Pandas, SQL, a vector database, or any other relevant library.
- Infrastructure as Code (IaC):
    Utilize an IaC solution among AWS CloudFormation, AWS SAM, AWS CDK, or the Serverless Framework for infrastructure setup and management.
- Continuous Integration and Continuous Delivery (CI/CD):
    Implement a CI/CD pipeline through GitHub Actions.
- README.md
    A comprehensive README file that clearly explains what the project does, its dependencies, how to run the program, its limitations, potential areas for improvement, and how AI Pair Programming tools (GitHub Copilot and one more tool of our choice) were used in your development process.
- Architectural Diagram
    A clear diagram representing the architecture of our application should be included.
- GitHub Configurations
    Must include GitHub Actions and a .devcontainer configuration for GitHub Codespaces. This should make the local version of our project completely reproducible. The repository should also include GitHub Action build badges for install, lint, test, and format actions.
- Quantitative Assessment
    Include a quantitative assessment of its reliability and stability. Use data science fundamentals to describe system performance, e.g., average latency per request at different levels of requests per second (100, 1000, etc.). Think of the software system as a data science problem that needs to be described using data science principles.


## Link to the deployed app:
https://wagess.azurewebsites.net/

## File Descriptions
- `app.py`: Flask application
- `Development of Average Annual Wages.csv`: dataset.
- `loadData.py`: load the csv.
- `operations`: SQLite operation on the dataset.
- `Makefile`: Contains commands for setting up the environment, testing, linting, and formatting
- `Dockerfile`: For containerizing the application

## Key components
- **Microservice**: Use Python to deploy a seb app that can display diagnostic graphs of wages change of 36 countries.
- **Data Engineering**: Using `SQLite database` to manage wages data.
- **Load Testing**: Test 10000 request per second.
- **Continuous Integration and Continuous Delivery**: Automated using GitHub Actions.
- **Docker**: Containerize the application.
- **locust**: Package used for Loading test.
- **CI/CD**: CI/CD is implemented using GitHub Actions for automated testing and deployment.

## Key steps to run the application
1. Git clone the repo, the environment will automatically be set up with necessary dependencies installed. If it doesn't, use `make install` to install `requirements.txt`.

2. Loading the data use function `load` in `loadData.py`. The data is stored in `Development of Average Annual Wages.csv`. The database is stored in `wages.db`.

3. Use `python app.py` to run the application locally to verify that it works.

4. Use the following command to log into DockerHub, build docker image and push to container:
```
echo "your_password" | docker login --username your_username --password-stdin
docker build -t <insert member username>/wages .
docker push <insert member username>/wages
docker run -p 7000:7000 wages
```

5. Create a new web app service on Azure, select Docker Container and deploy the DockerHub image.

6. Navigate to **Configuration** -> **Application Settings**, and add `WEBSITES_PORT` with a value of 7000.

![Alt text](port-1.png)

7. Run the app using the URL provided by Azure.

## Limitations

## Potential areas for improvement

## Using Copilot and Chatgpt:
- We use copilot in two ways while writing my code:

    1. Press `Cmd+I` on macOS (or `Ctrl+I` on Windows/Linux) to bring up the Chat input to send request to Copilot. After that, we can choose if we acceptthe suggestion from copilot to write the code. In addition, the suggestion will not be fully correct. We need to modify the code to make it correct, but it provide us a template to write our code, which helps us to write code faster with less errors.

    2. Copilot will also suggest some contents automatically while we are writing code. We can press `Tab` to accept the suggestion from copilot, which also helps us to write code faster with less errors.

- For Chatgpt, it is used in the same way as the first way of using copilot. The difference is that Chatgpt can provide suggestions besides the code. However, its suggestions will not be fully correct as well.

- Hence, there are two advantages of using copilot and Chatgpt:
    1. They helps me to write code faster. 
    2. They helps me to write code with less errors. 

## Video
