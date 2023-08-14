from django.db import models
from django.contrib.auth.models import User

# User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.jpg')
    location = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return str(self.user.username)
