import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from portfolio.models import Profile

# Update profile with the new professional image
profile = Profile.objects.filter(name="Ahmed Abdinasir").first()
if profile:
    profile.profile_image = 'profile/ahmed_v2.jpg'
    profile.save()
    print("Profile image updated to the new professional photo!")
else:
    print("Profile not found.")
