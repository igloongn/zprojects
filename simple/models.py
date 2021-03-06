from django.db import models
import uuid
from django.contrib.auth.models import User

from django.db.models.deletion import CASCADE

from user.models import Profile

# Create your models here.

class Project(models.Model):

    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)

    title = models.CharField(max_length = 200)
    description = models.TextField(null=True, blank= True)
    featured_image = models.ImageField(null=True, blank=True, default = "default.jpg")
    demo_link = models.CharField(max_length=200, blank=True, null=True)
    source_link = models.CharField(max_length=2000, blank=True, null=True)
    tag = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, blank=True, null=True)
    vote_ratio = models.IntegerField(default=0, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique= True , primary_key=True, editable=False)
    
    def __str__(self):
        return self.title

class Reviews(models.Model):
    VOTE_TYPE = ( 
        ("up","Up Vote"),
        ("down","Down Vote"),
    )
    # owner
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length = 150, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique= True , primary_key=True, editable=False)
    

    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length = 150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique= True , primary_key=True, editable=False)
    


    def __str__(self):
        return self.name
            
class Signup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    


        

