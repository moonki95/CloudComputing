from django import forms
from .models import SearchList

class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchList
        fields = ('title', 'price')