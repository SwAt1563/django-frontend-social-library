from django import forms


def correct_email(email):
    import re
    return re.match(r'^[0-9]{7}@student\.birzeit\.edu$', email)

class LoginForm(forms.Form):
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'id': 'email_input',
            'placeholder': '*******@student.birzeit.edu',
        }
    ))
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'password_input',
            'placeholder': '*******',
        }
    ))

    def clean(self):
        email = self.cleaned_data.get('email')
        if not correct_email(email):
            self.errors['email'] = self.error_class(['You should use university format'])
            raise forms.ValidationError('wrong email')
        return self.cleaned_data


QUESTIONS = (
    ('', 'Select Question'),
    ('Who is your best friend', "Who is your best friend"),
    ('What is your dog name', 'What is your dog name'),
)
class RegisterForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'reg_username',
            'placeholder': 'Username',
            'name': 'user_email',
        }
    ))
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'id': 'reg_useremail',
            'placeholder': '*******@student.birzeit.edu',
            'name': 'user_email',
        }
    ))
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'reg_userpassword',
            'placeholder': 'Password',
            'name': "user_password",
            'data-placement': "bottom",
            'data-toggle': "popover",
            'data-container': "body",
            'data-html': "true",
        }
    ))
    password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'reg_userpasswordconfirm',
            'placeholder': 'Password Confirm',
            'data-placement': "bottom",
            'data-toggle': "popover",
            'data-container': "body",
            'data-html': "true",
        }
    ))
    question = forms.ChoiceField(required=True, choices=QUESTIONS, widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'reg_userquestion',
            'name': 'user_question',
        }
    ))
    answer = forms.CharField(required=True, max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'reg_useranswer',
            'placeholder': 'Your answer',
            'name': 'user_answer'
        }
    ))

    def clean(self):
        email = self.cleaned_data.get('email')
        question = self.cleaned_data.get('question')
        pass1, pass2 = self.cleaned_data.get('password'), self.cleaned_data.get('password2')
        if not correct_email(email):
            self.errors['email'] = self.error_class(['You should use university format'])
            raise forms.ValidationError('wrong email')

        if not question or len(question) == 0:
            self.errors['question'] = self.error_class(['You should choose question'])
            raise forms.ValidationError('no question')

        if not pass1 or not pass2 or str(pass1) != str(pass2):
            self.errors['password'] = self.error_class(['You should enter correct password'])
            raise forms.ValidationError('password error')

        '''
         We should check the unique email if it is exist before or not and raise not unique error to html
         but username not matter if its not unique
        '''

        return self.cleaned_data


class ResetEmailForm(forms.Form):
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'id': 'reg_useremail',
            'placeholder': '*******@student.birzeit.edu',
            'name': 'user_email',
        }
    ))
    question = forms.ChoiceField(required=True, choices=QUESTIONS, widget=forms.Select(
        attrs={
            'class': 'form-control',
            'id': 'reg_userquestion',
            'name': 'user_question',
        }
    ))
    answer = forms.CharField(required=True, max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'reg_useranswer',
            'placeholder': 'Your answer',
            'name': 'user_answer'
        }
    ))

    def clean(self):
        email = self.cleaned_data.get('email')
        question = self.cleaned_data.get('question')

        if not correct_email(email):
            self.errors['email'] = self.error_class(['You should use university format'])
            raise forms.ValidationError('wrong email')

        if not question or len(question) == 0:
            self.errors['question'] = self.error_class(['You should choose question'])
            raise forms.ValidationError('no question')
        return self.cleaned_data

class ResetPasswordForm(forms.Form):
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'reg_userpassword',
            'placeholder': 'Password',
            'name': "user_password",
            'data-placement': "bottom",
            'data-toggle': "popover",
            'data-container': "body",
            'data-html': "true",
        }
    ))
    password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'reg_userpassword',
            'placeholder': 'Password',
            'name': "user_password",
            'data-placement': "bottom",
            'data-toggle': "popover",
            'data-container': "body",
            'data-html': "true",
        }
    ))

    def clean(self):
        pass1, pass2 = self.cleaned_data.get('password'), self.cleaned_data.get('password2')

        if str(pass1) != str(pass2):
            self.errors['password2'] = self.error_class(['You should enter right confirm password'])
            raise forms.ValidationError('password error')


        return self.cleaned_data