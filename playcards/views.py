from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Card, User
from django.contrib.auth.decorators import login_required
from . import forms
import json

@login_required(login_url="/accounts/login/")
def open_pack(request):
  return render(request, 'playcards/dashboard.html')

@login_required(login_url="/accounts/login/")
def pack(request):
  if request.method == 'POST':
    if 'friendship' in request.POST:
      name = 'friendship'
      pack = Card.objects.all().filter(packId=1)
      basicPack = pack.filter(author=1)
      ownCards = pack.filter(author=request.user)
    if 'relationship' in request.POST:
      name = 'relationship'
      pack = Card.objects.all().filter(packId=2)
      basicPack = pack.filter(author=1)
      ownCards = pack.filter(author=request.user)
    if 'family' in request.POST:
      name = 'family'
      pack = Card.objects.all().filter(packId=3)
      basicPack = pack.filter(author=1)
      ownCards = pack.filter(author=request.user)
    return render(request, 'playcards/pack.html', {'ownCards': ownCards, 'basicPack': basicPack, 'name': name})


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

@login_required(login_url="/accounts/login/")
def card_delete(request, pk):
  obj = get_object_or_404(Card, pk=pk)
  if request.method == 'POST':
    obj.delete()
    return redirect('cards:openPack')


def get_card(request, pk):
  if request.method == "GET":
    try:
      card = Card.objects.get(pk=pk)
      print('************', vars(card))
      response = json.dumps({'cardText': card.cardText, 'pack': card.packId, 'author': card.author_id})
    except:
      response = json.dumps({'Error': 'No card with this id.'})
  return HttpResponse(response, content_type='text/json')
