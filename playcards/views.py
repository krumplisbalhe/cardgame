from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Card
from django.contrib.auth.decorators import login_required
from . import forms

def playcards_list(request):
  cards = Card.objects.all()
  return render(request, 'playcards/playcards_list.html', {'cards': cards})

@login_required(login_url="/accounts/login/")
def card_create(request):
  if request.method == 'POST':
    form = forms.CreateCard(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.author = request.user
      instance.save()
      return redirect('cards:list')
  else:
    form = forms.CreateCard()
  return render(request, 'playcards/card_create.html', {'form': form})
