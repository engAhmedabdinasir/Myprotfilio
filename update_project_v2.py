import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from portfolio.models import Project

# Update the "My Portfolio" project
project = Project.objects.filter(title="My Portfolio").first()
if project:
    project.description = "A responsive web application built to highlight development skills, featured projects, and technologies used."
    project.technology = "A modern portfolio project designed to showcase skills, projects, and experience with a clean and professional interface."
    project.save()
    print("Project 'My Portfolio' updated (description and technology)!")
else:
    # Fallback to first project if "My Portfolio" not found
    project = Project.objects.first()
    if project:
        project.description = "A responsive web application built to highlight development skills, featured projects, and technologies used."
        project.technology = "A modern portfolio project designed to showcase skills, projects, and experience with a clean and professional interface."
        project.save()
        print(f"Project '{project.title}' updated (description and technology)!")
    else:
        print("No projects found.")
