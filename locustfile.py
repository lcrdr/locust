import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task(3)
    def view_items(self):
        for item_id in range(10):
            self.client.get(f"/planets/{item_id}")
            self.client.get(f"/people/{item_id}")

            time.sleep(1)

  