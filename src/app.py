from src.tasks import TaskManager
from src.cli import CLI

def main():
    task_manager = TaskManager()
    cli = CLI(task_manager)
    cli.run()

if __name__ == "__main__":
    main()
