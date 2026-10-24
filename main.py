
import argparse
from services.storage_service import load_users, save_users
from services.api_client import APIClient
from models.user import User
from models.project import Project
from models.task import Task


def main():
    parser = argparse.ArgumentParser(
        description="A CLI tool for managing users, projects, and tasks."
    )
    subparsers = parser.add_subparsers(dest="command")

    # Add user
    add_user_parser = subparsers.add_parser("add-user", help="Add a new user.")
    add_user_parser.add_argument("--name", required=True)
    add_user_parser.add_argument("--email", required=True)

    # List users
    subparsers.add_parser("list-users", help="List all users.")

    # Add project
    add_project_parser = subparsers.add_parser(
        "add-project", help="Add a project to a user."
    )
    add_project_parser.add_argument("--user-id", type=int, required=True)
    add_project_parser.add_argument("--title", required=True)
    add_project_parser.add_argument("--description", required=True)
    add_project_parser.add_argument("--due-date", required=True)

    # List projects
    list_projects_parser = subparsers.add_parser(
        "list-projects", help="List projects for a user."
    )
    list_projects_parser.add_argument("--user-id", type=int, required=True)

    # Add task
    add_task_parser = subparsers.add_parser(
        "add-task", help="Add a task to a project."
    )
    add_task_parser.add_argument("--user-id", type=int, required=True)
    add_task_parser.add_argument("--project-id", type=int, required=True)
    add_task_parser.add_argument("--title", required=True)
    add_task_parser.add_argument("--assigned-to", required=True)
    add_task_parser.add_argument(
        "--status",
        choices=["pending", "in progress", "completed"],
        default="pending"
    )

    # List tasks
    list_tasks_parser = subparsers.add_parser(
        "list-tasks", help="List tasks in a project."
    )
    list_tasks_parser.add_argument("--user-id", type=int, required=True)
    list_tasks_parser.add_argument("--project-id", type=int, required=True)

    # Update task status
    update_task_parser = subparsers.add_parser(
        "update-task", help="Update a task's status."
    )
    update_task_parser.add_argument("--user-id", type=int, required=True)
    update_task_parser.add_argument("--project-id", type=int, required=True)
    update_task_parser.add_argument("--task-id", type=int, required=True)
    update_task_parser.add_argument(
        "--status",
        choices=["pending", "in progress", "completed"],
        required=True
    )

    # Import a task from an external API
    import_task_parser = subparsers.add_parser(
        "import-task", help="Import a task from JSONPlaceholder."
    )
    import_task_parser.add_argument("--user-id", type=int, required=True)
    import_task_parser.add_argument("--project-id", type=int, required=True)
    import_task_parser.add_argument("--api-task-id", type=int, required=True)

    args = parser.parse_args()

    if args.command == "add-user":
        users = load_users()
        if any(u.email.lower() == args.email.lower() for u in users):
            print(f"Error: Email '{args.email}' already exists.")
            return
        try:
            new_user = User(args.name, args.email)
            users.append(new_user)
            save_users(users)
            print(f"User '{new_user.name}' added successfully!")
        except (TypeError, ValueError) as error:
            print(f"Error: {error}")

    elif args.command == "list-users":
        users = load_users()
        if not users:
            print("No users found.")
            return
        for user in users:
            print(f"ID: {user.id} | {user}")

    elif args.command == "add-project":
        users = load_users()
        user = next((u for u in users if u.id == args.user_id), None)
        if user is None:
            print(f"Error: User with ID {args.user_id} not found.")
            return
        try:
            project = Project(args.title, args.description, args.due_date)
            user.add_project(project)
            save_users(users)
            print(f"Project '{project.title}' added to {user.name} successfully!")
        except (TypeError, ValueError) as error:
            print(f"Error: {error}")

    elif args.command == "list-projects":
        users = load_users()
        user = next((u for u in users if u.id == args.user_id), None)
        if user is None:
            print(f"Error: User with ID {args.user_id} not found.")
            return
        if not user.projects:
            print(f"No projects found for {user.name}.")
            return
        print(f"Projects for {user.name}:")
        for project in user.projects:
            print(
                f"\nID: {project.id}\nTitle: {project.title}"
                f"\nDescription: {project.description}"
                f"\nDue Date: {project.due_date}"
            )

    elif args.command == "add-task":
        users = load_users()
        user = next((u for u in users if u.id == args.user_id), None)
        if user is None:
            print(f"Error: User with ID {args.user_id} not found.")
            return
        project = next(
            (p for p in user.projects if p.id == args.project_id), None
        )
        if project is None:
            print(f"Error: Project with ID {args.project_id} not found for {user.name}.")
            return
        try:
            task = Task(args.title, args.status, args.assigned_to)
            project.add_task(task)
            save_users(users)
            print(f"Task '{task.title}' added to project '{project.title}'.")
        except (TypeError, ValueError) as error:
            print(f"Error: {error}")

    elif args.command == "list-tasks":
        users = load_users()
        user = next((u for u in users if u.id == args.user_id), None)
        if user is None:
            print(f"Error: User with ID {args.user_id} not found.")
            return
        project = next(
            (p for p in user.projects if p.id == args.project_id), None
        )
        if project is None:
            print(f"Error: Project with ID {args.project_id} not found for {user.name}.")
            return
        if not project.tasks:
            print(f"No tasks found in project '{project.title}'.")
            return
        print(f"Tasks for project '{project.title}':")
        for task in project.tasks:
            print(
                f"\nID: {task.id}\nTitle: {task.title}"
                f"\nStatus: {task.status}\nAssigned to: {task.assigned_to}"
            )

    elif args.command == "update-task":
        users = load_users()
        user = next((u for u in users if u.id == args.user_id), None)
        if user is None:
            print(f"Error: User with ID {args.user_id} not found.")
            return
        project = next(
            (p for p in user.projects if p.id == args.project_id), None
        )
        if project is None:
            print(f"Error: Project with ID {args.project_id} not found for {user.name}.")
            return
        task = next((t for t in project.tasks if t.id == args.task_id), None)
        if task is None:
            print(f"Error: Task with ID {args.task_id} not found.")
            return
        try:
            task.change_status(args.status)
            save_users(users)
            print(f"Task '{task.title}' status updated to '{task.status}'.")
        except (TypeError, ValueError) as error:
            print(f"Error: {error}")

    elif args.command == "import-task":
        users = load_users()
        user = next((u for u in users if u.id == args.user_id), None)
        if user is None:
            print(f"Error: User with ID {args.user_id} not found.")
            return

        project = next(
            (p for p in user.projects if p.id == args.project_id), None
        )
        if project is None:
            print(
                f"Error: Project with ID {args.project_id} "
                f"not found for {user.name}."
            )
            return

        try:
            api_task = APIClient().get_task(args.api_task_id)

            status = "completed" if api_task["completed"] else "pending"
            assigned_to = f"API User {api_task['userId']}"

            task = Task(api_task["title"], status, assigned_to)
            project.add_task(task)
            save_users(users)

            print(
                f"Imported API task '{task.title}' into "
                f"project '{project.title}' successfully!"
            )
        except (RuntimeError, ValueError, TypeError, KeyError) as error:
            print(f"Error importing task: {error}")


if __name__ == "__main__":
    main()
