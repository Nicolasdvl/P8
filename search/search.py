from django import forms

class SearchForm(forms.Form):
    product_id = forms.CharField(widget=forms.HiddenInput(attrs={'id':'product_id'}))
    myInput = forms.CharField(label='', widget=forms.TextInput(attrs={'id':'myInput'}))