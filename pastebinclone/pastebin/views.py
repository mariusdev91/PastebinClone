from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from datetime import datetime
from pastebin.models import Pastebin

def checkForUser(request):
    username = None
    if request.user.is_authenticated:
        username = request.user
        return username
    else:
        username = 'guest'
        return username

def createPaste(request):
    if request.method=='POST':
        title = request.POST['title']
        user = checkForUser(request)
        pastebin = request.POST['pastebin']
        pub_date = datetime.now()
        syntax = request.POST['syntax']
        paste = Pastebin.objects.create(title=title, author=user, content=pastebin, pub_date=pub_date, syntax=syntax)
        paste.save()
        return redirect('/pastebin/')
    else:
        return render(request, "home.html")

def pastebins(request):
    pastebins = Pastebin.objects.order_by('-pub_date')[:10]
    return render(request, "pastebins.html", {"pastebins": pastebins})

def pastebinDetails(request, pastebin_id):
    pastebin = get_object_or_404(Pastebin, pk=pastebin_id)
    return render(request, "pastebin/pastedetail.html", {'pastebin': pastebin})

