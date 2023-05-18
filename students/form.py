from django import forms

class PostForm(forms.Form):
    stdName = forms.CharField(max_length=50, initial='', required=True)
    stdID = forms.CharField(max_length=10, initial='', required=True)
    stdSex = forms.CharField(max_length=2, initial="M")
    stdBirth = forms.DateField()
    stdPhone = forms.CharField(max_length=10, initial='', required=False)
    stdEmail = forms.EmailField(max_length=100, initial='', required=False)