from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class JobSearchForm(forms.Form):
    job_title = forms.CharField(label='Job title', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Job title, keywords or company'}))
    location = forms.CharField(label='Location', max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'State, city or zip code'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
