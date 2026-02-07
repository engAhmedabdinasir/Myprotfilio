import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from portfolio.models import Project

print("--- Current Projects ---")
for pj in Project.objects.all():
    print(f"Title: {pj.title}")
    print(f"Image: {pj.image}")
    print("-" * 20)
