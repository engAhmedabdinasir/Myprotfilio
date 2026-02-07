import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from portfolio.models import Project

def update_images():
    # Update Portfolio Project
    try:
        p1 = Project.objects.get(title="My Portfolio")
        p1.image = 'projects/portfolio.png'
        p1.save()
        print(f"Updated {p1.title}")
    except Project.DoesNotExist:
        print("Portfolio project not found")

    # Update E-commerce Project
    try:
        p2 = Project.objects.get(title="E-commerce Store")
        p2.image = 'projects/ecommerce.png'
        p2.save()
        print(f"Updated {p2.title}")
    except Project.DoesNotExist:
        print("E-commerce project not found")

    # Update Task Manager Project
    try:
        p3 = Project.objects.get(title="Task Manager")
        p3.image = 'projects/task_manager.png'
        p3.save()
        print(f"Updated {p3.title}")
    except Project.DoesNotExist:
        print("Task Manager project not found")

if __name__ == '__main__':
    update_images()
