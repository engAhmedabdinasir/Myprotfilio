import os
import django
from django.utils.text import slugify
from django.core.files.base import ContentFile

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from portfolio.models import Profile, Skill, Service, Project, BlogPost

def populate():
    print("Populating database...")

    # Profile
    if not Profile.objects.exists():
        Profile.objects.create(
            name="Ahmed Abdinasir",
            title="Full Stack Developer",
            bio="I am a passionate software engineer with expertise in Django, Python, and modern frontend technologies. I build scalable and user-friendly web applications."
        )
        print("Profile created.")

    # Skills
    skills = [
        ("Python", "fab fa-python", 90),
        ("Django", "fas fa-server", 85),
        ("HTML5", "fab fa-html5", 95),
        ("CSS3", "fab fa-css3-alt", 80),
        ("JavaScript", "fab fa-js", 75),
        ("PostgreSQL", "fas fa-database", 70),
    ]
    for name, icon, prof in skills:
        Skill.objects.get_or_create(name=name, defaults={'icon': icon, 'proficiency': prof})
    print("Skills created.")

    # Services
    services = [
        ("Web Development", "I build responsive and fast websites using modern technologies.", "fas fa-code"),
        ("Backend Development", "Robust API development and database management.", "fas fa-server"),
        ("Consulting", "Tech consulting and architecture planning.", "fas fa-comment-dots"),
    ]
    for title, desc, icon in services:
        Service.objects.get_or_create(title=title, defaults={'description': desc, 'icon': icon})
    print("Services created.")

    # Projects
    projects = [
        ("My Portfolio", "A personal portfolio website built with Django and Tailwind CSS.", "Django, Tailwind CSS", None),
        ("E-commerce Store", "A full-featured e-commerce platform with payment gateway integration.", "Python, Django, Stripe", None),
        ("Task Manager", "A productivity app to manage daily tasks and collaborate with teams.", "React, Django REST Framework", None),
    ]
    for title, desc, tech, img in projects:
        Project.objects.get_or_create(title=title, defaults={'description': desc, 'technology': tech})
    print("Projects created.")

    # Blog Post
    posts = [
        ("Getting Started with Django", "Django is a high-level Python web framework..."),
        ("Why Tailwind CSS?", "Utility-first CSS framework for rapid UI development..."),
    ]
    for title, content in posts:
        slug = slugify(title)
        BlogPost.objects.get_or_create(title=title, defaults={'slug': slug, 'content': content})
    print("Blog posts created.")

    print("Database populated successfully!")

if __name__ == '__main__':
    populate()
