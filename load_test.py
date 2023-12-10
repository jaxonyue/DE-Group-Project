from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(0.1, 0.5)

    @task
    def load_wages(self):
        self.client.get("https://wagesviz.azurewebsites.net/")