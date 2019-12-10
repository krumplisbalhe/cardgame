from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from .models import Card, User
from django.contrib.auth.decorators import login_required
from . import forms
import json
import tasks

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
    tasks.echo('****** This is the newly added card: ' + request.POST['cardText'])
    return redirect('cards:openPack')
  else:
    return render(request, 'playcards/card_create.html')

@login_required(login_url="/accounts/login/")
def card_delete(request, pk):
  obj = get_object_or_404(Card, pk=pk)
  if request.method == 'POST':
    obj.delete()
    return redirect('cards:openPack')

@login_required(login_url="/accounts/login/")
def card_play(request):
  if request.method == 'GET':
    name = request.GET.get('name', '')
    if name =='friendship':
      pack = Card.objects.all().filter(packId=1)
      basicPack = pack.filter(author=1)
      ownCards = pack.filter(author=request.user)
      cards = (basicPack | ownCards).distinct()
    if name == 'relationship':
      pack = Card.objects.all().filter(packId=2)
      basicPack = pack.filter(author=1)
      ownCards = pack.filter(author=request.user)
      cards = (basicPack | ownCards).distinct()
    if name == 'family':
      pack = Card.objects.all().filter(packId=3)
      basicPack = pack.filter(author=1)
      ownCards = pack.filter(author=request.user)
      cards = (basicPack | ownCards).distinct()
    return render(request, 'playcards/play.html', {'cards': cards, 'name': name})

############## REST API ##############
def get_card(request, pk):
  if request.method == "GET":
    try:
      card = Card.objects.get(pk=pk)
      user = User.objects.get(pk=card.author_id)
      response = json.dumps({'cardText': card.cardText, 'pack': card.packId, 'authorId': card.author_id, 'authorUserName': user.username})
    except:
      response = json.dumps({'Error': 'No card with this id.'})
  return HttpResponse(response, content_type='text/json')

def get_user(request, pk):
  if request.method == "GET":
    try:
      user = User.objects.get(pk=pk)
      cards = Card.objects.filter(author=pk)
      data = serializers.serialize('json', list(cards), fields=('packId','cardText', 'question'))
      response = json.dumps({'id': user.id,'userName': user.username, 'isSuperUser': user.is_superuser, 'cards': data})
    except:
      response = json.dumps({'Error': 'No user with this id.'})
  return HttpResponse(response, content_type='application/json')

def get_pack(request, pk):
  if request.method == "GET":
    try:
      cards = Card.objects.filter(packId=pk).values()
      return JsonResponse({'pack': list(cards)})
    except:
      response = json.dumps({'Error': 'No pack with this id.'})
      return HttpResponse(response, content_type='application/json')
