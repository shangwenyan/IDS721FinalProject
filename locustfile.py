from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    def on_start(self):
        self.client.post("/", {
        })
    
    @task
    def html(self):
        self.client.get("/html")