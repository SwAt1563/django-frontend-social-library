from django import forms

class PostUpdateForm(forms.Form):
    title = forms.CharField(required=True, max_length=100, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Leave a comment here',
            'id': 'post_title',
        }
    ))
    description = forms.CharField(required=True, max_length=100, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Leave a comment here',
            'id': 'floatingTextarea2',
            'style': 'height: 100px;',
        }
    ))

class PostForm(PostUpdateForm):
    uploaded_file = forms.FileField(required=True, widget=forms.FileInput(
        attrs={
            'class': 'form-control form-control-lg',
            'id': 'formFileLg',

        }
    ))

    def clean(self):
        if not self.cleaned_data.get('uploaded_file'):
            raise forms.ValidationError('no files')

        file = self.cleaned_data.get('uploaded_file')
        file_name = file.name
        file_size = file.size

        if file_size / (10 ** 6) > 10:
            self.errors['uploaded_file'] = self.error_class(['Big size'])
            raise forms.ValidationError('Big size file')

        check_image = file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))
        check_pdf = file_name.lower().endswith('.pdf')

        if not check_image and not check_pdf:
            self.errors['uploaded_file'] = self.error_class(['File type not supported'])
            raise forms.ValidationError('File type not supported')
        elif check_pdf:
            self.cleaned_data.update({'pdf': file})
        elif check_image:
            self.cleaned_data.update({'image': file})

        return self.cleaned_data


class StarForm(forms.Form):
    star = forms.CharField(required=True, widget=forms.HiddenInput(
        attrs={
            'value': "yes",
        }
    ))
    unlike = forms.CharField(required=True, widget=forms.HiddenInput(
        attrs={
            'value': "no",
        }
    ))


class CommentForm(forms.Form):
    comment = forms.CharField(required=True, max_length=200, widget=forms.TextInput(
        attrs={

            'class': "form-control",
            'placeholder': "Add a comment",
        }
    ))
