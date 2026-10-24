class Task:
    # Class Attribute
    count = 0


    def __init__(self, title, status, assigned_to):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to
        Task.count += 1
        self.id = Task.count


    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("title must be a string")
        if not value.strip():
            raise ValueError("title cannot be empty")
        self._title = value


    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if not isinstance(value, str):
            raise TypeError("status must be a valid string")
        if value not in ["pending", "in progress", "completed"]:
            raise ValueError('status must be listed as "pending", "in progress", or "completed"')
        self._status = value


    @property
    def assigned_to(self):
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, value):
        if not isinstance(value, str):
            raise TypeError("assigned_to must be a string")
        if not value.strip():
            raise ValueError("assigned_to cannot be empty")
        self._assigned_to = value



    # Instance Method
    def change_status(self, new_status):
        self.status = new_status

    def convert_to_dictionary(self):
        return {
            "id": self.id, 
            "title": self.title, 
            "status": self.status, 
            "assigned_to": self.assigned_to
            }



    # Class Method
    @classmethod
    def from_dictionary(cls, data):
        task = cls(data["title"], data["status"], data["assigned_to"])
        task.id = data["id"]
        cls.count = max(cls.count, task.id)
        return task



    # CLI Output
    def __str__(self):
        return f'Task Title: {self.title}\nStatus: {self.status}\nAssigned to: {self.assigned_to}'

    