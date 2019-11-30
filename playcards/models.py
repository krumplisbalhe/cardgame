from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
  packId = models.PositiveIntegerField(default=1)
  cardText = models.CharField(max_length=250)
  author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

  def __str__(self):
    return self.cardText
