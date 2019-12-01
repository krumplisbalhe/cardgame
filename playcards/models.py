from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete

class Card(models.Model):
  packId = models.PositiveIntegerField(default=1)
  cardText = models.CharField(max_length=250)
  author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

  def __str__(self):
    return self.cardText

def after_delete_post(sender, instance, **kwargs):
  print("******Someone deleted a card")

post_delete.connect(after_delete_post, sender=Card)
