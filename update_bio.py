import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from portfolio.models import Profile

# Update the profile bio
profile = Profile.objects.filter(name="Ahmed Abdinasir").first()
if profile:
    profile.bio = "I am a passionate software engineer with expertise in Django, Python, and modern frontend technologies. I build scalable and user-friendly web applications."
    profile.save()
    print("Profile bio updated in database!")
else:
    print("Profile not found.")
