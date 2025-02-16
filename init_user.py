from django.contrib.auth.models import User
import os

username = os.getenv("DJANGO_SUPERUSER_USERNAME", "1")
email = os.getenv("DJANGO_SUPERUSER_EMAIL", "")
password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "1")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created")
else:
    print("Superuser already exists")