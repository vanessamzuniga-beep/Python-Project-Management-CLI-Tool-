import requests


class APIClient:
    """Client for retrieving sample tasks from JSONPlaceholder."""

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_task(self, task_id):
        """Fetch a task by ID and return its data."""

        if not isinstance(task_id, int) or isinstance(task_id, bool) or task_id < 1:
            raise ValueError("Task ID must be a positive integer.")

        try:
            response = requests.get(
                f"{self.BASE_URL}/todos/{task_id}",
                timeout=10,
            )
            response.raise_for_status()
        except requests.RequestException as error:
            raise RuntimeError(f"Unable to fetch task from API: {error}") from error

        try:
            task_data = response.json()
        except requests.exceptions.JSONDecodeError as error:
            raise ValueError("API returned invalid JSON.") from error

        if not isinstance(task_data, dict) or not task_data or "id" not in task_data:
            raise ValueError(f"No task found with ID {task_id}.")

        return task_data
