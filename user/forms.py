from django.contrib.auth.models import User
from django.forms import forms
from django.forms import models
from .models import Profile


class ProfileForm(models.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"



        # THIS IS TO CHANGE THE ATTRS IN THE FORM IN THE HTML FILE
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['user'].widget.attrs.update({'class': 'input input--text', 'placeholder':"Add title"})

        self.fields['location'].widget.attrs.update({'class': 'input input--text', })
        self.fields['username'].widget.attrs.update({'class': 'input input--text', 'placeholder':"Username"})

        self.fields['email'].widget.attrs.update({'class': 'input input--text', 'placeholder':"Enter Email Here"})

        self.fields['short_intro'].widget.attrs.update({'class': 'input input--text', 'placeholder':"Short Intro"})

        self.fields['bio'].widget.attrs.update({'class': 'input input--text','placeholder':"Bio"})


        self.fields['social_github'].widget.attrs.update({'class': 'input input--text', 'placeholder':"Github Link"})

        self.fields['social_twitter'].widget.attrs.update({'class': 'input input--text', 'placeholder':"Twitter Link"})

        self.fields['social_website'].widget.attrs.update({'class': 'input input--text', 'placeholder':"Your Website"})
 