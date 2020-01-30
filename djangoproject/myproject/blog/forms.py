from django import forms


class Blog(forms.Form):
    title = forms.CharField()
    blog = forms.CharField(widget=forms.Textarea)
    