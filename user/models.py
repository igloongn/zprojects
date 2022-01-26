from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField, UUIDField
import uuid

# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE, blank=True, null=True)    
    

    name = models.CharField(max_length=200, blank=True, null=True)

    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True, default='This is the space for "Location"')

    email = models.EmailField(max_length=500, null=True, blank=True)
    short_intro = models.CharField(max_length = 150, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="profile-pics/", default='profile-pics/default.jpg' )
    
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique= True , primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True,null=True)
    name = models.CharField(max_length=130, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique= True , primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


