from django import forms
from . import models

class CreateCard(forms.ModelForm):
  class Meta:
    model = models.Card
    fields = ['packId', 'cardText']
