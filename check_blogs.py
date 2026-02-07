import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from portfolio.models import BlogPost

print("--- Current Blog Posts ---")
for post in BlogPost.objects.all():
    print(f"Title: {post.title}")
    print(f"Image: {post.image}")
    print(f"Slug: {post.slug}")
    print("-" * 20)
