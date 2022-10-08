from django import forms



class PostSearchForm(forms.Form):
    post_search = forms.CharField(max_length=500, required=True, widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter Search term...',
            'aria-label':'Enter search term...',
            'aria-describedby': 'button-search'
        }
    ))

class PeopleSearchForm(forms.Form):
    people_search = forms.CharField(max_length=500, required=True, widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter the name...',
            'aria-label':'Enter search term...',
            'aria-describedby': 'button-search'
        }
    ))