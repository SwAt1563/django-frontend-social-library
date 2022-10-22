from django import forms
from django.core.validators import RegexValidator



class PersonalImageForm(forms.Form):
    image = forms.ImageField(help_text="Upload image: ", required=True, widget=forms.FileInput(
        attrs={
            'class': 'file-uploader pull-left',
            'id':'personalImage',
        }
    ))

    def clean(self):
        if not self.cleaned_data.get('image'):
            raise forms.ValidationError('No image')
        image = self.cleaned_data['image']
        image_size = image.size
        # if image more than 10 mega
        if image_size / (10 ** 6) > 10:
            self.errors['image'] = self.error_class(['Big size'])
            raise forms.ValidationError('Big image size')
        return self.cleaned_data

class ProfileEditForm(forms.Form):
    firstname = forms.CharField(required=True, max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your answer',
            'id': 'firstname'
        }
    ))
    lastname = forms.CharField(required=True, max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your answer',
            'id': 'lastname'
        }
    ))
    age = forms.IntegerField(required=True, max_value=1000, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your answer',
            'id': 'age'
        }
    ))
    address = forms.CharField(required=True, max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your answer',
            'id': 'address'
        }
    ))
    status = forms.CharField(required=True, max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your answer',
            'id': 'status'
        }
    ))
    phone = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your answer',
            'id': 'phone',
            'type': 'number',

        }
    ))
    about_me = forms.CharField(required=True, max_length=5000, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your answer',
            'id': 'aboutme',
            'name': 'aboutme',
        }
    ))


    def clean(self):
        import re
        if not self.cleaned_data.get('phone'):
            raise forms.ValidationError('No Phone')
        phone = self.cleaned_data.get('phone')
        match = re.match(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', phone)
        if not match:
            self.errors['phone'] = self.error_class(['Wrong phone format'])
            raise forms.ValidationError('Wrong phone format')
        return self.cleaned_data