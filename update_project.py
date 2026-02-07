import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from portfolio.models import Project

# Update the "My Portfolio" project description
project = Project.objects.filter(title="My Portfolio").first()
if project:
    project.description = "A responsive web application built to highlight development skills, featured projects, and technologies used."
    project.save()
    print("Project 'My Portfolio' updated in database!")
else:
    # If it doesn't exist, create it or try to find another one
    project = Project.objects.first()
    if project:
        project.description = "A responsive web application built to highlight development skills, featured projects, and technologies used."
        project.save()
        print(f"Project '{project.title}' updated in database!")
    else:
        print("No projects found.")
