from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(0.01, 0.05)

    @task
    def load_wages(self):
        self.client.get("https://wagess.azurewebsites.net")

    # @task
    # def load_wages(self):
    #     self.client.get("https://wagess.azurewebsites.net")
    
    # @task
    # def load_wages(self):
    #     self.client.get("https://wagess.azurewebsites.net")

    # @task
    # def load_wages(self):
    #     self.client.get("https://wagess.azurewebsites.net")
    
    # @task
    # def load_wages(self):
    #     self.client.get("https://wagess.azurewebsites.net")

    # @task
    # def load_wages(self):
    #     self.client.get("https://wagess.azurewebsites.net")

    # @task
    # def load_wages(self):
    #     self.client.get("https://wagess.azurewebsites.net")

    # @task
    # def load_wages(self):
    #     self.client.get("https://wagess.azurewebsites.net")

    # @task
    # def load_wages(self):
    #     self.client.get("https://wagess.azurewebsites.net")

    # @task
    # def load_wages(self):
    #     self.client.get("https://wagess.azurewebsites.net")