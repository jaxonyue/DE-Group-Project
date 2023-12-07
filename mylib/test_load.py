from locust import HttpUser, task, between
import csv

class MyUser(HttpUser):
    wait_time = between(0.1, 0.5)  # Add some delay between requests

    def on_start(self):
        # Read a sample CSV file for generating requests
        dataset = "dataset/Development of Average Annual Wages.csv"
        with open(dataset, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            self.request_data = list(csv_reader)

    @task
    def load_test(self):
        # Pick a random row from the CSV and send a POST request to the microservice
        data = self.request_data[self.user % len(self.request_data)]
        response = self.client.post("http://0.0.0.0:7000/api/wages", json=data)
