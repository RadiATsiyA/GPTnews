from django import forms

from general.models import Emails, Suggestions


class EmailForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input_area',
        'placeholder': 'Enter your email...'
    }))

    class Meta:
        model = Emails
        fields = ('email',)


class SuggestionForm(forms.ModelForm):
    theme = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'theme_input',
        'placeholder': 'A new life has been found on the moon'
    }))

    class Meta:
        model = Suggestions
        fields = ('theme',)
