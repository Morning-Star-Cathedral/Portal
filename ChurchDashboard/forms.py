from django import forms
from .models import *


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = (
            'name',
        )
