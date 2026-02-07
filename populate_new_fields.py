import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from portfolio.models import Profile, Service

def populate():
    profile = Profile.objects.first()
    if profile:
        profile.phone_number = "+252615000000"
        profile.whatsapp_number = "252615000000"
        profile.github_url = "https://github.com/AhmedAbdinasir"
        profile.linkedin_url = "https://linkedin.com/in/AhmedAbdinasir"
        profile.twitter_url = "https://twitter.com/AhmedAbdinasir"
        profile.location = "Mogadishu, Somalia"
        profile.save()
        print("Profile updated.")
    else:
        print("No profile found to update.")

    services = Service.objects.all()
    for service in services:
        if not service.price:
            service.price = "Starting at $50"
            service.save()
    print("Services updated.")

if __name__ == "__main__":
    populate()
