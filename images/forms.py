from django import forms

from .models import SimpleModel


class UserForm(forms.ModelForm):

    class Meta:
        model = SimpleModel
        fields = ('image',)
