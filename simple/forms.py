# THE CREATE UPDATE AND DELETE  
from django.db.models import fields
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Project, Signup

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['title', 'description', 'featured_image', 'demo_link', 'source_link', 'tag']
        widgets = {
            'tag':forms.CheckboxSelectMultiple()
        }

    # THIS IS TO CHANGE THE ATTRS IN THE FORM IN THE HTML FILE
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'input input--text', 'placeholder':"Add title"})

        self.fields['description'].widget.attrs.update({'class': 'input input--text', 'placeholder':"Add title"})

        self.fields['featured_image'].widget.attrs.update({'class': 'input input--text', 'placeholder':"Add title"})

        self.fields['demo_link'].widget.attrs.update({'class': 'input input--text', 'placeholder':"Add title"})

        self.fields['source_link'].widget.attrs.update({'class': 'input input--text','placeholder':"Add title"})


        self.fields['tag'].widget.attrs.update({'class': 'input input--text', 'placeholder':"Add title"})
 


    # THIS IS TO MAKE THINGS FASTER
        # for name, field in self.register.items():
        #     field.widget.attrs.update({'class':'input'})
         
        

class SignupForm(ModelForm):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ("first_name", "username", "email", "password", )