from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Card
from django.contrib.auth.decorators import login_required
from . import forms

# def playcards_list(request):
#   usersCards = Card.objects.all().filter(author=request.user)
#   defaultCards = Card.objects.all().filter(author=1)
#   return render(request, 'playcards/playcards_list.html', {'usersCards': usersCards, 'defaultCards': defaultCards})

@login_required(login_url="/accounts/login/")
def open_pack(request):
  return render(request, 'playcards/dashboard.html')

@login_required(login_url="/accounts/login/")
def pack(request):
  if request.method == 'POST':
    if 'friendship' in request.POST:
      name = 'friendship'
      pack = Card.objects.all().filter(packId=1)
    if 'relationship' in request.POST:
      name = 'relationship'
      pack = Card.objects.all().filter(packId=2)
    if 'family' in request.POST:
      name = 'family'
      pack = Card.objects.all().filter(packId=3)
    return render(request, 'playcards/pack.html', {'pack': pack, 'name': name})

@login_required(login_url="/accounts/login/")
def card_create(request):
  packIdToNumber = None
  if request.method == 'POST':
    if request.POST['packId'] == 'friendship':
      packIdToNumber = 1
    if request.POST['packId'] == 'relationship':
      packIdToNumber = 2
    if request.POST['packId'] == 'family':
      packIdToNumber = 3
    card = Card()
    card.packId = packIdToNumber
    card.cardText = request.POST['cardText']
    card.author = request.user
    card.save()
    # if form.is_valid():
    #   instance = form.save(commit=False)
    #   instance.author = request.user
    #   instance.save()
    return redirect('cards:openPack')
  else:
    return render(request, 'playcards/card_create.html')
