from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Textarea, IntegerField
from .models import Image, Profile, Follow


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'likes']


        
# class CommentForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['comment'].widget = forms.TextInput()
#         self.fields['comment'].widget.attrs['placeholder'] = 'Add a comment...'

#     class Meta:
#         model = Comment
#         fields = ('comment',)

class UpdatebioForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'followers', 'following']


class NewsLetterForm(forms.ModelForm):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
