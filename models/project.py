from models.task import Task

class Project:
    # Class Attribute
    count = 0


    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []
        Project.count += 1
        self.id = Project.count

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
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError("description must be a string")
        if not value.strip():
            raise ValueError("description cannot be empty")
        self._description = value


    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        if not isinstance(value, str):
            raise TypeError("due date must be a string")
        if not value.strip():
            raise ValueError("due date cannot be empty")
        self._due_date = value



    # Instance Method
    def add_task(self, task):
        if not isinstance(task, Task):
            raise TypeError("task must be a Task instance")
        self.tasks.append(task)

    def convert_to_dictionary(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": [task.convert_to_dictionary() for task in self.tasks]
        }



    # Class Method
    @classmethod
    def from_dictionary(cls, data):
        project = cls(data["title"], data["description"], data["due_date"])
        project.id = data["id"]
        cls.count = max(cls.count, project.id)
        for task_data in data["tasks"]:
            task = Task.from_dictionary(task_data)
            project.add_task(task)
        return project



    # CLI Output
    def __str__(self):
        return f'Project Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}'