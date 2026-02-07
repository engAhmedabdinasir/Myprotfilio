import os
import shutil
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')
django.setup()

from portfolio.models import Project

# Source paths (artifacts)
SOURCE_DIR = r"C:\Users\ahmed\.gemini\antigravity\brain\216f1cde-f660-482f-acc3-fc5fbc31332e"
IMAGES = [
    ("uploaded_image_1_1768810596221.jpg", "graphic_design.jpg", 1),
    ("uploaded_image_2_1768810596221.jpg", "restaurant.jpg", 2),
    ("uploaded_image_3_1768810596221.jpg", "wedding.jpg", 3),
]

MEDIA_ROOT = os.path.join(os.getcwd(), 'media', 'projects')
if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT)

def update_images():
    print("Updating project images...")
    
    # We need to sort projects by ID to ensure mapping is consistent with assumed order
    # logic: ID 1 -> img 1, ID 2 -> img 2, ID 3 -> img 3
    
    projects = list(Project.objects.all().order_by('id'))
    
    # Since we might not have ID 1, 2, 3 exactly if deletions happened, let's just map by index
    # But usually distinct IDs exist.
    
    for src_filename, dest_filename, p_id in IMAGES:
        src_path = os.path.join(SOURCE_DIR, src_filename)
        dest_path = os.path.join(MEDIA_ROOT, dest_filename)
        
        if os.path.exists(src_path):
            print(f"Copying {src_filename} to {dest_filename}...")
            shutil.copy2(src_path, dest_path)
            
            try:
                # Try getting project by ID, or by index if that fails/logic dictates
                # Here we stick to ID as planned
                project = Project.objects.get(pk=p_id)
                # Update image field
                # Note: FileField stores relative path from MEDIA_ROOT usually
                project.image = f"projects/{dest_filename}" 
                project.save()
                print(f"Updated Project {project.id} ({project.title}) with {dest_filename}")
            except Project.DoesNotExist:
                print(f"Project with ID {p_id} not found, skipping update for this image.")
        else:
            print(f"Source file {src_path} not found!")

if __name__ == '__main__':
    update_images()
