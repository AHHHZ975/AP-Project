from django import forms
from . import models

class company(forms.ModelForm):
    class Meta:
        model = models.company
        model = models.assets
        model = models.currentAssets
        fields = "__all__"
        # exclude = ['name']