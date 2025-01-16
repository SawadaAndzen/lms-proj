from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'profile')
    pfp = models.ImageField(upload_to = 'profile/pfp/', blank = True, null = True, default='static/profile/default-pfp.jpg')
    desc = models.TextField()
    
    def save(self, *args, **kwargs):
        if not self.pfp:
            self.pfp = '/static/profile/default-pfp.jpg'
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"@{self.user.username}'s profile"