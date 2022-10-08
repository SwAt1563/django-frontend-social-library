from django import forms

class DashboardSearchForm(forms.Form):
    search_field = forms.CharField(required=True, max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Search...',
        }
    ))