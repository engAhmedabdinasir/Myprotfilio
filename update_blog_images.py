import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from portfolio.models import BlogPost

# Update "Why Tailwind CSS?"
post1 = BlogPost.objects.filter(title="Why Tailwind CSS?").first()
if post1:
    post1.image = 'blog/tailwind.png'
    post1.save()
    print("Updated 'Why Tailwind CSS?' with image.")

# Update "Getting Started with Django"
post2 = BlogPost.objects.filter(title="Getting Started with Django").first()
if post2:
    post2.image = 'blog/django.png'
    post2.save()
    print("Updated 'Getting Started with Django' with image.")
