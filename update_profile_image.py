import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from portfolio.models import Profile

# Update or create profile with the image
profile, created = Profile.objects.get_or_create(
    name="Ahmed Abdinasir",
    defaults={
        'title': "Full Stack Developer",
        'bio': "I am a passionate software engineer with expertise in Django, Python, and modern frontend technologies. I build scalable and user-friendly web applications."
    }
)

# Update the profile image
profile.profile_image = 'profile/ahmed.jpg'
profile.save()

print(f"Profile {'created' if created else 'updated'} successfully!")
print(f"Name: {profile.name}")
print(f"Image: {profile.profile_image}")
