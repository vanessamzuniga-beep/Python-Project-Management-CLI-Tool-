from models.project import Project

class User:
    # Class Attribute
    count = 0


    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.projects = []
        User.count += 1
        self.id = User.count

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        if not value.strip():
            raise ValueError("name cannot be empty")
        self._name = value


    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("email must be a string")
        if not value.strip():
            raise ValueError("email cannot be empty")
        self._email = value



    # Instance Methods
    def add_project(self, project):
        if not isinstance(project, Project):
            raise TypeError("project must be a Project instance")
        self.projects.append(project)

    def convert_to_dictionary(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": [project.convert_to_dictionary() for project in self.projects]
        }



    # Class Method
    @classmethod
    def from_dictionary(cls, data):
        user = cls(data["name"], data["email"])
        user.id = data["id"]
        cls.count = max(cls.count, user.id)
        for project_data in data["projects"]:
            project = Project.from_dictionary(project_data)
            user.add_project(project)
        return user



    # CLI Output
    def __str__(self):
        return f'{self.name} ({self.email})'