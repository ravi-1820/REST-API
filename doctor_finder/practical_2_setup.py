import os
import subprocess
import sys

def setup_django_project():
    print("Setting up the Django Project Environment...")
    
    # Check if requirements.txt exists
    if not os.path.exists("requirements.txt"):
        print("requirements.txt not found. Creating a default one.")
        with open("requirements.txt", "w") as f:
            f.write("Django\ndjangorestframework\nrequests\n")

    # Install packages
    print("Installing packages from requirements.txt...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    # Initialize a new Django project named doctor_project
    project_name = "doctor_project"
    if not os.path.exists(project_name):
        print(f"Creating Django project '{project_name}'...")
        subprocess.check_call([sys.executable, "-m", "django", "startproject", project_name])
    else:
        print(f"Project '{project_name}' already exists.")
        
    print("Setup Complete.")

if __name__ == "__main__":
    setup_django_project()
