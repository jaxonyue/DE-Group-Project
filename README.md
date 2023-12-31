# Data Engineering Group Project [![CI](https://github.com/jaxonyue/DE-Group-Project/actions/workflows/cicd.yml/badge.svg)](https://github.com/jaxonyue/DE-Group-Project/actions/workflows/cicd.yml)

- Flask App: https://wagess.azurewebsites.net/
- YouTube Demo: https://www.youtube.com/watch?v=L81pk2aqBRk

## Team Members

Team: Jaxon Yue, Haochong(Harry) Xia, Xiyue(Vivian) Zhang, Xinyi(Eve) Sheng

## Overview
We use python to build this Flask app in `app.py`. This app provide the diagnosis of the World Bank Average Wages growth of 38 countries, which includes a data pipeline,a load test, data engineering, and CI/CD integrations. Since our microservice's primary role is to process data from a data pipeline and doesn't need to be directly called by other services, we don't need an API. Instead, the microservice focus on processing data, interfacing with the data pipeline, and performing any necessary tasks without exposing an external API.

The Overall Archetecture of our final project is shown as below:
![PHOTO-2023-12-09-21-35-31](https://github.com/jaxonyue/DE-Group-Project/assets/143654445/687baed4-7c13-478f-a107-6f24615c48e4)

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

## File Descriptions
- `app.py`: Flask application
- `Development of Average Annual Wages_1.csv` and `Development of Average Annual Wages_2.csv`: dataset.
- `loadData.py`: load the csv.
- `operations`: SQLite operation on the dataset.
- `Makefile`: Contains commands for setting up the environment, testing, linting, and formatting
- `Dockerfile`: For containerizing the application

## Key components
- **Microservice**: Use Python to deploy a web app that can display tables and line graphs of World Bank Average Wages growth of 38 countries.
- **Data Engineering**: Using `SQLite database` to manage wages data.
- **Load Testing**: Test based on request per second.
- **Continuous Integration and Continuous Delivery**: Automated using GitHub Actions.
- **Docker**: Containerize the application.
- **IaC**: Use Terraform to create the infrastructure on Azure.
- **locust**: Package used for Loading test.
- **CI/CD**: CI/CD is implemented using GitHub Actions for automated testing and deployment.
- **Teamwork Reflections**: Contains every team member's teamwork reflection report.

## App Introduction
- This app is a simple web app that can provide you a table with wage information and a line graph about the wage growth of the selected country. It includes following features:
1. A title indicates the purpose of this app
2. A button to select which country you are interested in
3. A button to generate the graph

![Alt text](images/app.png)

## Key steps to run the application
1. Git clone the repo, the environment will automatically be set up with necessary dependencies installed. If it doesn't, use `make install` to install `requirements.txt`.

2. Loading the data use function `load` in `loadData.py`. The data is stored in `Development of Average Annual Wages_1.csv` and `Development of Average Annual Wages_2.csv`. The database is stored in `wages.db`.

3. Use `python app.py` to run the application locally to verify that it works.

4. Use the following command to log into DockerHub, build docker image and push to container:
```
echo "your_password" | docker login --username your_username --password-stdin
docker build -t <insert member username>/wagess .
docker push <insert member username>/wagess
docker run -p 7000:7000 wagess
```

5. Create a new web app service on Azure, terraform will automatically create the App Service on Azure and configure it using our provided settings. You can change `main.tf` to your settings or do more customizations on Azure Portal if needed.

6. Run the app using the URL provided by Azure.

## Logging
- At first, we tried to use `App Service logs` to log the information of the app and debug. After we begin to run the app on Azure, we found that using `Log stream` is already enough and also more convenient. With the help of the log, we can easily find the error and debug and finally make the app work.

![Alt text](<images/App Service logs.png>)

![Alt text](<images/log stream.png>)


## Load test and quantitative assessment
- We use `locust` to do the load test with several different setting of parameters. `Locust` is an open source load testing tool used to test the performance of web applications. It is designed to be easy to use, highly customizable, and scalable. Locust allows us to simulate the behavior of thousands of concurrent users (virtual users) and measure the performance of our application under different loads.
- We use the following command to run the load test:
```
locust -f load_test.py --host=https://wagess.azurewebsites.net/
```
- After running the command, we can open the web page `http://localhost:8089/` to see the load test user interface. We can set the number of users and the spawn rate to simulate the load. After clicking the `Start swarming` button, the load test will start. The result will be shown in the web page.

- At the beginning, we are using the standard S1 server plan with only one instance, and we set the number of users to 10000 and the spawn rate to 100. The test result is shown as below:

![Alt text](<images/10000-100 original.png>)

As we can see, the average RPS(request per second) is about 100, and the maximum is 395.7 with 206.5 failures. The total percentage of faliues is also a little high. In addition, after we adjust the number of users to 100000 and the spawn rate to 1000, it even could't run. Hence, we upgrade the plan of the server in Azure, and increase the number of instance. Although, according to Azure website, the highest instances we should be able to reach is 30, but we only reach 10, and the result did get better.

10000 users with spawn rate of 100:

![Alt text](<images/10000-100 update.png>)

![Alt text](<images/10000-100 update table.png>)

100000 users with spawn rate of 1000:

![Alt text](<images/100000-1000 update.png>)

![Alt text](<images/100000-1000 update table.png>)

Next, we upgrade the plan to the highest one(Premium v3 P5mv3), and we got a pretty good result:

![Alt text](<images/10000-100 final.jpeg>)

Finally, we adjust the user to 100000 with spawn rate of 1000 and find a suitable waiting time between each request,

![Alt text](<images/final result-1.png>)

The test result is shown as below:

![Alt text](<images/final table.png>)

- Analysis: By applying data science principles, we've quantitatively assessed the system's reliability and stability, focusing on average latency, failure rates, and charts at different levels of load. According to the chart, we can see that after performing scale up and scale out, our app finally reach a great performance with high average RPS. There were 28,531 failures with 971,573 total requests, resulting in a failure rate of approximately 2.94% (28,531 / 971,573), which is already very low, indicating the system's reliability and stability and the robustness of our server. There's a noticeable increase in average latency as the system load goes from 100 Requests/s to 1,000 Requests/s. The increase in average latency suggests that the system may be approaching or experiencing a performance bottleneck as the load intensifies. The system's scalability is a key concern, as it should ideally handle higher loads with minimal impact on latency. In our test result, we notice the wide range between the minimum and maximum response times (30 to 2264875 milliseconds), which is interesting since we didn't expect the system's performance will be various in this large scale. We think that this may due to the difference of network traffics, which make us to conclude that in order to get a more resonable result, we need to run the test multiple times, and wait enough time for each round of test.


## Limitations
The first limitation is that we use a small dataset to do the app, which only have 38 countries' wages data. We can add more countries' data to make the app more informational and useful. In addition, we did not apply any API to connect to data here, which might not be effective and automative. As a result, we need to upload updated data mannually, which is time-consuming. Also, the project rely solely on CSV files for data storage. Integrating additional data sources or databases could enrich the application's data and provide more diverse and up-to-date information.

The second limitation is that While we have performed load testing and improved performance by scaling up and out, there is still a limitation on scalability due to server limitations and potential bottlenecks. Further optimization and distribution of resources could enhance the system's ability to handle even larger loads.

The third limitation is that the user interface of the application is relatively basic, with room for improvement in terms of design and user experience. Enhancing the user interface with more interactive features and visualization options could make the application more user-friendly.

## Potential areas for improvement
First, we could use larger dataset with more information of wage and automate the data loading process with data api of resouces. Another way to improve data loading could be transfering data to databricks and combine it with Azure service. We could also consider enriching the dataset with additional economic indicators, such as inflation rates, GDP growth, or employment statistics. This would allow users to analyze wage growth in a broader economic context.For the user interface, we could make it more intuitive and visually appealing. Implement interactive charts, filters, and user customization options to provide a richer user experience.
## Using Copilot and Chatgpt:
- We use copilot in two ways while writing my code:

    1. Press `Cmd+I` on macOS (or `Ctrl+I` on Windows/Linux) to bring up the Chat input to send request to Copilot. After that, we can choose if we acceptthe suggestion from copilot to write the code. In addition, the suggestion will not be fully correct. We need to modify the code to make it correct, but it provide us a template to write our code, which helps us to write code faster with less errors.

    2. Copilot will also suggest some contents automatically while we are writing code. We can press `Tab` to accept the suggestion from copilot, which also helps us to write code faster with less errors.

- For Chatgpt, it is used in the same way as the first way of using copilot. The difference is that Chatgpt can provide suggestions besides the code. However, its suggestions will not be fully correct as well.

- Hence, there are two advantages of using copilot and Chatgpt:
    1. They helps me to write code faster. 
    2. They helps me to write code with less errors. 

## Reference
https://learn.microsoft.com/en-us/azure/app-service/manage-scale-up

https://learn.microsoft.com/en-us/azure/app-service/troubleshoot-diagnostic-logs
