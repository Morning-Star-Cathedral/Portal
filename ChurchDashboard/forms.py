from django import forms
from .models import *


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = (
            'name',
        )


class CreateChapelForm(forms.ModelForm):
    class Meta:
        model = Chapels
        fields = (
            'name',
        )


# class CreateMemberForm(forms.ModelForm):
#     class Meta:
#         model = Members
#         feilds = ('_all_')