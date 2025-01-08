from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BlogPostModel

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'bg-gray-200 rounded pl-12 py-2 md:py-4 focus:outline-none w-full',
        'placeholder': 'Enter your email'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'bg-gray-200 rounded pl-12 py-2 md:py-4 focus:outline-none w-full',
        'placeholder': 'Enter your password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'bg-gray-200 rounded pl-12 py-2 md:py-4 focus:outline-none w-full',
        'placeholder': 'Confirm your password'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'bg-gray-200 rounded pl-12 py-2 md:py-4 focus:outline-none w-full',
                'placeholder': 'Enter your username'
            })
        }


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPostModel
        exclude =  ['author', 'slug', 'created_at', 'updated_at', 'published']
        widgets = {
            'title': forms.TextInput(attrs={
                'class':'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5',
                'placeholder':'Enter Your blog title'
            }), 
            'heading2': forms.TextInput(attrs={
                'class':'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5',
                'placeholder':'Enter Heading Two'
            }), 
            'heading3': forms.TextInput(attrs={
                'class':'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5',
                'placeholder':'Enter Heading Three'
            }), 
            'category': forms.Select(attrs={
                'class':'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-2.5',
            }), 
            'content': forms.Textarea(attrs={
                'class':'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-4',
                'rowa':'4',
            }), 
            'heading2Content': forms.Textarea(attrs={
                'class':'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-4',
                'rowa':' 3',
            }), 
            'heading3Content': forms.Textarea(attrs={
                'class':'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-4',
                'rowa':'3',
            }), 
            'important': forms.Textarea(attrs={
                'class':'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-cyan-600 focus:border-cyan-600 block w-full p-4',
                'rowa':'2',
            }), 
            'main_image': forms.ClearableFileInput(attrs={
                'class':'hidden',
            }), 
            'image': forms.ClearableFileInput(attrs={
                'class':'hidden',
            }), 

        }